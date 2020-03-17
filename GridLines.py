import pygame
from Environment.py import Cell_Size
from Environment.py import N
from Environment.py import Size
class Grid:
	def __init__(self):

		self.gridlines = [((Size, 0),(Size, Size))] # size bar

		# vertical lines
		i = N - 1
		while(i):
			Tup = ((i*Cell_Size, 0), (i*Cell_Size, Size))
			gridlines.append(Tup)
			i -= 1

		# horizontal lines
		i = N - 1
		while(i):
			Tup = ((0,i*Cell_Size), (Size, i*Cell_Size))
			gridlines.append(Tup)
			i -= 1

	def draw(self, surface):
		for line in self.gridlines:
			pygame.draw.line(surface, (0, 0, 0), line[0], line[1], 2)