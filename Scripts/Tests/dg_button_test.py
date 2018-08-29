from ArchicadDG import *

class FormPalette(object):
    def __init__(self):
        self.pal=Palette(Rect(Point(0,0),500,560))

        self.btn_one=Button(self.pal,Rect(Point(100,100),120,80))
        self.btn_one.SetText("BtnOne")
        self.btn_one.SetFontSize(Font.Large)
        self.btn_one_obs=ButtonItemObserver(self.btn_one)
        self.btn_one_obs.ButtonClicked=self.btn_clicked
        self.btn_one.Show()


        self.spl_btn=SplitButton(self.pal,Rect(Point(100,220),120,40))
        self.spl_btn.SetText("SplBtn")

        self.spl_btn.AppendItem("item1")#1
        self.spl_btn.AppendItem("item2")#2
        self.spl_btn.AppendSeparator()#3
        self.spl_btn.AppendItem("item3")#4
        #self.spl_btn.DisableItem(2)

        self.spl_btn_obs1=ButtonItemObserver(self.spl_btn)
        self.spl_btn_obs1.ButtonClicked=self.btn_clicked

        self.spl_btn_obs2=SplitButtonObserver(self.spl_btn)
        self.spl_btn_obs2.SplitButtonPopupChanged=self.popup_changed
        self.spl_btn.Show()
        self.pal.Show()
        pass

    def btn_clicked(self,sender,e):
        print '--btn_clicked--'
        print type(sender)
        print type(e)

    def popup_changed(self,sender,e):
        print '--popup_changed--'
        print type(sender)
        print 'selected index:'+str(sender.GetSelectedItem())
        print 'selected item:'+sender.GetItemText(sender.GetSelectedItem())
