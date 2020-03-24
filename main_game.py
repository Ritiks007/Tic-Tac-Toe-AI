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
	if Env.vs_computer:
		while Env.gameover == False:
			Env.update()	
	if Env.running == True:
		Env.reset() 
	clock.tick(30)
pygame.quit()