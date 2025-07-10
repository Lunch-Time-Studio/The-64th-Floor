import os, pygame
from .cache import ResourceCache
from config import paths

ImageCache = {}
SoundCache = {}
FontCache = {}

# === image ===
def load_image(filename):
    if filename in ImageCache:
        return ImageCache[filename]
    
    path = os.path.join(paths.images_dir, filename)
    image = pygame.image.load(path).convert_alpha()
    ImageCache[filename] = image
    return image

# === sound ===
def load_sound(filename):
    if filename in SoundCache:
        return SoundCache[filename]
    
    path = os.path.join(paths.sounds_dir, filename)
    sound = pygame.mixer.Sound(path)
    SoundCache[filename] = sound
    return sound

# === font ===
def load_font(filename, size):
    key = f"{filename}_{size}"
    if key in FontCache:
        return FontCache[key]
    
    path = os.path.join(paths.fonts_dir, filename)
    font = pygame.font.Font(path, size)
    FontCache[key] = font
    return font

