import os
import bpy
import bpy.utils.previews

class PTM_IconMgr(object):
    class __PTM_IconMgr:
        def __init__(self):
            pass

        def __str__(self):
            return "self" + self.images
        
        def get_icon(self, key):
            return self.images[key]
        
        def load(self):
            self.images =  bpy.utils.previews.new()
            
            icons_dir = os.path.join(os.path.dirname(__file__), "icons")
            self.images.load("align_left", os.path.join(icons_dir, "align.png"), 'IMAGE')
            
             
        def unload(self):
            bpy.utils.previews.remove(self.images)        
        
    instance = None
    
    def __new__(cls): # __new__ always a classmethod
        if not PTM_IconMgr.instance:
            PTM_IconMgr.instance = PTM_IconMgr.__PTM_IconMgr()
        return PTM_IconMgr.instance
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)