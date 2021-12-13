import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.nn.functional as F

from src.python.constants import N

# check https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html


class SudokuAgent(nn.Module):
    def __init__(self, input_shape=N, n_channels=1, n_actions=3):
        super(SudokuAgent, self).__init__()

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.n_actions = n_actions
        self.input_shape = input_shape
        self.n_channels = n_channels
        

        self.lin1 = nn.Linear(input_shape**2, input_shape**2)
        self.lin2 = nn.Linear(input_shape**2, input_shape**2)
        self.head = nn.Linear(input_shape**2, n_actions)

    # Called with either one element to determine next action, or a batch
    # during optimization. Returns tensor([[left0exp,right0exp]...]).
    def forward(self, x):
        print(x.flatten().shape)
        x = torch.from_numpy(x.flatten()).type(torch.float32).to(self.device)
        x = F.relu(self.lin1(x))
        x = F.relu(self.lin2(x))
        return self.head(x)


