import pygame
pygame.init()
from Environment import Environment

Env = Environment()
clock = pygame.time.Clock()

while Env.quit == False:
	if Env.running == False:
		Env.create_game()
	elif Env.vs_human:
		Env.update()
		# clock.tick(30)
	elif Env.vs_computer:
		Env.update()
		# clock.tick(30)	
pygame.quit()