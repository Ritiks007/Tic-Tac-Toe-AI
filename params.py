import pygame
# Game Parameters
# Default game mode : 3*3 to 4*4
# Default winning condition : 3 consecutive to win
Size = 600
N = 5
Game_Window = [Size + 150 ,Size]
Cell_Size = Game_Window[1]//N
cross_color = (130,114,195)
cross_thickness = 4
circle_color = (235,117,117)
circle_thickness = 3
grid_thickness = 3
background = (255, 255, 230)
overall_color = (122, 24, 70)
font = pygame.font.SysFont('comicsansms', 32)
smaller_font = pygame.font.SysFont('comicsansms', 25)
even_smaller_font = pygame.font.SysFont('comicsansms', 20)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
