import os
import gym
import numpy as np
from gym import error, spaces, utils
from gym.utils import seeding
import pathlib

from src.python.grid import load_grids, finished, valid


class SudokuEnv(gym.Env):
    def __init__(self, N, rootEx, rootSol):
        super(SudokuEnv, self).__init__()

        self.N = N
        self.pathsEx = [pathlib.Path(rootEx, nameEx) for nameEx in os.listdir(rootEx)]
        self.pathsSol = [pathlib.Path(rootSol, nameSol) for nameSol in os.listdir(rootSol)]
        
        self.lenExperiences = len(self.pathsEx)
        self.pointer = np.random.randint(0, self.lenExperiences)
        
        self.currentEx, self.currentSol = load_grids(self.pathsEx[self.pointer], self.pathsSol[self.pointer])

        self.initial_state = np.copy(self.currentEx)

        self.action_space = spaces.Box(low=np.array([0, 0, 1]), high=np.array([N-1, N-1, N]), dtype=np.int32)

        self.observation_space = spaces.Box(low=1, high=N, shape=(N,N), dtype=np.int32)

    def step(self, action):
        assert self.action_space.contains(action)

        reward = 0
        done = False
        i, j, value = action[0], action[1], action[2]

        curr = self.currentEx.squeeze()
        sol = self.currentSol.squeeze()

        if curr[i,j] != 0:
            reward += -1

        elif sol[i,j] != value:
            reward += -1

        else:
            reward +=3

        curr[i,j] = value

        if valid(curr.squeeze(), i, j):
            reward+=1

        else:
            reward+= -1

        if finished(curr.squeeze()):
            reward += np.sum(curr==sol) - self.N**2
            done = True
            self.pointer = (self.pointer + 1) % self.lenExperiences
            self.currentEx, self.currentSol = load_grids(self.pathsEx[self.pointer], self.pathsSol[self.pointer])
            self.initial_state = np.copy(self.currentEx)

        return self.currentEx, reward, done, {}

    def reset(self):

        self.pointer = np.random.randint(0, self.lenExperiences)
        self.currentEx, self.currentSol = load_grids(self.pathsEx[self.pointer], self.pathsSol[self.pointer])
        self.initial_state = np.copy(self.currentEx)
        return self.currentEx
        
    def render(self, mode='human'):

        print("-"*20+"Initial State"+"-"*20)
        print(self.initial_state.squeeze())
        print("-"*20+"Current state"+"-"*20)
        print(self.currentEx.squeeze())
        print("-"*20+"Current solution"+"-"*20)
        print(self.currentSol.squeeze())