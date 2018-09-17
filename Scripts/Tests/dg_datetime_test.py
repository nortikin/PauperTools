from ArchicadDG import *

class Form(Palette):
    def __init__(self):
        super(Form,self).__init__(Rect(Point(0,0),400,500))

        self.dc=DateControl(self,Rect(Point(10,10),150,40))
        self.dc.Show()
        self.dc_obs=DateTimeObserver(self.dc)
        self.dc_obs.DateTimeChanged=self.change


        self.tc=TimeControl(self,Rect(Point(10,60),150,40))
        self.tc.Show()
        self.tc_obs=DateTimeObserver(self.tc)
        self.tc_obs.DateTimeChanged=self.change

        self.cc=CalendarControl(self,Rect(Point(10,110),150,40))
        self.cc.Show()
        self.cc_obs=DateTimeObserver(self.cc)
        self.cc_obs.DateTimeChanged=self.change
        pass

    def change(self,sender,e):
        print '--change--'
        print 'pre:'+str(e.PreviousTime)
        print 'val:'+str(sender.GetValue())
