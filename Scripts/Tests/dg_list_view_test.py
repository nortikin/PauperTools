from ArchicadDG import *
from ArchicadGfx import *


class Form(Palette):
    def __init__(self):
        super(Form,self).__init__(Rect(Point(0,0),450,600))

        self.sslv=MultiSelListView(self,Rect(Point(10,10),430,300))

        self.sslv.AppendItem()
        self.sslv.SetItemText(1,"LV1")

        self.sslv.AppendItem()
        self.sslv.SetItemText(2,"LV2")
        self.sslv.SetItemColor(2,Color.Red)

        self.sslv.AppendItem()
        self.sslv.SetItemText(3,"LV3")
        self.sslv.DisableItem(3)

        self.sslv.AppendItem()
        self.sslv.SetItemText(4,"LV4")
        
        self.sslv.Show()


        self.sslv.SetBackground(ListView.BGButtonFace)
        self.sslv.SetSelectionStyle(ListView.SSPush)
        self.sslv.SetViewMode(ListView.RightText)
        self.sslv.SelectItems([1,4])
        self.sslv.EnableMouseMoveEvent()
        self.sslv.EnableHoverEvent()
        self.sslv.EnablePressedEvent()
        print 'GetBackground:'+str(self.sslv.GetBackground())


        self.sslvobs=ListViewObserver(self.sslv)
        self.sslvobs.ListViewSelectionChanged=self.lvs_change
        self.sslvobs.ListViewContextMenuRequested=self.lv_cmenu
        self.sslvobs.ListViewMouseDown=self.lv_mdown
        self.sslvobs.ListViewDoubleClicked=self.lv_dclick
        self.sslvobs.ListViewMouseMoved=self.lv_mmove
        self.sslvobs.ListViewItemUpdate=self.lv_iupdate
        self.sslvobs.ListViewHoverStarted=self.lv_hstarted
        self.sslvobs.ListViewPressed=self.lv_pressed
        pass

    def lvs_change(self,sender,e):
        print '--lvs_change--'
        print 'sel count:'+str(sender.GetSelectedCount())
        print 'sel:'+str(sender.GetSelectedItems())

    def lv_cmenu(self,sender,e):
        print '--lv_cmenu--'

    def lv_mdown(self,sender,e):
        print '--lv_mdown--'

    def lv_dclick(self,sender,e):
        print '--lv_dclick--'

    def lv_mmove(self,sender,e):
        print '--lv_mmove--'

    def lv_iupdate(self,sender,e):
        print '--lv_iupdate--'

    def lv_hstarted(self,sender,e):
        print '--lv_hstarted--'

    def lv_pressed(self,sender,e):
        print '--lv_pressed--'
    
                 
        
