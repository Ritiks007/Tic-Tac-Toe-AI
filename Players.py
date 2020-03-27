import pygame

from params import Cell_Size,cross_color,cross_thickness,circle_color,circle_thickness
from get_input_func import InputBox

class Cross:
    def __init__(self,x,y):
        
        #Coordinates of Cell 
        self.x = x
        self.y = y

        self.color = cross_color
        self.thickness = cross_thickness

        # Diagonal 1
        self.line1_start = (self.x*Cell_Size , self.y*Cell_Size)
        self.line1_end = ((self.x+1)*Cell_Size , (self.y+1)*Cell_Size)

        # Diagonal 2
        self.line2_start = ((self.x+1)*Cell_Size , self.y*Cell_Size)
        self.line2_end = (self.x*Cell_Size , (self.y+1)*Cell_Size)

    def draw(self,surface):
        # Draw the cross
        pygame.draw.line(surface, self.color, self.line1_start, self.line1_end, self.thickness)
        pygame.draw.line(surface, self.color, self.line2_start, self.line2_end, self.thickness)

class Circle:
    def __init__(self,x,y):
        
        #Coordinates of Cell 
        self.x = x
        self.y = y

        self.color = circle_color
        self.thickness = circle_thickness
        self.radius = Cell_Size//2
        self.center = (self.x*Cell_Size + self.radius, self.y*Cell_Size + self.radius)
        
    def draw(self,surface):
        # Draw the circle
        pygame.draw.circle(surface, self.color, self.center, self.radius, self.thickness)

class Player:
    def __init__(self):
        self.players = []
        self.players.append([])
        self.players.append([])
        self.player_cross = 0   #Determines which player's symbol is cross
        self.player1_name = 'Human1'
        self.player2_name = 'Human2'
        
        self.input_box1 = InputBox(670, 188, 110, 20,self.player1_name)
        self.input_box2 = InputBox(670, 338, 110, 20,self.player2_name)


    def move(self,turn,x,y):
        if turn == self.player_cross:
            # If turn is of cross, append a cross
            cross = Cross(x,y)
            self.players[self.player_cross].append(cross)
        else:
            # If turn is of circle, append a circle
            circle = Circle(x,y)
            self.players[1-self.player_cross].append(circle)

    def draw(self,surface):
        # Draw all crosses and circles
        for c in self.players:
            for ci in c:
                ci.draw(surface)

    def reset(self):
        # Reset everything
        self.players.clear()
        self.players.append([])
        self.players.append([])
        self.player_cross = 0
        self.player1_name = 'Human1'
        self.player2_name = 'Human2'
        self.input_box1 = InputBox(670, 188, 110, 20,self.player1_name)
        self.input_box2 = InputBox(670, 338, 110, 20,self.player2_name)

