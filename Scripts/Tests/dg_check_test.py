from ArchicadDG import *

class Form(Palette):
    def __init__(self):
        super(Form,self).__init__(Rect(Point(0,0),350,430))

        self.cb=CheckBox(self,Rect(Point(20,50),80,30))
        self.cb.SetText("CheckBox")
        self.cb.Show()
        self.cb_obs=CheckItemObserver(self.cb)
        self.cb_obs.CheckItemChanged=self.check_change
        self.cb_obs.CheckItemDoubleClicked=self.doule_click

        self.icb=IconCheckBox(self,Rect(Point(20,90),70,30))
        self.icb.Show()
        self.icb_obs=CheckItemObserver(self.icb)
        self.icb_obs.CheckItemChanged=self.check_change
        self.icb_obs.CheckItemDoubleClicked=self.doule_click


        self.pcb=PushCheck(self,Rect(Point(20,130),120,30))
        self.pcb.SetText("PushCheck")
        self.pcb.Show()
        self.pcb_obs=CheckItemObserver(self.pcb)
        self.pcb_obs.CheckItemChanged=self.check_change
        self.pcb_obs.CheckItemDoubleClicked=self.doule_click

        self.ipc=IconPushCheck(self,Rect(Point(20,170),110,30))
        self.ipc.Show()
        self.ipc_obs=CheckItemObserver(self.ipc)
        self.ipc_obs.CheckItemChanged=self.check_change
        self.ipc_obs.CheckItemDoubleClicked=self.doule_click
        
        pass

    def check_change(self,sender,e):
        print '--check_change--'
        print type(sender)
        print type(e)
        print 'cur state:'+str(sender.IsChecked())
        pass
        
    def doule_click(self,sender,e):
        print '--doule_click--'
        pass
