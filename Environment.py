#TIC TAC TOE Environment
import pygame
from params import Size, Cell_Size, N, font, smaller_font, even_smaller_font
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
        self.user_details_received = False
        self.surface = pygame.display.set_mode((Size+200,Size))
        pygame.display.set_caption("tic tac toe")
        self.gameover = False
    
    def create_game(self):
        self.surface.fill([255,255,255])
        self.grid.draw(self.surface)
        self.display_start_menu(self.surface)
        pygame.display.flip()

    def update(self):
        self.surface.fill([255,255,255])
        self.grid.draw(self.surface)
        if self.user_details_received == False:  
            self.display_user_details(self.surface)
        else:
            self.display_running_game()
        # elif self.gameover == True:
        #     self.display_reset(result)
        if self.user_details_received == True:
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
            self.player.draw(self.surface)

        pygame.display.flip()

    def reset(self):
        self.running = True
        self.gameover = False
        self.vs_human = False
        self.vs_computer = False
        self.user_details_received = False
        self.turn = 0
        self.grid.reset()
        self.player.reset()
        self.surface.fill([255,255,255])
        self.grid.draw(self.surface)
        self.display_start_menu(self.surface)
        pygame.display.flip()
    
    # Side Pannel Functions

    def display_running_game(self):
        if self.turn == 1 :
            player_name = self.player.player1_name
        else:
            player_name = self.player.player2_name
        player1_name = self.player.player1_name
        player2_name = self.player.player2_name
        turn = font.render(player_name + "'s Turn", 1, (255,0,0))
        self.surface.blit(turn, (Cell_Size*(N+0.5), 100))
        player_1 = font.render(player1_name + " is ", 1, (250, 0, 0))
        self.surface.blit(player_1, (Cell_Size*(N+0.5), 150))
        player_2 = font.render(player2_name + " is ", 1, (250, 0, 0))
        self.surface.blit(player_2, (Cell_Size*(N+0.5), 200))
        restart = font.render("restart", 1, (250,0,0))
        self.surface.blit(restart, (Cell_Size*(N + 0.5), 500))

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
                
    def display_user_details(self,surface):
        
        input_boxes = [self.player.input_box1, self.player.input_box2]
        details_1 = smaller_font.render('Player 1',1,(0,0,0))
        details_2 = smaller_font.render('Player 2',1,(0,0,0))
        name_txt = even_smaller_font.render('Name : ',1,(0,0,0))
        confirm_txt = smaller_font.render('Play',1,(0,0,0))
        choose_txt = even_smaller_font.render('Choose :',1,(0,0,0))
        check_box1 = even_smaller_font.render('X',1,(0,0,0))
        check_box2 = even_smaller_font.render('O',1,(0,0,0))
        surface.blit(details_1,(Cell_Size*(N+0.5), 120))
        surface.blit(name_txt,(Cell_Size*(N+0.1), 160))
        surface.blit(choose_txt,(Cell_Size*(N+0.1), 200))
        surface.blit(check_box1,(Cell_Size*(N+1), 200))
        surface.blit(check_box2,(Cell_Size*(N+1.3), 200))

        surface.blit(details_2,(Cell_Size*(N+0.5), 270))
        surface.blit(name_txt,(Cell_Size*(N+0.1), 310))

        surface.blit(confirm_txt,(Cell_Size*(N+0.6), 380))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.gameover = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                # print('{},{}'.format(x,y))
                if x>=665 and x<=722 and y>=378 and y<=405:
                    self.user_details_received = True
            for i,box in enumerate(input_boxes):
                player_name_received = box.handle_event(event)
                if i == 0:
                    self.player.player1_name = player_name_received
                else:
                    self.player.player2_name = player_name_received
        
        # print('{} , {}'.format(self.player.player1_name,self.player.player2_name))
            
        for box in input_boxes:
            box.update()
            box.draw(self.surface)