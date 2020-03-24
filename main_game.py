import pygame
from Environment import Environment

Env = Environment()

while not Env.running:
	Env.create_game()

if Env.vs_human:
	while Env.running:
		# for event in pygame.event.get():
		# 	if(event.type == pygame.QUIT):
		# 		Env.running = False
		Env.update()
if Env.vs_computer:
	while 
pygame.quit()