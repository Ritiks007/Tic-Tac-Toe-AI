import pygame as pg
from params import COLOR_ACTIVE,COLOR_INACTIVE,even_smaller_font as font

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.cursor = ''
        self.blink = 0

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.

            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.active = False
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                # self.txt_surface = font.render(self.text+self.cursor, True, self.color)
        return self.text
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        if self.active:
            if self.blink >= 160 and self.blink <= 480:
                self.cursor = '|'
                self.blink +=1
            elif self.blink == 640:
                self.cursor = ''
                self.blink = 0
            else:
                self.cursor = ''
                self.blink +=1
        else:
            self.cursor = ''
            self.blink = 0
        self.txt_surface = font.render(self.text+self.cursor, True, self.color)
        screen.blit(self.txt_surface, (self.rect.x+4, self.rect.y+3))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 1)

