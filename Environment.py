#TIC TAC TOE Environment
import pygame
from params import Size, Cell_Size, N, font, smaller_font
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
        self.display_start_menu(self.surface)
        pygame.display.flip()

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
        # else:
        #     self.display_running_game()
        self.player.draw(self.surface)
        pygame.display.flip()

    def reset(self):
        self.running = False
        self.gameover = False
        self.vs_human = False
        self.vs_computer = False
        self.player = Player()
        self.turn = 0
        self.grid.reset()
        self.player.reset()
        self.surface.fill([255,255,255])
        self.grid.draw(self.surface)
        self.display_start_menu(self.surface)
        pygame.display.flip()
    
    # Side Pannel Functions
    def display_start_menu(self,surface):

        mode1 = smaller_font.render('Vs Human',1,(0,0,0))
        mode2 = smaller_font.render('Vs AI',1,(0,0,0))
        choose = font.render('Select Mode',1,(0,0,0))
        surface.blit(choose,(Cell_Size*(N+0.2), 180))
        surface.blit(mode1, (Cell_Size*(N+0.3), 260))
        surface.blit(mode2, (Cell_Size*(N+0.3), 310))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.gameover = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # [x, y] = pos//Cell_Size
                x = pos[0]
                y = pos[1]
                # print('{},{}'.format(x,y))
                if x>=620 and x<=760 and y>=250 and y<=295:
                    self.vs_human = True
                    self.running = True
                elif x>=620 and x<=760 and y>=300 and y<=345:
                    self.vs_computer = True
                    self.running = True
                
