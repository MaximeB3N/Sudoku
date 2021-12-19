import pygame
import numpy as np

N = 9

WIDTH, HEIGHT = 800, 600

WHITE = (255,255,255)
BLACK = (0,0,0)
## Defining quit button
# light shade of the button
COLOR_LIGHT_QUIT = (240,0,0)
# dark shade of the button
COLOR_DARK_QUIT = (200,0,0)

# Button quit dimensions
WIDTH_QUIT, HEIGHT_QUIT = 30,30
POS_QUIT_X, POS_QUIT_Y = WIDTH-WIDTH_QUIT-10, 10
TEXT_MARGIN_QUIT = (7,4)

## Defining the generator button
# light shade of the button
COLOR_LIGHT_GENERATOR = (205,220,225)
# dark shade of the button
COLOR_DARK_GENERATOR = (126,127,127)

# Button generator dimensions
WIDTH_GENERATOR, HEIGHT_GENERATOR = 250,40
POS_GENERATOR_X, POS_GENERATOR_Y = WIDTH/2 - WIDTH_GENERATOR/2, HEIGHT - HEIGHT_GENERATOR - 20
TEXT_MARGIN_GENERATOR = (20,8)

## Defining the grid
BLOCKSIZE = 50
WIDTH_GRID = [int(WIDTH/2 - 4.5*BLOCKSIZE), int(4.5*BLOCKSIZE+WIDTH/2)]
HEIGHT_GRID = [ 50, 9*BLOCKSIZE+50] #[int(POS_GENERATOR_X-(N+1)*BLOCKSIZE), int(POS_GENERATOR_Y-BLOCKSIZE)]
MARGIN_NUMBER = (BLOCKSIZE/2-6,BLOCKSIZE/2-10)