#TIC TAC TOE Environment
import pygame
from params import Size, Cell_Size, N
from GridLines import Grid
from Player import Cross,Circle
surface = pygame.display.set_mode((Size+200,Size))
pygame.display.set_caption("tic tac toe")


grid = Grid()
crosses = []
circles = []
running = True
turn_player_1 = True
turn_player_2 = False    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # [x, y] = pos//Cell_Size
            x = pos[0]//Cell_Size
            y = pos[1]//Cell_Size
            if(x<N and y<N):
	            if(turn_player_1):
	                cross = Cross(x,y)
            if(x<N and y<N and grid.check(x,y)):
	            if(turn_player_1):
	            	cross = Cross(x,y)
	                crosses.append(cross)
	            if(turn_player_2):
	                circle = Circle(x,y)
	                circles.append(circle)
            	grid.update(x,y)
	            turn_player_1 = not turn_player_1
	            turn_player_2 = not turn_player_2
            
    surface.fill([255,255,255])

    # get the cell on which mouse clicked in x and y

    grid.draw(surface)
    for c in crosses:
        c.draw(surface)
    for ci in circles:
        ci.draw(surface)

    pygame.display.flip()
pygame.quit()