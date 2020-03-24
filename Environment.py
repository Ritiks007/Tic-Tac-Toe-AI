#TIC TAC TOE Environment
import pygame
from params import Size, Cell_Size, N
from GridLines import Grid 
from Player import Player

class Environment:
    def __init__(self):
        self.grid = Grid()
        self.running = False
        self.vs_human = True
        self.vs_computer = False
        self.player = Player()
        self.turn = 0
        self.surface = pygame.display.set_mode((Size+200,Size))
        pygame.display.set_caption("tic tac toe")
        self.gameover = False
    
    def create_game(self):
        self.surface.fill([255,255,255])
        self.grid.draw(self.surface)
        # self.display_start_menu(self.surface)
        pygame.display.flip()

	def display_running_game(self):

		if(self.turn == 1):
			self.player_name = self.player.player1_name
		else:
			self.player_name = self.player.player2_name

		turn = font.render(self.player_name + "'s Turn", 1, (255,0,0))
		surface.blit(turn, (Cell_Size*(N+0.5), 100))

		player_1 = font.render(player1_name + " is ", 1, (250, 0, 0))
		surface.blit(player_1, (Cell_Size*(N+0.5), 150))

		player_2 = font.render(player2_name + " is ", 1, (250, 0, 0))
		surface.blit(player_2, (Cell_Size*(N+0.5), 200))

		restart = font.render("restart", 1, (250,0,0))
		surface.blit(restart, (Cell_Size*(N + 0.5), 500))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.gameover = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # [x, y] = pos//Cell_Size
                x = pos[0]//Cell_Size
                y = pos[1]//Cell_Size
                if(x<N and y<N and self.grid.check(x,y) == -1):
                    self.player.move(self.turn, x, y)
                    self.grid.update(x,y,self.turn) 
                    result = self.grid.checkwin(x, y, self.turn) 
                    if(result==1 or result==2):
                        print("Player {} won".format(self.turn+1))
                        self.gameover = True
                    elif(result==3):
                        print("Draw")
                        self.gameover = True
                    print(self.grid.CheckGrid)
                    self.turn = 1 - self.turn

        self.surface.fill([255,255,255])
        self.grid.draw(self.surface)
        # if self.user_details_received == False:  
        #     self.display_user_details()
        # elif self.gameover == True:
        #     self.display_reset()
        if self.user_details_received == True and self.gameover == False:
			self.display_running_game()
        self.player.draw(self.surface)
        pygame.display.flip()
        
    def reset(self):
        self.turn = 0
        self.grid.reset()
        self.player.reset()
        self.gameover = False
