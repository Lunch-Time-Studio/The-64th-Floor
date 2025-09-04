import os, pygame

def find_centre(image):
        w = image.get_rect()[2]
        h = image.get_rect()[3]
        centre = w/2,h/2
        return centre