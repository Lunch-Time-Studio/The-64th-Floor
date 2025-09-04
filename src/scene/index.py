import pygame, sys, os
from . import character_select
from assets import *
from src.utils import *
from src.core import SceneManager
from pygame.locals import *
pygame.font.init()


class index (SceneManager.allscene):
  def __init__ (self):
    super().__init__()
    font1 = pygame.font.Font(None,100)
    Title = font1.render("The 64th Floor",True,(0,0,0))

  def HandleEvents (self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if startbox.collidepoint(x, y):
          print('loading character selection page...')
          character_select.main(self)

  def Update (self):
      pass

  def Render (self):
      background.BackgroundLoad(self)
      background.BackgroundDraw(self)
      self.window.blit(Title,buttonfirst)
      self.window.blit(button1,buttonc)
      self.window.blit(button1,buttonthird)

          
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

      pygame.display.update()
