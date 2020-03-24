import pygame
pygame.init()
from Environment import Environment

Env = Environment()
clock = pygame.time.Clock()
while not Env.running and not Env.gameover:
	Env.create_game()

while Env.running:
	if Env.vs_human:
		while Env.gameover == False:
			Env.update()
			# clock.tick(30)
	if Env.vs_computer:
		while Env.gameover == False:
			Env.update()
			# clock.tick(30)	
	if Env.running == True:
		Env.reset() 
pygame.quit()