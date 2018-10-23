from ArchicadDG import *
from ArchicadGS import *

class Form(Palette):
    def __init__(self):
        super(Form,self).__init__(Rect(Point(0,0),400,500))

        self.pck=PushMenuCheck(self,Rect(Point(10,10),150,40))
        print 'GetItemCount:'+str(self.pck.GetItemCount())
        self.pck.SetItemCount(15)
        self.pck.SetItemIcon(1)
        self.pck.SetItemIcon(2)
        self.pck.SetItemIcon(3)
        print 'GetItemCount:'+str(self.pck.GetItemCount())
        self.pck.Show()
        self.pck_obs=PushMenuObserver(self.pck)
        self.pck_obs.PushMenuChanged=self.menu_change


        self.prd1=PushMenuRadio(self,Rect(Point(170,10),150,40),1)
        self.prd1.SetItemCount(2)
        self.prd1.Show()
        self.prd1_obs=PushMenuObserver(self.prd1)
        self.prd1_obs.PushMenuChanged=self.menu_change

        self.prd2=PushMenuRadio(self,Rect(Point(170,60),150,40),1)
        self.prd2.SetItemCount(2)
        self.prd2.Show()
        self.prd2_obs=PushMenuObserver(self.prd2)
        self.prd2_obs.PushMenuChanged=self.menu_change

    def menu_change(self,sender,e):
        print type(e)
        print str(sender.GetSelectedItem())
        

