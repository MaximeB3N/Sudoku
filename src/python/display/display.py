import pygame
import numpy as np

from src.python.constants import N, BLOCKSIZE, COLOR_GRID

def inside_rect(mouse, posX, posY, width, height):
    if posX <= mouse[0] <= posX + width and posY <= mouse[1] <= posY + height:
        return True
    else:
        return False

def display_button(screen, text, color_light, color_dark, margin, posX, posY, width, height, mouse):
    if posX <= mouse[0] <= posX + width and posY <= mouse[1] <= posY + height:
        pygame.draw.rect(screen, color_light, [posX, posY, width, height])
        # superimposing the text onto our button
        if not text is None:
            screen.blit(text, (posX + margin[0], posY + margin[1]))
    else:
        pygame.draw.rect(screen, color_dark, [posX, posY, width, height])
        # superimposing the text onto our button
        if not text is None:
            screen.blit(text, (posX + margin[0], posY + margin[1]))




def display_grid(screen, grid, initial_grid, blockSize, width, height, color_modified, color_unmodified, font, margin_text):
    
    for j, x in enumerate(range(width[0], width[1], blockSize)):
        for i, y in enumerate(range(height[0], height[1], blockSize)):
            if i<=8 and j<=8:
                pygame.draw.rect(screen, COLOR_GRID, [x, y, BLOCKSIZE, BLOCKSIZE])
                if initial_grid[i][j] != 0:
                    text_block = font.render(f"{int(grid[i][j])}" , True , color_unmodified)
                    screen.blit(text_block, (x + margin_text[0], y + margin_text[1]))
                
                else:
                    if grid[i][j] != 0:
                        text_block = font.render(f"{int(grid[i][j])}" , True , color_modified)
                        screen.blit(text_block, (x + margin_text[0], y + margin_text[1]))

            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, color_unmodified, rect, 1)

    k = int(np.sqrt(N))
    for x in range(width[0], width[1], k*blockSize):
        for y in range(height[0], height[1], k*blockSize):
            rect = pygame.Rect(x, y, k*blockSize, k*blockSize)
            pygame.draw.rect(screen, color_unmodified, rect, 4)


def state_modification(ev):
    box_state = -1
    if ev.key == pygame.K_ESCAPE:
        box_state = 0
    if ev.key == pygame.K_1:
        box_state = 1
    if ev.key == pygame.K_2:
        box_state = 2
    if ev.key == pygame.K_3:
        box_state = 3
    if ev.key == pygame.K_4:
        box_state = 4
    if ev.key == pygame.K_5:
        box_state = 5
    if ev.key == pygame.K_6:
        box_state = 6
    if ev.key == pygame.K_7:
        box_state = 7
    if ev.key == pygame.K_8:
        box_state = 8
    if ev.key == pygame.K_9:
        box_state = 9

    return box_state