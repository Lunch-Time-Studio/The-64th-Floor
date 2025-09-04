import os, sys, pygame
from src.utils import *

class allscene:
    def __init__ (self):
        pygame.display.set_caption("The 64th Floor")
        self.window = pygame.display.set_mode()
        self.dw, self.dh = calc.WindowSize(self.window)
        self.FPS = pygame.time.Clock()
        self.background = background()
        self.running = True
    
    def HandleEvents (self):
        pass

    def Update (self):
        pass

    def Render (self):
        pass

    def run (self):
        while self.running:
            self.HandleEvents()
            self.Update()
            self.Render()
            pygame.display.update()


