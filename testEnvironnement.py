import torch
import torch.optim as optim

from src.python.constants import N
from src.python.SudokuEnv import SudokuEnv
from src.python.SudokuAgent import SudokuAgent
from src.python.agentUtils import ReplayMemory, select_action, plot_durations, optimize_model

# check https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html

BATCH_SIZE = 128
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 200
TARGET_UPDATE = 10

rootEx = "Files/exercices/"
rootSol = "Files/solutions/"

env = SudokuEnv(N, rootEx, rootSol)
n_actions = env.action_space.n


policy_net = SudokuAgent()
target_net = SudokuAgent()
target_net.load_state_dict(policy_net.state_dict())
target_net.eval()
optimizer = optim.RMSprop(policy_net.parameters())
memory = ReplayMemory(10000)


obs = env.reset()
for i in range(5):
  action = env.action_space.sample()
  action_bis = agent(obs)
  print(action_bis)
  obs, rewards, done, info = env.step(action)
  print(action)
  print(rewards)
  print(done)
  env.render()