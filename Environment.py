#TIC TAC TOE Environment
import pygame
import params
import Players
import GridLines
from params import Size,Cell_Size,N, font, smaller_font, even_smaller_font, cross_color, circle_color, overall_color, background
from GridLines import Grid 
from Players import Player
from model_train import AI,get_hash

class Environment:

    def __init__(self):
        self.grid = Grid()
        self.running = False
        self.quit = False
        self.vs_human = False
        self.vs_computer = False
        self.learning = False
        self.turn_computer = 1
        self.ai = AI(0,2)
        self.ai.load_policy()
        self.player = Player()
        self.turn = 0
        self.user_details_received = False
        self.surface = pygame.display.set_mode((Size+200,Size))
        pygame.display.set_caption("tic tac toe")
        self.gameover = False
        self.result = 0
    
    def create_game(self):
        self.surface.fill(background)
        self.display_start_menu(self.surface)
        self.grid.draw(self.surface)
        pygame.display.flip()

    def update(self):
        self.surface.fill(background)
        if self.user_details_received == False:  
            self.display_user_details(self.surface)
        elif self.gameover == True:
            if self.learning:
                if self.result == self.turn_computer + 1:
                    self.ai.feedReward(1)
                elif self.result == 3:
                    self.ai.feedReward(0.5)
                elif self.result == 2 - self.turn_computer:
                    self.ai.feedReward(-1)
                self.ai.reset()
                self.ai.save_policy(N)
                self.learning = False
            self.display_reset()
        else:
            self.display_running_game()
        self.grid.draw(self.surface)
        pygame.display.flip()

    def reset(self):
        self.quit = False
        self.running = True
        self.gameover = False
        self.vs_human = False
        self.vs_computer = False
        self.learning = False
        self.turn_computer = 1
        self.user_details_received = False
        self.turn = 0
        self.result = 0
        self.ai = AI(0,2)
        self.ai.load_policy()
        self.grid.reset()
        self.player.reset()
    
    # Side Pannel Functions

    def display_running_game(self):

        # Assigning player's symbol and colour
        if self.player.player_cross == 0:
            player1_symbol = 'Cross'
            player2_symbol = 'Circle'
            player1_color = cross_color
            player2_color = circle_color
        else:
            player1_symbol = 'Circle'
            player2_symbol = 'Cross'
            player1_color = circle_color
            player2_color = cross_color

        # local variables of player names
        player1_name = self.player.player1_name
        if self.vs_human:
            player2_name = self.player.player2_name
        else:
            player2_name = "Computer"

        # display of Player's Turn
        if self.turn:
            turn = smaller_font.render(player2_name + "'s Turn", 1, player2_color)
        else:
            turn = smaller_font.render(player1_name + "'s Turn", 1, player1_color)
        self.surface.blit(turn, (Size+(self.surface.get_width()-Size)//2 - turn.get_width()//2, 150))

        # display of Players Symbols
        player_1 = smaller_font.render(player1_name + " is " + player1_symbol, 1, player1_color)
        self.surface.blit(player_1, (Size+(self.surface.get_width()-Size)//2 - player_1.get_width()//2, 250))

        player_2 = smaller_font.render(player2_name + " is " + player2_symbol, 1, player2_color)
        self.surface.blit(player_2, (Size+(self.surface.get_width()-Size)//2 - player_2.get_width()//2, 300))

        # working of game and display and working of reset button 
        reset = font.render("Reset", 1, overall_color)
        self.surface.blit(reset, (672, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.gameover = True
                self.quit = True
                return
            if self.vs_computer and self.turn == self.turn_computer:
                (x,y) = self.ai.choose_action(self.grid.CheckGrid)
                self.player.move(self.turn,x,y)
                self.grid.update(x,y,self.turn)
                if self.learning: 
                    self.ai.add_State(get_hash(self.grid.CheckGrid))
                self.result = self.grid.checkwin(x, y, self.turn) 
                if(self.result==1 or self.result==2):
                    self.gameover = True
                elif(result==3):
                    self.gameover = True
                self.turn = 1 - self.turn
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]//Cell_Size
                y = pos[1]//Cell_Size
                if(x<N and y<N and self.grid.check(x,y) == -1):
                    self.player.move(self.turn, x, y)
                    self.grid.update(x,y,self.turn) 
                    self.result = self.grid.checkwin(x, y, self.turn) 
                    if(self.result==1 or self.result==2):
                        self.gameover = True
                    elif(self.result==3):
                        self.gameover = True
                    self.turn = 1 - self.turn
                x = pos[0]
                y = pos[1]
                if x>= 620 and x <= 760 and y <= 550 and y >= 450:
                    self.reset()
                    self.running = False
        self.player.draw(self.surface)

    def display_start_menu(self,surface):

        # display of mode selection 
        choose = font.render('Select Mode',1,overall_color)
        surface.blit(choose,(641, 180))

        mode1 = smaller_font.render('Vs Human',1,(88, 95, 193))
        surface.blit(mode1, (658, 260))

        mode2 = smaller_font.render('Vs AI',1,(88, 95, 193))
        surface.blit(mode2, (678, 300))

        matrix = smaller_font.render('Game 3x3',1,(88, 95, 193))
        surface.blit(matrix, (658, 350))

        matrix = smaller_font.render('Game 4x4',1,(88, 95, 193))
        surface.blit(matrix, (658, 390))

        matrix = smaller_font.render('Game 5x5',1,(88, 95, 193))
        surface.blit(matrix, (658, 430))
    
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
                
                if x>=670 and x<=745 and y>=345 and y<=370: # selecting matrix 3x3
                    self.ChangeGame(3)
                elif x>=670 and x<=745 and y>=385 and y<=410: # selecting matrix 4x4
                    self.ChangeGame(4)
                elif x>=670 and x<=745 and y>=425 and y<=450: # selecting matrix 5x5
                    self.ChangeGame(5)
                elif x>=650 and x<=745 and y>=253 and y<=280: # selecting vs human
                    self.vs_human = True
                    self.running = True
                    self.gameover = False
                elif x>=670 and x<=725 and y>=302 and y<=330: # selecting vs computer
                    self.vs_computer = True
                    self.running = True
                    self.gameover = False
                                
    def display_user_details(self,surface):
        if self.vs_human:
            input_boxes = [self.player.input_box1, self.player.input_box2]
        else:
            input_boxes = [self.player.input_box1]

        # display of P1 tag
        details_1 = smaller_font.render('Player 1',1,overall_color)
        surface.blit(details_1,(672, 140))

        # display of name tag for P1
        name_txt = even_smaller_font.render('Name : ',1,overall_color)
        surface.blit(name_txt,(612, 190))

        # display of choose symbol tag for P1 
        choose_txt = even_smaller_font.render('Choose :',1,overall_color)
        surface.blit(choose_txt,(612, 230))

        # display of cross symbol
        check_box1 = smaller_font.render('X',1,cross_color)
        surface.blit(check_box1,(696, 230))

        # display of circle symbol
        check_box2 = smaller_font.render('O',1,circle_color)
        surface.blit(check_box2,(756, 230))

        # display of selected symbol by player1
        tick = even_smaller_font.render('<--',1,overall_color)
        if self.player.player_cross == 0:
            surface.blit(tick,(706, 230))
        else:
            surface.blit(tick,(771, 230))

        # display of P2 tag 
        if self.vs_human:
            details_2 = smaller_font.render('Player 2',1,overall_color)
            surface.blit(details_2,(672, 300))
            surface.blit(name_txt,(612, 340))
        else:
            pick_turn = smaller_font.render(2-self.turn_computer,1,overall_color)
            surface.blit(pick_turn,(Size+(self.surface.get_width()-Size)//2 - pick_turn.get_width()//2,300))
        # display of play button
        play_button = smaller_font.render('Play',1,overall_color)
        surface.blit(play_button,(684, 450))        


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
                if x>=696 and x<=730 and y>=227 and y<=245:
                    self.player.player_cross = 0
                elif x>=731 and x<=770 and y>=227 and y<=245:
                    self.player.player_cross = 1
                if x>=665 and x<=722 and y>=450 and y<=480:
                    self.user_details_received = True
                if self.vs_computer:
                    # if x>=731 and x<=770 and y>=227 and y<=245:
                    #     self.turn_computer = 1-self.turn_computer
                    self.ai = AI(0.2,self.turn_computer+1)
                    self.ai.load_policy(N)
                    if N == 3:
                        self.learning = False
                    else:
                        self.learning = True                    
            for i,box in enumerate(input_boxes):
                player_name_received = box.handle_event(event)
                if i :
                    self.player.player2_name = player_name_received
                else:
                    self.player.player1_name = player_name_received
                    
        for box in input_boxes:
            box.update()
            box.draw(self.surface)
    
    def display_reset(self):

        # display of result
        if(self.result == 0):
            return
        elif(self.result == 1):
            win = smaller_font.render(self.player.player1_name + ' Won !! :)', 1, (125,0,125))
        elif(self.result == 2):
            win = smaller_font.render(self.player.player2_name + ' Won !! :)' , 1, (125,0,125))
        else:
            win = smaller_font.render('Draw :(', 1, (125,0,125))

        self.surface.blit(win, (Size+(self.surface.get_width()-Size)//2 - win.get_width()//2, 280))
        
        # display of reset
        reset = font.render("Reset", 1, overall_color)
        self.surface.blit(reset, (Size+(self.surface.get_width()-Size)//2 - reset.get_width()//2, 500))

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
    
    def ChangeGame(self,n):
        global N
        global Cell_Size
        N = n
        Cell_Size = Size//n
        params.N = n
        params.Cell_Size = params.Size//params.N
        GridLines.N = n
        if n!=3:
            GridLines.win_condition = 4
        else:
            GridLines.win_condition = 3
        GridLines.Cell_Size = GridLines.Size//GridLines.N
        Players.Cell_Size = Size//N
        self.grid = Grid()
