import pygame
from params import Cell_Size,N,Size,grid_color,grid_thickness

class Grid:
	def __init__(self):

		self.gridlines = [((Size, 0),(Size, Size))] # side bar

		# vertical lines
		i = N - 1
		while(i):
			Tup = ((i*Cell_Size, 0), (i*Cell_Size, Size))
			self.gridlines.append(Tup)
			i -= 1

		# horizontal lines
		i = N - 1
		while(i):
			Tup = ((0,i*Cell_Size), (Size, i*Cell_Size))
			self.gridlines.append(Tup)
			i -= 1

	def draw(self, surface):
		for line in self.gridlines:
			pygame.draw.line(surface, grid_color, line[0], line[1], grid_thickness)