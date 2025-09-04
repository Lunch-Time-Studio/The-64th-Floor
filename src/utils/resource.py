import os, pygame
from .cache import LoaderCache
from config import paths

class Loaders:
# === image ===
    def __init__(self):
        self.cache = LoaderCache()
        self.ImageCache = self.cache.images
        self.SoundCache = self.cache.sounds
        self.FontCache = self.cache.fonts

    def load_image(self,filename):
        if filename in self.ImageCache:
            return self.ImageCache[filename]
        
        path = os.path.join(paths.images_dir, filename)
        image = pygame.image.load(path).convert_alpha()
        self.ImageCache[filename] = image
        return image

    # === sound ===
    def load_sound(self,filename):
        if filename in self.SoundCache:
            return self.SoundCache[filename]
        
        path = os.path.join(paths.sounds_dir, filename)
        sound = pygame.mixer.Sound(path)
        self.SoundCache[filename] = sound
        return sound

    # === font ===
    def load_font(self,filename, size):
        key = f"{filename}_{size}"
        if key in self.FontCache:
            return self.FontCache[key]
        
        path = os.path.join(paths.fonts_dir, filename)
        font = pygame.font.Font(path, size)
        self.FontCache[key] = font
        return font

