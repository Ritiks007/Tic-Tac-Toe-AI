import pygame
pygame.init()
from Environment import Environment

Env = Environment()

while not Env.running:
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
pygame.quit()