import torch
import numpy as np

from src.python.RL.SudokuEnv import SudokuEnv
from src.python.RL.SudokuAgent import SudokuAgent
from src.python.RL.agentUtils import ReplayMemory

class SudokuPlayer(SudokuEnv):
    def __init__(self, N, rootEx, rootSol, save_dir):
        super(SudokuPlayer, self).__init__(N, rootEx, rootSol)
        self.memory = ReplayMemory(10000)
        self.gamma = 0.9
        self.exploration_rate = 1.
        self.exploration_rate_decay = 0.99999
        self.exploration_rate_min = 0.1
        self.curr_step = 0
        self.save_every = 100000
        self.batch_size = 32
        self.burnin = 1e4  # min. experiences before training
        self.learn_every = 3  # no. of experiences between updates to Q_online
        self.sync_every = 1e4  # no. of experiences between Q_target & Q_online sync

        self.save_dir = save_dir

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.net = SudokuAgent().to(self.device)
        self.optimizer = torch.optim.Adam(self.net.parameters(), lr=0.00025)
        self.loss_fn = torch.nn.SmoothL1Loss()



    def act(self, state):
        # To be modified
        action = None
        if np.random.rand() < self.exploration_rate:
            action = np.random.randint((self.N*self.N*self.N))
        else:
            action = self.net(state, model="online").argmax().item()
            #action = np.array([value//81, (value%81)//9, (value%81)%9])
            
        self.curr_step+=1
        self.exploration_rate *= self.exploration_rate_decay
        self.exploration_rate = max(self.exploration_rate_min, self.exploration_rate)
            
        return action


    def cache(self, state, action, next_state, reward, done):
        state, action, next_state, reward, done = (torch.from_numpy(state).to(self.device), torch.tensor(action).to(self.device),
                                                torch.from_numpy(np.array([next_state])).to(self.device),torch.tensor([reward]).to(self.device), torch.tensor([done]).to(self.device)
                                                )                                     
        self.memory.push(state, action, next_state, reward, done)

    def recall(self):
        return self.memory.sample(self.batch_size)

    def td_estimate(self, state, action):
        # print(self.net(state, model="online"))
        # print(self.net(state, model="online").shape)
        # print(action.shape)
        
        # print(action)
        # Wrong shape for action
        current_Q = self.net(state, model="online")[
            np.arange(0, self.batch_size), action
        ]  # Q_online(s,a)
        return current_Q

    @torch.no_grad()
    def td_target(self, reward, next_state, done):
        next_state_Q = self.net(next_state, model="online")
        best_action = torch.argmax(next_state_Q, axis=1)
        next_Q = self.net(next_state, model="target")[
            np.arange(0, self.batch_size), best_action
        ]
        return (reward + (1 - done.float()) * self.gamma * next_Q).float()

    def update_Q_online(self, td_estimate, td_target):
        loss = self.loss_fn(td_estimate, td_target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return loss.item()


    def sync_Q_target(self):
        self.net.target.load_state_dict(self.net.online.state_dict())


    def save(self):
        save_path = (
            self.save_dir / f"sudoku_net_{int(self.curr_step // self.save_every)}.chkpt"
        )
        torch.save(
            dict(model=self.net.state_dict(), exploration_rate=self.exploration_rate),
            save_path,
        )
        print(f"SudokuNet saved to {save_path} at step {self.curr_step}")


    def learn(self):
        if self.curr_step % self.sync_every == 0:
            self.sync_Q_target()

        if self.curr_step % self.save_every == 0:
            self.save()

        if self.curr_step < self.burnin:
            return None, None

        if self.curr_step % self.learn_every != 0:
            return None, None

        # Sample from memory
        # print(len(self.recall()))
        # print(type(self.recall()))
    
        state, action, next_state, reward, done = self.recall()

        # print(state)
        # print(action)
        # print(state.shape)
        # print(action.shape)
        # Get TD Estimate
        td_est = self.td_estimate(state, action)

        # Get TD Target
        td_tgt = self.td_target(reward, next_state, done)

        # Backpropagate loss through Q_online
        loss = self.update_Q_online(td_est, td_tgt)

        return (td_est.mean().item(), loss)