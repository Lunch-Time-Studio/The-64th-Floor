import pygame, os

class graphics:
    def find_centre(image):
        w = image.get_rect()[2]
        h = image.get_rect()[3]
        centre = w/2,h/2
        return centre

    def resize (image,size):
        image = pygame.transform.scale(image,size)
        return image

    def image_load(self,directory,file_name):
        image = pygame.image.load(os.path.join(self.dir ,directory,file_name))
        return image

    def background (self):
        scalex = self.window.get_width() / 128
        background = pygame.transform.scale(self.background, (128 * scalex, 128 * scalex))
        self.window.blit(background,(0,0))
