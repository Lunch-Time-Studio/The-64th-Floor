import pygame, sys, os
import logic
from pygame.locals import *
pygame.init()

pygame.display.set_caption("The 64th Floor")

class MAINRUN():
  def __init__ (self):
    self.dir = os.getcwd()
    self.background = pygame.image.load(os.path.join(self.dir,"Images/Backgrounds/gress-background.png"))
    self.window = pygame.display.set_mode()
    self.dw, self.dh = self.window.get_size()
    self.FPS = pygame.time.Clock()
    self.main()

  def main (self):
    self.FPS.tick(60)
    running = True
    
    while running:
#background ======================================

      logic.graphics.background(self)
      
#background ======================================
      
#input ===========================================
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
#input ===========================================
          
#object ==========================================

      """
      buttonw = button1.get_rect()[2]/2
      buttonh = button1.get_rect()[3]/2
      buttonfirst = self.dw/2-buttonw,self.dh/4-buttonh
      buttonc = self.dw/2-buttonw,self.dh/2-buttonh
      buttonthird = self.dw/2-buttonw,(3*self.dh)/4-buttonh
      """

#object ==========================================

      pygame.display.update()


print(__name__)
if __name__ == '__main__':
    MAINRUN()
