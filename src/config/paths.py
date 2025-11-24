"""import os, sys

if hasattr(sys,'_MEIPASS'):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))


asset_dir = os.path.join(base_dir,'assets')
images_dir = os.path.join(asset_dir,'images')
background_dir = os.path.join(asset_dir,'backgrounds')
sounds_dir = os.path.join(asset_dir,'sounds')
fonts_dir = os.path.join(asset_dir,'fonts')

src_dir = os.path.join(base_dir,'src')
config_dir = os.path.join(src_dir,'config')
game_dir = os.path.join(src_dir,'game')
scene_dir = os.path.join(src_dir,'scene')
utils_dir = os.path.join(src_dir,'utils')
entities_dir = os.path.join(src_dir,'entities')
ui_dir = os.path.join(src_dir,'ui')
audio_dir = os.path.join(src_dir,'audio')

"""

from pathlib import Path
import sys

if hasattr(sys,'_MEIPASS'):
    base_dir = sys._MEIPASS
else:
    BASE_DIR = Path(__file__).resolve().parent
