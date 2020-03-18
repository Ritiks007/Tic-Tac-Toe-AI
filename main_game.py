import pygame
from Environment import Environment

Env = Environment()
Env.create_game()

while Env.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Env.running = False
    Env.update()
pygame.quit()