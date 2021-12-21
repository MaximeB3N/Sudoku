import pygame
import sys
import os
import numpy as np
import time

from src.python.display.display import display_button, display_grid, inside_rect, state_modification
from src.python.grid import finished, load_grids
from src.python.constants import (N, WIDTH, HEIGHT,

                                    WHITE, BLACK, GREY,
                                
                                    COLOR_LIGHT_QUIT, COLOR_DARK_QUIT,
                                    WIDTH_QUIT, HEIGHT_QUIT, POS_QUIT_X, POS_QUIT_Y,
                                    TEXT_MARGIN_QUIT,

                                    COLOR_LIGHT_GENERATOR, COLOR_DARK_GENERATOR,
                                    WIDTH_GENERATOR, HEIGHT_GENERATOR, POS_GENERATOR_X, POS_GENERATOR_Y,
                                    TEXT_MARGIN_GENERATOR,

                                    BLOCKSIZE, WIDTH_GRID, HEIGHT_GRID,
                                    MARGIN_NUMBER)

from src.python.constants import (WIDTH_REVERSE, HEIGHT_REVERSE, 
                            POS_REVERSE_X, POS_REVERSE_Y, TEXT_MARGIN_REVERSE,

                            WIDTH_FORWARD, HEIGHT_FORWARD,
                            POS_FORWARD_X, POS_FORWARD_Y, TEXT_MARGIN_FORWARD,
                            
                            WIDTH_STATE, HEIGHT_STATE,
                            POS_STATE_X, POS_STATE_Y, TEXT_MARGIN_STATE,

                            WIDTH_HINT, HEIGHT_HINT,
                            POS_HINT_X, POS_HINT_Y, TEXT_MARGIN_HINT,
                            
                            RED_WIN, WIDTH_WIN, HEIGHT_WIN,
                            POS_WIN_X, POS_WIN_Y, TEXT_MARGIN_WIN,
                            
                            )


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

SMALLFONT = pygame.font.SysFont('Corbel',35)

text_quit = SMALLFONT.render('X' , True , WHITE)
text_generator = SMALLFONT.render('Generate Sudoku' , True , WHITE)
text_reverse = SMALLFONT.render('' , True , WHITE)
text_forward = SMALLFONT.render('' , True , WHITE)
text_state = SMALLFONT.render('' , True , WHITE)
text_win = SMALLFONT.render('' , True , RED_WIN)

## Defining the path to the sudoku file
rootFile = "Files/exercices/"
rootSol = "Files/solutions/"
pathsEx = [rootFile + name for name in os.listdir(rootFile)]
pathsSol = [rootSol + name for name in os.listdir(rootSol)]
pathsEx.sort()
pathsSol.sort()

N_generate = len(pathsEx)

# Defining an unfilled grid
initial_ex = np.zeros((N,N))
ex = np.zeros((N,N))
sol = np.zeros((N,N))

