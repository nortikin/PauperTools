from ArchicadDG import *
from ArchicadGfx import *

class Form(Palette):
    def __init__(self):
        super(Form,self).__init__(Rect(Point(0,0),400,700))
        self.ct1=CenterText(self,Rect(Point(10,40),100,100),StaticText.ClientFrame)
        self.ct1.SetText("CenterText")
        self.ct1.SetBackgroundColor(Color.Red)
        self.ct1.Show()

        self.ct2=CenterText(self,Rect(Point(10,150),100,100),StaticText.NoFrame,StaticText.VCenter)
        self.ct2.SetText("CenterText")
        self.ct2.SetBackgroundColor(Color.Red)
        self.ct2.Show()

        self.ct3=CenterText(self,Rect(Point(10,260),100,100),StaticText.ModalFrame,StaticText.VBottom)
        self.ct3.SetText("CenterText")
        self.ct3.SetBackgroundColor(Color.Red)
        self.ct3.Show()

        self.lt1=LeftText(self,Rect(Point(120,40),100,100),StaticText.ModalFrame,StaticText.VBottom)
        self.lt1.SetText("LeftText")
        self.lt1.SetBackgroundColor(Color.Red)
        self.lt1.Show()

        self.lt2=LeftText(self,Rect(Point(120,150),100,100),StaticText.StaticFrame,StaticText.VCenter)
        self.lt2.SetText("LeftText")
        self.lt2.SetBackgroundColor(Color.Red)
        self.lt2.Show()

        self.lt3=LeftText(self,Rect(Point(120,260),100,100))
        self.lt3.SetText("LeftText")
        self.lt3.SetBackgroundColor(Color.Gray)
        self.lt3.SetTextColor(Color.Blue)
        self.lt3.Show()

        self.rt1=RightText(self,Rect(Point(230,40),100,100),StaticText.ModalFrame,StaticText.VBottom)
        self.rt1.SetText("RightText")
        self.rt1.SetBackgroundColor(Color.Red)
        self.rt1.Show()

        self.rt2=RightText(self,Rect(Point(230,150),100,100),StaticText.StaticFrame,StaticText.VCenter)
        self.rt2.SetText("RightText")
        self.rt2.SetBackgroundColor(Color.Red)
        self.rt2.Show()

        self.rt3=RightText(self,Rect(Point(230,260),100,100))
        self.rt3.SetText("RightText")
        self.rt3.SetBackgroundColor(Color.Gray)
        self.rt3.SetTextColor(Color.Blue)
        self.rt3_obs=StaticTextObserver(self.rt3)
        self.rt3_obs.StaticTextClicked=self.static_click
        self.rt3_obs.StaticTextDoubleClicked=self.static_double
        self.rt3_obs.StaticTextMouseMoved=self.static_move
        #self.rt3.EnableMouseMoveEvent()
        self.rt3.Show()

        self.gb1=GroupBox(self,Rect(Point(10,380),80,80),GroupBox.Primary)
        self.gb1.SetText("gb1")
        self.gb1.Show();

        self.gb2=GroupBox(self,Rect(Point(100,380),80,80),GroupBox.Secondary)
        self.gb2.SetText("gb2")
        self.gb2.Show();

        self.sp=Separator(self,Rect(Point(10,470),100,100))
        self.sp.Show()
        
        pass

    def static_click(self,sender,e):
        print '--static_click--'

    def static_double(self,sender,e):
        print '--static_double--'

    def static_move(self,sender,e):
        print '--static_move--'
