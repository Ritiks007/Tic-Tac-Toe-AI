import pygame
from Environment import Environment

Env = Environment()
Env.create_game()

while Env.running:
    Env.update()
for event in pygame.event.get():
	if(event.type == pygame.quit):
		pygame.quit()