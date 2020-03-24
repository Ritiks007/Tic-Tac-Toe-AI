def ask(question):
    '''ask(question) -> answer'''
    current_string = ""
    display_box(question + ": " + current_string)
    while 1:
        current_string += str(enterName.getCharacter)
        # show the full string while typing
        display_box(question + ": " + current_string)
    return current_string # this is the answer

class enterName:
    def getKeyPress(self):
      for event in pygame.event.get():
         if event.type == KEYDOWN:    
             return event.key
         else:
             return False

    def getCharacter(self):
      # Check to see if the player has used a modifier key (Shift, Alt, Ctrl)
      keyinput = pygame.key.get_pressed()  

      character = "NULL"

      # Get all "Events" that have occurred.
      pygame.event.pump()
      keyPress = self.getKeyPress()

      #If the user presses a key on the keyboard then get the character
      #If the user presses the shift key while pressing another character
      #then capitalise it
      if keyPress >= 32 and keyPress <= 126:
          if keyinput[K_LSHIFT]: 
              keyPress -= 32

          character = chr(keyPress)

      return character

def display_box(message):
  "Print a message in a box in the middle of the screen"
  left = (SCREENWIDTH / 2) - 156
  top = (SCREENHEIGHT / 2) + 4  #16
  pygame.draw.rect(SCREEN, DARKGREEN, (left, top, 320, 200)) # 320  240
  SCREEN.blit(BASICFONT.render("New High Score!", True, GREEN),
              (left + 90, top + 35)) # 55
  SCREEN.blit(BASICFONT.render("Press return when done.", True, GREEN),
              (left + 51, top + 160)) # 180
  
  pygame.draw.rect(SCREEN, BLACK, (left + 39, top + 110, 240, 20))
  pygame.draw.rect(SCREEN, WHITE, (left + 38, top + 108, 244, 24), 1)
  
  if len(message) != 0:
    SCREEN.blit(BASICFONT.render(message, True, WHITE), (left+42, top + 111))
                
  pygame.display.flip()
