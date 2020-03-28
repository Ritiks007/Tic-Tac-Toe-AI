import pygame
pygame.init()
# Game Parameters
# Default game mode : 3*3  Change to 4 or 5 to change mode
N = 3

# Default winning condition : 3 consecutive to win
win_condition = 3

# Game Window 
Size = 600
Game_Window = [Size + 200 ,Size]
Cell_Size = Game_Window[1]//N
grid_thickness = 3

# Colors
cross_color = (130,114,195)
cross_thickness = 4
circle_color = (235,117,117)
circle_thickness = 3
overall_color = (122, 24, 70)
background = (255, 255, 240)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

# Fonts
font = pygame.font.SysFont(None, 32)
smaller_font = pygame.font.SysFont(None, 25)
even_smaller_font = pygame.font.SysFont(None, 20)
