import pygame, os, sys
import logic

def fade_in (self,next_file):
    self.alpha = 0
    self.colour = (0,0,0)
    self.surface = pygame.Surface((self.dw, self.dh))
    self.surface.fill(self.colour)
    fade = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if fade:
            self.alpha += 5
            if self.alpha >= 255:
                self.alpha = 255
                fade = False
                
        elif fade == False:
            self.alpha -= 5
            if self.alpha <= 0:
                self.alpha = 0
                imported = __import__(next_file)
                imported.main(self)
                
        self.surface.set_alpha(self.alpha)
        logic.graphics.background(self)
        self.window.blit(self.surface, (0,0))
        pygame.display.flip()
        

def fade_out (self,next_file):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        self.alpha -= 2
        if self.alpha <= 0:
            self.alpha = 0
            imported = __import__(next_file)
            imported.main(self)

        self.surface.fill((*self.colour,self.alpha))
        self.window.blit(self.surface, (0,0))
        pygame.display.flip()
