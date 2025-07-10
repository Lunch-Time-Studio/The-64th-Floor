import pygame, sys, os
import logic,character_select
from pygame.locals import *
pygame.init()

pygame.display.set_caption("The 64th Floor")

# THIS WILL BE REPLACED BY ACTUAL TITLE ILUSTRATION: THIS IS TEMPORARY
pygame.font.init()
font1 = pygame.font.Font(None,100)
Title = font1.render("The 64th Floor",True,(0,0,0))
# THIS WILL BE REPLACED BY ACTUAL TITLE ILUSTRATION: THIS IS TEMPORARY 

class starter:
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
#input ===========================================
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          x, y = event.pos
          if startbox.collidepoint(x, y):
            print('loading character selection page...')
            character_select.main(self)
          #if endbox.collidepoint(x,y):
            
#input ===========================================

      logic.graphics.background(self)
          
#object ==========================================

      button1 = logic.graphics.resize(logic.graphics.image_load(self,"Images","box.xcf"),(300,150))
      buttonw = button1.get_rect()[2]
      buttonh = button1.get_rect()[3]
      button = buttonw,buttonh
      buttonfirst = self.dw/2-buttonw/2,self.dh/4-buttonh/2
      buttonc = self.dw/2-buttonw/2,self.dh/2-buttonh/2
      buttonthird = self.dw/2-buttonw/2,(3*self.dh)/4-buttonh/2

      startbox = pygame.Rect(buttonc,button)
      endbox = pygame.Rect(buttonthird,button)

#object ==========================================

      self.window.blit(Title,buttonfirst)
      self.window.blit(button1,buttonc)
      self.window.blit(button1,buttonthird)
      pygame.display.update()
