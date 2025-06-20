import pygame, sys
from pygame.locals import *
pygame.init()

displayw = 1000
displayh = 600
window = pygame.display.set_mode((displayw,displayh))

FPS = pygame.time.Clock()

pygame.display.set_caption("ChessFront")

background = pygame.image.load("/home/sh1224/ChessFront/Images/Backgrounds/temporary_background.xcf")
option1 = pygame.image.load("/home/sh1224/ChessFront/Images/rectangle.png")
option2 = pygame.image.load("/home/sh1224/ChessFront/Images/rectangle.png")



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
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      
      
      window.blit(background,(0,0))
      window.blit(option1,(0,0))
      window.blit(option2,(0,0))
      pygame.display.update()


print(__name__)
if __name__ == '__main__':
    starter(displayw,displayh,background)


