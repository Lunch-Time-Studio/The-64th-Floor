import pygame, sys, os
from src.utils import *
from src.core import SceneManager
#from . import scene_change
from pygame.locals import *

def main (self):
    self.FPS.tick(60)
    running = True

    while running:
    #input ===========================================
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          x, y = event.pos
          if startbox.collidepoint(x, y):
            print('clicked on image')
          #if endbox.collidepoint(x,y):
            
    #input ===========================================

      SceneManager.allscene.BackgroundLoad(self)
      SceneManager.allscene.BackgroundDraw(self)
          
    #object ==========================================

      button1 = ImageUtils.ImageScale(resource.load_image("box.xcf"),(300,150))
      buttonw = button1.get_rect()[2]
      buttonh = button1.get_rect()[3]
      button = buttonw,buttonh
      buttonfirst = self.dw/2-buttonw/2,self.dh/4-buttonh/2
      buttonc = self.dw/2-buttonw/2,self.dh/2-buttonh/2
      buttonthird = self.dw/2-buttonw/2,(3*self.dh)/4-buttonh/2

      startbox = pygame.Rect(buttonc,button)
      endbox = pygame.Rect(buttonthird,button)

    #object ==========================================

      self.window.blit(button1,buttonc)
      self.window.blit(button1,buttonthird)
      pygame.display.update()
