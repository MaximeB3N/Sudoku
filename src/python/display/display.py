import pygame
from src.python.constants import BLOCKSIZE, COLOR_DARK_GENERATOR, WIDTH

def inside_rect(mouse, posX, posY, width, height):
    if posX <= mouse[0] <= posX + width and posY <= mouse[1] <= posY + height:
        return True
    else:
        return False

def display_button(screen, text, color_light, color_dark, margin, posX, posY, width, height, mouse):
    if posX <= mouse[0] <= posX + width and posY <= mouse[1] <= posY + height:
        pygame.draw.rect(screen, color_light, [posX, posY, width, height])
        # superimposing the text onto our button
        screen.blit(text, (posX + margin[0], posY + margin[1]))
    else:
        pygame.draw.rect(screen, color_dark, [posX, posY, width, height])
        # superimposing the text onto our button
        screen.blit(text, (posX + margin[0], posY + margin[1]))




def display_grid(screen, grid, blockSize, width, height, color, font, margin_text):
    
    for i, x in enumerate(range(width[0], width[1], blockSize)):
        for j, y in enumerate(range(height[0], height[1], blockSize)):
            if i<=8 and j<=8:
                pygame.draw.rect(screen, COLOR_DARK_GENERATOR, [x, y, BLOCKSIZE, BLOCKSIZE])
                text_block = font.render(f"{int(grid[i][j])}" , True , color)
                screen.blit(text_block, (x + margin_text[0], y + margin_text[1]))

            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, color, rect, 1)