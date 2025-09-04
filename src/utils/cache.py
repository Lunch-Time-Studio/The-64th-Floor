class LoaderCache:
    def __init__ (self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}

    def CacheLoad (self,kind,key):
        return getattr(self,kind).get(key)
    
    def CacheSet (self,kind,key,value):
        getattr(self,kind)[key] = value


