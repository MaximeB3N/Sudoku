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

        self.action_space = spaces.Box(low=np.array([0,0,1]), high=np.array([N,N,N+1]), shape=(int(np.sqrt(N)),), dtype=np.int32)

        self.observation_space = spaces.Box(low=1, high=N, shape=(N,N), dtype=np.int32)

    def step(self, action, verbose=False):

        reward = 0
        done = False
        # print(type(action))
        i, j, value = action//81, (action%81)//9, (action%81)%9+1

        # print(self.currentEx.shape)
        curr = self.currentEx.squeeze()
        sol = self.currentSol.squeeze()
        # print(curr.shape)
        # print(i,j)
        # print(curr[i,j])
        empty = True
        if curr[i,j]==0 and sol[i,j] == value:
            reward+=1

        else:
            reward+= -1 
        # if curr[i,j] != 0:
        #     empty = False
        #     reward += -1

        # elif sol[i,j] != value:
        #     reward += -1

        # elif curr[i,j] == 0 and sol[i,j] == value:
        #     reward +=3

        # print(self.currentEx.shape)
        self.currentEx[i,j,0] = value
        curr = self.currentEx.squeeze()
        # print(np.sum(curr==0))
        # if empty and valid(curr.squeeze(), i, j):
        #     reward+=1

        # else:
        #     reward+= -1

        if finished(curr.squeeze()):
            done = True
            
            if verbose:
                self.render()
            #self.pointer = (self.pointer + 1) % self.lenExperiences
            self.currentEx, self.currentSol = load_grids(self.pathsEx[self.pointer], self.pathsSol[self.pointer])
            self.initial_state = np.copy(self.currentEx)

        return self.currentEx, reward, done, {}

    def reset(self):

        #self.pointer = np.random.randint(0, self.lenExperiences)
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
        print("-"*20+"Binary state"+"-"*20)
        print((self.currentSol.squeeze()==self.currentEx.squeeze()).astype(int))
