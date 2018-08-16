from ArchicadDG import *

def hot_key(panel,e):
    print '--hot_key---'
    print str(e.KeyId)
    pass

def panel_move(panel,e):
    print '--panel_move--'
    pass

class FormPalette(object):
    def __init__(self):
        self.pal=Palette(Rect(30,40,400,480),Dialog.HVGrow,Dialog.Close)
        self.pal_obs=PanelObserver(self.pal)
        #listen CloseRequested event
        self.pal_obs.CloseRequested=self.close_request
        #listen HotkeyPressed event
        self.pal_obs.HotkeyPressed=hot_key
        #listen ResizeEntered event
        self.pal_obs.ResizeEntered=self.resize_entered
        #listen Moving event
        self.pal_obs.Moving=panel_move
        #more event;you can test it
        pass

    def Show(self):
        #regist hot key
        print '--regist hot key--'
        print str(self.pal.RegisterHotKey(Key.F1,Key.NoModifier,Key.NoModifier,Key.NoModifier))
        cd=Key.Code('e')
        print str(self.pal.RegisterHotKey(cd.GetValue(),Key.NoModifier,Key.NoModifier,Key.NoModifier))
        self.pal.Show()
        pass

    def close_request(self,panel,e):
        print '--Palette Close Request--'
        pass

    def resize_entered(self,panel,e):
        print '--resize_entered--'
        pass


