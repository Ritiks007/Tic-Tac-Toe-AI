import pygame
pygame.init()
from Environment import Environment

Env = Environment()
Env.create_game()

while Env.running:
	while Env.gameover == False:
		Env.update()
	Env.reset()
pygame.quit()
