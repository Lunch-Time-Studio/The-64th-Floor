import json

class LoaderCache:
    def __init__ (self):
        try:
           with open("Image.json") as f:
              self.images = json.load(f)
        except:
           return "Fail to load"
        
        try:
           with open("Sound.json") as f:
              self.sounds = json.load(f)
        except:
           return "Fail to load"
        
        try:
           with open("Font.json") as f:
              self.fonts = json.load(f)
        except:
           return "Fail to load"

    def CacheLoad (self,kind,key):
        return getattr(self,kind).get(key)
    
    def CacheSet (self,kind,key,value):
        getattr(self,kind)[key] = value


def load(location,idlocation):
  with open(location) as f:
    try:
      if f.read().strip() == '':
        return 'No data exist'
      else:
        f.seek(0)
        loadlist = json.load(f)
        pas = loadlist[idlocation]
    except:
      return 'Fail to load'
  return pas