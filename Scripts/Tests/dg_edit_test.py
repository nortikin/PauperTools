from ArchicadDG import *

class PaletteForm(object):
    def __init__(self):
        
        self.pal=Palette(Rect(Point(0,0),400,500),Dialog.HVGrow,Dialog.Close)

        #Create PosIntEdit and Show
        self.pos_int=PosIntEdit(self.pal,Rect(Point(10,10),120,30))
        self.pos_int.Show()
        self.pos_int_obs=PosIntEditObserver(self.pos_int)
        self.pos_int_obs.PosIntEditChanged=self.edit_change

        #Create IntEdit and Show
        self.int=IntEdit(self.pal,Rect(Point(10,40),120,30))
        self.int.Show()
        self.int_obs=IntEditObserver(self.int)
        self.int_obs.IntEditChanged=self.edit_change

        #Create RealEdit and Show
        self.real=RealEdit(self.pal,Rect(Point(10,70),120,30))
        self.real.Show()
        self.real_obs=RealEditObserver(self.real)
        self.real_obs.RealEditChanged=self.edit_change

        #Create LengthEdit and Show
        self.leth=LengthEdit(self.pal,Rect(Point(10,100),120,30))
        self.leth.Show()
        self.leth_obs=RealEditObserver(self.leth)
        self.leth_obs.RealEditChanged=self.edit_change

        #Create AngleEdit and Show
        self.angl=AngleEdit(self.pal,Rect(Point(10,130),120,30))
        self.angl.Show()
        self.angl_obs=RealEditObserver(self.angl)
        self.angl_obs.RealEditChanged=self.edit_change

        #Create PolarAngleEdit and Show
        self.polar=PolarAngleEdit(self.pal,Rect(Point(10,160),120,30))
        self.polar.Show()
        self.polar_obs=RealEditObserver(self.polar)
        self.polar_obs.RealEditChanged=self.edit_change

        #Create MMPointEdit and Show
        self.mmp=MMPointEdit(self.pal,Rect(Point(10,190),120,30))
        self.mmp.Show()
        self.mmp_obs=RealEditObserver(self.mmp)
        self.mmp_obs.RealEditChanged=self.edit_change

        #Create TextEdit and Show
        self.text=TextEdit(self.pal,Rect(Point(10,220),150,30))
        self.text.Show()
        self.text_obs=TextEditBaseObserver(self.text)
        self.text_obs.TextEditChanged=self.edit_change

        #Create PasswordEdit and Show
        self.pwd=PasswordEdit(self.pal,Rect(Point(10,250),150,30))
        self.pwd.Show()
        self.pwd_obs=TextEditBaseObserver(self.pwd)
        self.pwd_obs.TextEditChanged=self.edit_change

        #Create ShortcutEdit and Show
        self.sht=ShortcutEdit(self.pal,Rect(Point(10,280),150,30))
        self.sht.Show()
        self.sht_obs=TextEditBaseObserver(self.sht)
        self.sht_obs.TextEditChanged=self.edit_change
        self.sht_hit_obs=ShortcutEditObserver(self.sht)
        self.sht_hit_obs.ShortcutHit=self.sht_hit

        #Create MultiLineEdit and Show
        self.mul=MultiLineEdit(self.pal,Rect(Point(150,10),200,200),MultiLineEdit.ScrollType.HVScroll)
        self.mul_obs=TextEditBaseObserver(self.mul)
        self.mul_obs.TextEditChanged=self.edit_change
        self.mul.Show()
        
        self.pal.Show()
        pass

    def edit_change(self,sender,e):
        print '--edit_change--'
        print type(sender)
        print type(e)
        #print 'text:'+sender.GetText()

    def sht_hit(self,sender,e):
        print '--sht_hit--'
        print 'char:'+e.Key.GetChar()
        sender.CatText(e.Key.GetChar())
        sender.Invalidate()
        pass
        
    
