import pygame
from params import Cell_Size,cross_color


class Cross:
    def __init__(self,x,y):
        
        #Coordinates of Cell 
        self.x = x
        self.y = y

        self.color = cross_color
        self.thickness = 4
        
        # Diagonal 1
        self.line1_start = (self.x*Cell_Size , self.y*Cell_Size)
        self.line1_end = ((self.x+1)*Cell_Size , (self.y+1)*Cell_Size)

        # Diagonal 2
        self.line2_start = ((self.x+1)*Cell_Size , self.y*Cell_Size)
        self.line2_end = (self.x*Cell_Size , (self.y+1)*Cell_Size)

    def draw(self,surface):
        pygame.draw.line(surface, self.color, self.line1_start, self.line1_end, self.thickness)
        pygame.draw.line(surface, self.color, self.line2_start, self.line2_end, self.thickness)