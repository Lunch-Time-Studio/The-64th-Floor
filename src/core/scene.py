import os, sys, pygame
from utils import *

class allscene:
    def __init__ (self):
        self.window = pygame.display.set_mode()
        self.dw, self.dh = self.window.get_size()
        self.FPS = pygame.time.Clock()
        self.background = None
    
    def BackgroundLoad (self):
        scalex = self.window.get_width() / 128
        self.background = pygame.transform.scale(self.background, (128 * scalex, 128 * scalex))

    def BackgroundDraw (self):
        self.window.blit(self.background,(0,0))
