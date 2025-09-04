import pygame, os
from . import *

class background:
    def __init__ (self,FileName):
        self.background = resource.load_image(FileName)

    def BackgroundLoad (self):
        scalex = self.window.get_width() / 128
        self.background = pygame.transform.scale(self.background, (128 * scalex, 128 * scalex))

    def BackgroundDraw (self):
        self.window.blit(self.background,(0,0))


    