BUFFER = []
pointer_state = -1
box_state = 0
solved = False
while True:
    
    mouse = pygame.mouse.get_pos()
    background = pygame.image.load('Files/display/china.jpeg')
    screen.blit(background, (0,0))
    display_grid(screen, ex, initial_ex, BLOCKSIZE, WIDTH_GRID, HEIGHT_GRID, GREY, BLACK, SMALLFONT, MARGIN_NUMBER)

    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT:
            pygame.quit()
        

        if ev.type == pygame.KEYDOWN:
            if state_modification(ev)!=-1:
                box_state = state_modification(ev)
                if box_state == 0:
                    text_state = SMALLFONT.render('', True , WHITE)

                else:
                    text_state = SMALLFONT.render(str(box_state) , True , WHITE)
            
            

        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
              
            # checks if the quit button is clicked
            # then closes the game
            if inside_rect(mouse, POS_QUIT_X, POS_QUIT_Y, WIDTH_QUIT, HEIGHT_QUIT):
                pygame.quit()

            elif inside_rect(mouse, WIDTH_GRID[0], HEIGHT_GRID[0], N*BLOCKSIZE, N*BLOCKSIZE):
                i, j = int( (mouse[0]-WIDTH_GRID[0])/BLOCKSIZE), int( (mouse[1] - HEIGHT_GRID[0])/BLOCKSIZE)
                print(i,j)
                if i<0 or j<0 or i>=N or j>=N:
                    continue

                # Reverse i and j to have the same convention as in the grid
                elif initial_ex[j][i] == 0 and not solved:
                    if box_state != 0:
                        # Reverse i and j to have the same convention as in the grid
                        ex[j][i] = box_state

                        # Update the buffer
                        for _ in range(len(BUFFER) - pointer_state - 1):
                            BUFFER.pop()
                        
                        BUFFER.append((i,j,box_state))
                        pointer_state+=1
                        box_state = 0
                        text_state = SMALLFONT.render('', True , WHITE)

                        if np.all(ex == sol):
                            text_win = SMALLFONT.render('You won !', True , RED_WIN)
                            solved = True
                        
                        elif not np.all(ex == sol) and finished(ex):
                            text_win = SMALLFONT.render('You lost !', True , RED_WIN)
                            solved = True


            # checks if the generator button is clicked
            # then generates a new sudoku
            elif inside_rect(mouse, POS_GENERATOR_X, POS_GENERATOR_Y, WIDTH_GENERATOR, HEIGHT_GENERATOR):
                print('Generator')
                i = np.random.randint(0, N_generate)
                pathEx, pathSol = pathsEx[i], pathsSol[i]
                ex, sol = load_grids(pathEx, pathSol, unsqueeze=False)
                solved = False
                initial_ex = np.copy(ex)
            
            # checks if the reverse button is clicked
            # then play th the sudoku
            elif inside_rect(mouse, POS_REVERSE_X, POS_REVERSE_Y, WIDTH_REVERSE, HEIGHT_REVERSE):
                if len(BUFFER)>0:
                    i, j, _ = BUFFER[pointer_state]
                    # It needs to be reversed because the grid is reversed
                    ex[j,i] = 0
                    pointer_state -= 1

            elif inside_rect(mouse, POS_FORWARD_X, POS_FORWARD_Y, WIDTH_FORWARD, HEIGHT_FORWARD):
                if pointer_state != len(BUFFER)-1:
                    pointer_state += 1
                    i, j, value = BUFFER[pointer_state]
                    ex[j,i] = value
            
            elif inside_rect(mouse, POS_HINT_X, POS_HINT_Y, WIDTH_HINT, HEIGHT_HINT):
                if not solved:
                    i, j = np.argwhere(ex == 0)[np.random.randint(0,len(np.argwhere(ex==0)))]
                    ex[i,j] = sol[i,j]
                    BUFFER.append((i,j,ex[i,j]))
                    if np.all(ex == sol):
                        text_win = SMALLFONT.render('You won !', True , RED_WIN)
                        solved = True

                    elif not np.all(ex == sol) and finished(ex):
                        text_win = SMALLFONT.render('You lost !', True , RED_WIN)
                        solved = True
            



    # Displaying the quit button 
    display_button(screen, text_quit, COLOR_LIGHT_QUIT, COLOR_DARK_QUIT,
                    TEXT_MARGIN_QUIT, POS_QUIT_X, POS_QUIT_Y, 
                    WIDTH_QUIT, HEIGHT_QUIT, mouse)
    
    # Display the Generator button
    display_button(screen, text_generator, COLOR_LIGHT_GENERATOR, 
                COLOR_DARK_GENERATOR, TEXT_MARGIN_GENERATOR, POS_GENERATOR_X, 
                POS_GENERATOR_Y, WIDTH_GENERATOR, HEIGHT_GENERATOR, mouse)

    # Display the Reverse button
    display_button(screen, text_reverse,
                    COLOR_LIGHT_GENERATOR,COLOR_DARK_GENERATOR, TEXT_MARGIN_REVERSE,
                    POS_REVERSE_X, POS_REVERSE_Y, WIDTH_REVERSE, HEIGHT_REVERSE, mouse)

    backward = pygame.image.load('Files/display/backward.png')
    screen.blit(backward, (POS_REVERSE_X,POS_REVERSE_Y))

    # Display the Forward button
    display_button(screen, text_forward, COLOR_LIGHT_GENERATOR, COLOR_DARK_GENERATOR,
                    TEXT_MARGIN_FORWARD, POS_FORWARD_X, POS_FORWARD_Y, 
                    WIDTH_FORWARD, HEIGHT_FORWARD, mouse)

    forward = pygame.image.load('Files/display/forward.png')
    screen.blit(forward, (POS_FORWARD_X,POS_FORWARD_Y))

    # Display the current state
    display_button(screen, text_state, COLOR_DARK_GENERATOR, COLOR_DARK_GENERATOR,
                    TEXT_MARGIN_STATE, POS_STATE_X, POS_STATE_Y,
                    WIDTH_STATE, HEIGHT_STATE, mouse)

    # Display the hint state
    display_button(screen, None, COLOR_LIGHT_GENERATOR, COLOR_DARK_GENERATOR,
                    TEXT_MARGIN_HINT, POS_HINT_X, POS_HINT_Y,
                    WIDTH_HINT, HEIGHT_HINT, mouse)

    hint = pygame.image.load('Files/display/ampoule.png')
    screen.blit(hint, (POS_HINT_X,POS_HINT_Y))

    if solved:
        # Display the win display
        display_button(screen, None, BLACK, BLACK,
                        TEXT_MARGIN_WIN, POS_WIN_X-5, POS_WIN_Y-5,
                        WIDTH_WIN+10, HEIGHT_WIN+10, mouse)

        display_button(screen, text_win, COLOR_LIGHT_GENERATOR, COLOR_LIGHT_GENERATOR,
                        TEXT_MARGIN_WIN, POS_WIN_X, POS_WIN_Y,
                    WIDTH_WIN, HEIGHT_WIN, mouse)

    # updates the frames of the game
    pygame.display.update()

