from ArchicadDG import *

class FormPalette(object):
    def __init__(self):
        self.pal=Palette(Rect(0,0,400,450),Dialog.HVGrow,Dialog.Close,Dialog.TopCaption,Dialog.NormalFrame)
        self.pal.Show()
        self.pal.SetTitle("palette test")
        print self.pal.GetTitle()
        pass
    
