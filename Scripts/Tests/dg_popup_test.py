from ArchicadDG import *
from ArchicadGS import *

class Form(Palette):
    def __init__(self):
        super(Form,self).__init__(Rect(Point(0,0),200,300))

        self.pop=PopUp(self,Rect(Point(10,10),120,30),150,20)
        self.pop.AppendItem()
        self.pop.SetItemText(1,"Item1")
        self.pop.AppendItem()
        self.pop.SetItemText(2,"Item2")
        self.pop.Show()

        self.pop_obs=PopUpObserver(self.pop)
        self.pop_obs.PopUpChanged=self.pop_change

        help(GSCharCode)
    def pop_change(self,sender,e):
        print type(e)
        print str(e.PreviousSelection)
        print str(sender.GetItemCharCode(sender.GetSelectedItem()))
        #help(sender)
