import pygame, sys, os
from pygame.locals import *
pygame.init()

pygame.display.set_caption("The 64th Floor")

class MAINRUN():
  def __init__ (self):
    self.dw = 1920
    self.dh = 1080
    self.dir = os.getcwd()
    self.background = pygame.image.load(os.path.join(self.dir,"Images/Backgrounds/sector1-room.png"))
    self.window = pygame.display.set_mode((self.dw,self.dh))
    self.FPS = pygame.time.Clock()
    self.main()

  def background (self):
    scalex = self.window.get_width() / 128
    scaley = self.window.get_height() / 128
    background = pygame.transform.scale(self.background, (128 * scalex, 128 * scaley))
    #background = pygame.transform.scale(background,(1000,1000))
    self.window.blit(background,(0,0))

  def image_load(self,directory,image_code):
    image = pygame.image.load("")    

  def main (self):
    self.FPS.tick(60)
    running = True
    
    while running:
#background ======================================

      backgroundc = self.dw/2, self.dh/2
      MAINRUN.background(self)
      
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
