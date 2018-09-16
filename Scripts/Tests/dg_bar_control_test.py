from ArchicadDG import *

class Form(Palette):
    def __init__(self):
        super(Form,self).__init__(Rect(Point(0,0),460,800))

        self.ss=SingleSpin(self,Rect(Point(10,10),160,40))
        self.ss.Show()
        self.ss.SetMin(0)
        self.ss.SetMax(100)
        self.ss_obs=BarControlObserver(self.ss)
        self.ss_obs.BarControlChanged=self.bar_change

        self.pie=PosIntEdit(self,Rect(Point(10,60),100,40))
        self.pie.Show()
        self.es=EditSpin(self,Rect(Point(130,60),100,40),self.pie)
        self.es.Show()
        
        self.sdr=Slider(self,Rect(Point(10,110),140,40),2,Slider.BottomRight)
        self.sdr.SetMin(0)
        self.sdr.SetMax(100)
        self.sdr.Show()
        self.sdr_obs=BarControlObserver(self.sdr)
        self.sdr_obs.BarControlChanged=self.bar_change

        self.sb=ScrollBar(self,Rect(Point(10,160),140,40))
        self.sb.SetMin(0)
        self.sb.SetMax(100)
        self.sb.Show()
        self.sb_obs=ScrollBarObserver(self.sb)
        self.sb_obs.ScrollBarChanged=self.scroll_change

        self.sb1=ScrollBar(self,Rect(Point(10,210),40,140),ScrollBar.Proportional)
        self.sb1.SetMin(0)
        self.sb1.SetMax(100)
        self.sb1.Show()
        self.sb1_obs=ScrollBarObserver(self.sb1)
        self.sb1_obs.ScrollBarChanged=self.scroll_change

        self.pb=ProgressBar(self,Rect(Point(10,360),140,30),ProgressBar.StaticFrame)
        self.pb.SetMin(0)
        self.pb.SetMax(100)
        self.pb.SetValue(24)
        self.pb.Show()
        pass

    def bar_change(self,sender,e):
        print '--bar_change--'
        print type(sender)
        print "value:"+str(sender.GetValue())
        self.pb.SetValue(sender.GetValue())

    def scroll_change(self,sender,e):
        print '--scroll_change--'
        print type(sender)
        print "value:"+str(sender.GetValue())
