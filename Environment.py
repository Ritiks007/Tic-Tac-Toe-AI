#TIC TAC TOE Environment
import pygame
from params import Size, Cell_Size, N
from GridLines import Grid
from Player import Player

class Environment:
    def __init__(self):
        self.grid = Grid()
        self.running = True
        self.player = Player()
        self.turn = 0
        self.surface = pygame.display.set_mode((Size+200,Size))
        pygame.display.set_caption("tic tac toe")
    
    def create_game(self):
        self.surface.fill([255,255,255])
        self.grid.draw(self.surface)        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # [x, y] = pos//Cell_Size
                x = pos[0]//Cell_Size
                y = pos[1]//Cell_Size
                if(x<N and y<N and self.grid.check(x,y)):
                    self.player.move(self.turn, x, y)
                    self.grid.update(x,y)
                    print(self.grid.CheckGrid)
                    self.turn = 1 - self.turn
                    
        self.surface.fill([255,255,255])
        self.grid.draw(self.surface)
        self.player.draw(self.surface)
        pygame.display.flip()