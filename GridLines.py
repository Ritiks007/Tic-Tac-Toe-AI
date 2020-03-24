import pygame
from params import Cell_Size,N,Size,grid_color,grid_thickness,font

class Grid:
    def __init__(self):
        self.empty_positions=N*N
        rows, cols = (N, N) 
        self.CheckGrid = [[-1 for i in range(cols)] for j in range(rows)]
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
            menu = font.render('MENU', 1, (255,0,0))
            surface.blit(menu, (Cell_Size*(N+0.5), 20))

    def update(self, x, y, t):
        self.CheckGrid[x][y] = t+1
        self.empty_positions-=1

    def check(self, x, y):
        return self.CheckGrid[x][y]

    def _right(self, a, b, t):
        if(a == N or self.CheckGrid[a][b] != t):
            return 0
        return 1 + self._right(a+1, b, t)

    def _left(self, a, b, t):
        if(a == -1 or self.CheckGrid[a][b] != t):
            return 0
        return 1 + self._left(a-1, b, t)

    def _up(self, a, b, t):
        if(b == -1 or self.CheckGrid[a][b] != t):
            return 0
        return 1 + self._up(a, b-1, t)

    def _down(self, a, b, t):
        if(b == N or self.CheckGrid[a][b] != t):
            return 0
        return 1 + self._down(a, b+1, t)

    def _leftUp(self, a, b, t):
        if(a == -1 or b == -1 or self.CheckGrid[a][b] != t):
            return 0
        return 1 + self._leftUp(a-1, b-1, t)

    def _rightUp(self, a, b, t):
        if(a == N or b == -1 or self.CheckGrid[a][b] != t):
            return 0
        return 1 + self._rightUp(a+1, b-1, t)

    def _leftdown(self, a, b, t):
        if(a == -1 or b == N or self.CheckGrid[a][b] != t):
            return 0
        return 1 + self._leftdown(a-1, b+1, t)

    def _rightDown(self, a, b, t):
        if(a == N or b == N or self.CheckGrid[a][b] != t):
            return 0
        return 1 + self._rightDown(a+1, b+1, t)

    def checkwin(self,x,y,t):
        win = []
        win.append(self._right(x+1, y, t+1) + 1 + self._left(x-1, y, t+1))
        win.append(self._leftdown(x-1, y+1, t+1) + 1 + self._rightUp(x+1, y-1, t+1))
        win.append(self._rightDown(x+1, y+1, t+1) + 1 + self._leftUp(x-1, y-1, t+1))
        win.append(self._up(x, y-1, t+1) + 1 + self._down(x,y+1, t+1))
        if((win[0]<4 and win[1]<4 and win[2]<4 and win[3]<4) and self.empty_positions>0):
            return 0
        elif((win[0]<4 and win[1]<4 and win[2]<4 and win[3]<4) and self.empty_positions==0):
            return 3
        elif((win[0]>=4 or win[1]>=4 or win[2]>=4 or win[3]>=4) and t==0):
            return 1
        elif((win[0]>=4 or win[1]>=4 or win[2]>=4 or win[3]>=4) and t==1):
            return 2

    def reset(self):
        self.CheckGrid = [[-1 for i in range(N)] for j in range(N)]
        self.empty_positions = N*N