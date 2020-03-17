import pygame
from Environment.py import Cell_Size


class Cross:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = (200,200,200)
        self.line1_start = (self.x*Cell_Size , self.y*Cell_Size)
        self.line1_end = ((self.x+1)*Cell_Size , (self.y+1)*Cell_Size)
        self.line2_start = ((self.x+1)*Cell_Size , self.y*Cell_Size)
        self.line2_end = (self.x*Cell_Size , (self.y+1)*Cell_Size)
        self.thickness = 2

    def draw(self,surface):
        pygame.draw.line(surface, color, line1_start, line1_end, thickness)
        pygame.draw.line(surface, color, line2_start, line2_end, thickness)