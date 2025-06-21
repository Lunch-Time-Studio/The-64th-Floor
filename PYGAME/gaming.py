import pygame, sys
from pygame.locals import *
pygame.init()

displayw = 1600
displayh = 1000
window = pygame.display.set_mode((displayw,displayh))

FPS = pygame.time.Clock()

pygame.display.set_caption("The 64th Floor")

background = pygame.image.load("/home/sh1224/The-64th-Floor/Images/Backgrounds/Temp_background2.xcf")
button1 = pygame.image.load("/home/sh1224/The-64th-Floor/Images/box.xcf")

# THIS WILL BE REPLACED BY ACTUAL TITLE ILUSTRATION: THIS IS TEMPORARY
pygame.font.init()
font1 = pygame.font.Font(None,100)
Title = font1.render("The 64th Floor",True,(0,0,0))
# THIS WILL BE REPLACED BY ACTUAL TITLE ILUSTRATION: THIS IS TEMPORARY 

class starter:
  def __init__ (self,displayw,displayh,background):
    self.dw = displayw
    self.dh = displayh
    self.background = background
    self.main()

  def main (self):
    FPS.tick(60)
    running = True
    
    while running:
#background ======================================

      backgroundc = self.dw/2, self.dh/2
      window.blit(background,(0,0))
      
#background ======================================
      
#input ===========================================
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
#input ===========================================
          
#object ==========================================

      buttonw = button1.get_rect()[2]/2
      buttonh = button1.get_rect()[3]/2
      buttonfirst = self.dw/2-buttonw,self.dh/4-buttonh
      buttonc = self.dw/2-buttonw,self.dh/2-buttonh
      buttonthird = self.dw/2-buttonw,(3*self.dh)/4-buttonh

#object ==========================================

      window.blit(Title,buttonfirst)
      window.blit(button1,buttonc)
      window.blit(button1,buttonthird)
      pygame.display.update()


print(__name__)
if __name__ == '__main__':
    starter(displayw,displayh,background)
