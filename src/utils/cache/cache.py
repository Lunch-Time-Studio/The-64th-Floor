import json
from pathlib import Path
from cache_utils import ensure_cache_file  # ← 네가 만든 외부 함수 불러오는 위치

class LoaderCache:
    def __init__(self):
        self.images = self.Loading_Cache("Image.json")
        self.sounds = self.Loading_Cache("Sound.json")
        self.fonts = self.Loading_Cache("Font.json")

    def Loading_Cache(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            ensure_cache_file(Path(filename))
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Cache] {filename} Loading Failed: {e}")
            return {}

    def CacheLoad(self, kind, key):
        return getattr(self, kind).get(key)

    def CacheSet(self, kind, key, value):
        getattr(self, kind)[key] = value
