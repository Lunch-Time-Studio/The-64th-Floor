import os, pygame

def find_centre(image):
        w = image.get_rect()[2]
        h = image.get_rect()[3]
        centre = w/2,h/2
        return centre

def WindowSize (window):
        dw, dh = window.get_size()
        return dw,dh

def AlignButton(x, y):
        ''
        
        
        """
        buttonw = button1.get_rect()[2]
        buttonh = button1.get_rect()[3]
        button = buttonw,buttonh
        buttonfirst = self.dw/2-buttonw/2,self.dh/4-buttonh/2
        buttonc = self.dw/2-buttonw/2,self.dh/2-buttonh/2
        buttonthird = self.dw/2-buttonw/2,(3*self.dh)/4-buttonh/2
        """