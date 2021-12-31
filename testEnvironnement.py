from itertools import count
import numpy as np
import torch
import torch.optim as optim
from pathlib import Path
from tqdm import trange

from src.python.constants import N
from src.python.RL.SudokuEnv import SudokuEnv
from src.python.RL.SudokuAgent import SudokuAgent
from src.python.RL.agentUtils import ReplayMemory, select_action, plot_durations, optimize_model
from src.python.RL.SudokuPlayer import SudokuPlayer
from src.python.RL.MetricLogger import MetricLogger
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
rootCheckpoints = Path("checkpoints/")

player = SudokuPlayer(N, rootEx, rootSol, rootCheckpoints)
logger = MetricLogger(rootCheckpoints)

episodes = 1000

for e in trange(episodes):
    # print("Episode : ", e)
    state = player.reset()
    initial_state = np.copy(state)
    solution = player.currentSol
    while True:
        action = player.act(state)

        # Agent performs action
        next_state, reward, done, info = player.step(action, verbose=True)

        # Remember
        # print(type(state),type(action), type(next_state))
        player.cache(state, action, next_state, reward, done)

        # Learn
        q, loss = player.learn()

        # Logging
        logger.log_step(reward, loss, q)

        # Update state
        state = next_state

        # Check if end of game
        if done:
            break

    logger.log_episode()

    if e % 10 == 0:
        logger.record(episode=e, epsilon=player.exploration_rate, step=player.curr_step)


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