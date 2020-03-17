#TIC TAC TOE Environment

import pygame

surface=pygame.display.set_mode((800,600))
pygame.display.set_caption("tic tac toe")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    surface.fill([255,255,255])
    
    pygame.display.flip()
pygame.quit()