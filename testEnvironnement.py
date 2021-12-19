from itertools import count
import torch
import torch.optim as optim

from src.python.constants import N
from src.python.RL.SudokuEnv import SudokuEnv
from src.python.RL.SudokuAgent import SudokuAgent
from src.python.RL.agentUtils import ReplayMemory, select_action, plot_durations, optimize_model
from src.python.RL.SudokuPlayer import SudokuPlayer
# check https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html

BATCH_SIZE = 128
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 200
TARGET_UPDATE = 10
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

rootEx = "Files/exercices/"
rootSol = "Files/solutions/"
rootCheckpoints = "checkpoints/"

player = SudokuPlayer(N, rootEx, rootSol, rootCheckpoints)

episodes = 3

for e in range(episodes):
    print("Episode : ", e)
    state = player.reset()
    while True:

        action = player.act(state)



# select_action(policy_net, n_actions, device, state, steps_done)
# plot_durations(episode_durations)
# optimize_model(memory, policy_net, target_net, optimizer, device=DEVICE, batch_size=BATCH_SIZE, gamma=GAMMA)



# obs = env.reset()
# for i in range(5):
#   action = env.action_space.sample()
#   action_bis = agent(obs)
#   print(action_bis)
#   obs, rewards, done, info = env.step(action)
#   print(action)
#   print(rewards)
#   print(done)
#   env.render()