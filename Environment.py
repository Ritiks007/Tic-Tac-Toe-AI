#TIC TAC TOE Environment
import pygame
from params import Size
from GridLines import Grid
from Player import Cross
surface = pygame.display.set_mode((Size+200,Size))
pygame.display.set_caption("tic tac toe")


grid = Grid()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    surface.fill([255,255,255])
    
    grid.draw(surface)
    cross=Cross(0,0)
    cross.draw(surface)
    pygame.display.flip()
pygame.quit()
