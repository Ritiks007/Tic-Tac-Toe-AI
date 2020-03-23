import pygame
from params import Cell_Size,cross_color,cross_thickness,circle_color,circle_thickness


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
        self.center = (self.x*Cell_Size + self.radius , self.y*Cell_Size + self.radius)
        
    def draw(self,surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius, self.thickness)

class Player:
    def __init__(self):
        self.players = []
        self.players.append([])
        self.players.append([])
        self.player_cross = 0

    def move(self,turn,x,y):
        if turn == self.player_cross:
            cross = Cross(x,y)
            self.players[self.player_cross].append(cross)
        else:
            circle = Circle(x,y)
            self.players[1-self.player_cross].append(circle)

    def draw(self,surface):
        for c in self.players:
            for ci in c:
                ci.draw(surface)
        
