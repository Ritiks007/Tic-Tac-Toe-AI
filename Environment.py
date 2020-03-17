#TIC TAC TOE Environment
from GridLines import Grid
import pygame
Size = 600
N = 5
Game_Window = [Size + 150 ,Size]
Cell_Size = Game_Window[1]//N
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
    pygame.display.flip()
pygame.quit()
