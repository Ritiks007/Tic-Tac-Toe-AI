#TIC TAC TOE Environment
import pygame
from params import Size, Cell_Size, N, font, smaller_font, even_smaller_font
from GridLines import Grid 
from Player import Player

class Environment:
    def __init__(self):
        self.grid = Grid()
        self.running = False
        self.quit = False
        self.vs_human = False
        self.vs_computer = False
        self.player = Player()
        self.turn = 0
        self.user_details_received = False
        self.surface = pygame.display.set_mode((Size+200,Size))
        pygame.display.set_caption("tic tac toe")
        self.gameover = False
        self.result = 0
    
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
        elif self.gameover == True:
            self.display_reset()
        else:
            self.display_running_game()

        pygame.display.flip()

    def reset(self):
        self.quit = False
        self.running = True
        self.gameover = False
        self.vs_human = False
        self.vs_computer = False
        self.user_details_received = False
        self.turn = 0
        self.result = 0
        self.grid.reset()
        self.player.reset()
    
    # Side Pannel Functions

    def display_running_game(self):
        
        if self.player.player_cross == 0:
            player1_symbol = 'Cross'
            player2_symbol = 'Circle'
        else:
            player1_symbol = 'Circle'
            player2_symbol = 'Cross'
            
        player1_name = self.player.player1_name
        player2_name = self.player.player2_name

        if self.turn == 0 :
            player_name = self.player.player1_name
        else:
            player_name = self.player.player2_name
        # display of Player's Turn
        if(self.turn == 1):
            turn = smaller_font.render(player_name + "'s Turn", 1, (235,117,117))
        else:
            turn = smaller_font.render(player_name + "'s Turn", 1, (130,114,195))
        self.surface.blit(turn, (Cell_Size*(N+0.4), 150))

        # display of Players Symbols
        player_1 = smaller_font.render(player1_name + " is " + player1_symbol, 1, (130,114,195))
        self.surface.blit(player_1, (Cell_Size*(N+0.3), 250))

        player_2 = smaller_font.render(player2_name + " is " + player2_symbol, 1, (235,117,117))
        self.surface.blit(player_2, (Cell_Size*(N+0.3), 300))

        # working of game and display and working of restart button 
        reset = font.render("Reset", 1, (122, 24, 70))
        self.surface.blit(reset, (Cell_Size*(N + 0.6), 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.gameover = True
                self.quit = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # [x, y] = pos//Cell_Size
                x = pos[0]//Cell_Size
                y = pos[1]//Cell_Size
                print('{},{}'.format(x,y))
                if(x<N and y<N and self.grid.check(x,y) == -1):
                    self.player.move(self.turn, x, y)
                    self.grid.update(x,y,self.turn) 
                    self.result = self.grid.checkwin(x, y, self.turn) 
                    if(self.result==1 or self.result==2):
                        print("Player {} won".format(self.result))
                        self.gameover = True
                    elif(self.result==3):
                        print("Draw")
                        self.gameover = True
                    print(self.grid.CheckGrid)
                    self.turn = 1 - self.turn
                x = pos[0]
                y = pos[1]
                if x>= 620 and x <= 760 and y <= 550 and y >= 450:
                    self.reset()
                    self.running = False
        self.player.draw(self.surface)

    def display_start_menu(self,surface):

        mode1 = smaller_font.render('Vs Human',1,(88, 95, 193))
        mode2 = smaller_font.render('Vs AI',1,(88, 95, 193))
        choose = font.render('Select Mode',1,(122, 24, 70))
        surface.blit(choose,(Cell_Size*(N+0.3)+5, 180))
        surface.blit(mode1, (Cell_Size*(N+0.4)+10, 260))
        surface.blit(mode2, (Cell_Size*(N+0.4)+30, 310))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.gameover = True
                self.quit = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                print(x,y)
                if x>=650 and x<=745 and y>=253 and y<=280:
                    self.vs_human = True
                    self.running = True
                    self.gameover = False
                elif x>=670 and x<=725 and y>=302 and y<=330:
                    self.vs_computer = True
                    print('here')
                    self.running = True
                    self.gameover = False
                
    def display_user_details(self,surface):
        if self.vs_human:
            input_boxes = [self.player.input_box1, self.player.input_box2]
        else:
            input_boxes = [self.player.input_box1]
        details_1 = smaller_font.render('Player 1',1,(122, 24, 70))
        
        if self.vs_human:
            details_2 = smaller_font.render('Player 2',1,(122, 24, 70))
        
        name_txt = even_smaller_font.render('Name : ',1,(122, 24, 70))
        play_button = smaller_font.render('Play',1,(122, 24, 70))
        choose_txt = even_smaller_font.render('Choose :',1,(122, 24, 70))
        
        check_box1 = smaller_font.render('X',1,(130,114,195))
        check_box2 = smaller_font.render('O',1,(235,117,117))
        
        # PLEASE CHANGE COLOR
        tick = even_smaller_font.render('<-',1,(0,0,0))
        if self.player.player_cross == 0:
            surface.blit(tick,(Cell_Size*(N+1.1), 230))
        else:
            surface.blit(tick,(Cell_Size*(N+1.44), 230))

        surface.blit(details_1,(Cell_Size*(N+0.6), 140))
        surface.blit(name_txt,(Cell_Size*(N+0.1), 190))
        surface.blit(choose_txt,(Cell_Size*(N+0.1), 230))
        surface.blit(check_box1,(Cell_Size*(N+1), 230))
        surface.blit(check_box2,(Cell_Size*(N+1.3), 230))
        
        if self.vs_human:
            surface.blit(details_2,(Cell_Size*(N+0.6), 300))
            surface.blit(name_txt,(Cell_Size*(N+0.1), 340))

        surface.blit(play_button,(Cell_Size*(N+0.7), 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.gameover = True
                self.quit = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                print('{},{}'.format(x,y))
                if x>=720 and x<=730 and y>=227 and y<=245:
                    self.player.player_cross = 0
                elif x>=755 and x<=770 and y>=227 and y<=245:
                    self.player.player_cross = 1
                if x>=665 and x<=722 and y>=450 and y<=480:
                    self.user_details_received = True
            for i,box in enumerate(input_boxes):
                player_name_received = box.handle_event(event)
                if i == 0:
                    self.player.player1_name = player_name_received
                else:
                    self.player.player2_name = player_name_received
                    
        for box in input_boxes:
            box.update()
            box.draw(self.surface)
    
    def display_reset(self):

        if(self.result == 0):
            return
        elif(self.result == 1):
            win = smaller_font.render(self.player.player1_name + ' Won !!', 1, (125,0,125))
        elif(self.result == 2):
            win = smaller_font.render(self.player.player2_name + ' Won !!', 1, (125,0,125))
        else:
            win = even_smaller_font.render('Draw :(', 1, (125,0,125))
        self.surface.blit(win, (Cell_Size*(N+0.4), 280))
            
        restart = font.render("Reset", 1, (122, 24, 70))
        self.surface.blit(restart, (Cell_Size*(N + 0.6), 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.gameover = True
                self.quit = True
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if x>= 620 and x <= 760 and y <= 550 and y >= 450:
                    self.reset()
                    self.running = False
        self.player.draw(self.surface)