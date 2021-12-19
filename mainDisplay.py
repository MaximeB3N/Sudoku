import pygame
import sys
import os
import numpy as np
import time

from src.python.display.display import display_button, display_grid, inside_rect
from src.python.grid import load_grids
from src.python.constants import (N, WIDTH, HEIGHT, 
                                    WHITE, BLACK,
                                    COLOR_LIGHT_QUIT, COLOR_DARK_QUIT,
                                    WIDTH_QUIT, HEIGHT_QUIT, POS_QUIT_X, POS_QUIT_Y,
                                    TEXT_MARGIN_QUIT,
                                    COLOR_LIGHT_GENERATOR, COLOR_DARK_GENERATOR,
                                    WIDTH_GENERATOR, HEIGHT_GENERATOR, POS_GENERATOR_X, POS_GENERATOR_Y,
                                    TEXT_MARGIN_GENERATOR,
                                    BLOCKSIZE, WIDTH_GRID, HEIGHT_GRID,
                                    MARGIN_NUMBER)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

SMALLFONT = pygame.font.SysFont('Corbel',35)

text_quit = SMALLFONT.render('X' , True , WHITE)
text_generator = SMALLFONT.render('Generate Sudoku' , True , WHITE)


## Defining the path to the sudoku file
rootFile = "Files/exercices/"
rootSol = "Files/solutions/"
pathsEx = [rootFile + name for name in os.listdir(rootFile)]
pathsSol = [rootSol + name for name in os.listdir(rootSol)]
N_generate = len(pathsEx)
ex = None
sol = None
# Defining an unfilled grid
ex = np.ones((N,N))*(-1)

while True:
    
    mouse = pygame.mouse.get_pos()

    display_grid(screen, ex, BLOCKSIZE, WIDTH_GRID, HEIGHT_GRID, BLACK, SMALLFONT, MARGIN_NUMBER)

    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
              
            # checks if the quit button is clicked
            # then closes the game
            if inside_rect(mouse, POS_QUIT_X, POS_QUIT_Y, WIDTH_QUIT, HEIGHT_QUIT):
                pygame.quit()

            # checks if the generator button is clicked
            # then generates a new sudoku
            elif inside_rect(mouse, POS_GENERATOR_X, POS_GENERATOR_Y, WIDTH_GENERATOR, HEIGHT_GENERATOR):
                print('Generator')
                i = np.random.randint(0, N_generate)
                pathEx, pathSol = pathsEx[i], pathsSol[i]
                ex, sol = load_grids(pathEx, pathSol, unsqueeze=False)
                print(ex) 

            elif inside_rect(mouse, WIDTH_GRID[0], HEIGHT_GRID[0], N*BLOCKSIZE, N*BLOCKSIZE):
                i, j = int(mouse[0]/BLOCKSIZE - WIDTH_GRID[0]), int(mouse[1]/BLOCKSIZE-HEIGHT_GRID[0])
                print(i,j)
                if i<0 or j<0 or i>=N or j>=N:
                    continue


    # Displaying the quit button 
    display_button(screen, text_quit, COLOR_LIGHT_QUIT, COLOR_DARK_QUIT,
                    TEXT_MARGIN_QUIT, POS_QUIT_X, POS_QUIT_Y, 
                    WIDTH_QUIT, HEIGHT_QUIT, mouse)
    
    # Display the Generator button
    display_button(screen, text_generator, COLOR_LIGHT_GENERATOR, 
                COLOR_DARK_GENERATOR, TEXT_MARGIN_GENERATOR, POS_GENERATOR_X, 
                POS_GENERATOR_Y, WIDTH_GENERATOR, HEIGHT_GENERATOR, mouse)


    # updates the frames of the game
    pygame.display.update()

