
from ArchicadDG import *

class Form(object):
    def __init__(self):
        self.group_one=1
        self.frm=Palette(Rect(Point(0,0),400,500))
        self.rdb_one_one=RadioButton(self.frm,Rect(Point(30,50),100,30),self.group_one)
        self.rdb_one_one_obs=RadioItemObserver(self.rdb_one_one)
        self.rdb_one_one_obs.RadioItemChanged=self.radio_item_change
        self.rdb_one_one_obs.RadioItemDoubleClicked=self.radio_item_double_clicked
        self.rdb_one_one_obs.Changed=self.item_clicked
        self.rdb_one_one.SetText("rdb one")
        self.rdb_one_one.Show()

        self.rdb_one_two=IconRadioButton(self.frm,Rect(Point(30,80),100,30),self.group_one)
        self.rdb_one_two_obs=RadioItemObserver(self.rdb_one_two)
        self.rdb_one_two_obs.RadioItemChanged=self.radio_item_change
        self.rdb_one_two_obs.RadioItemDoubleClicked=self.radio_item_double_clicked
        self.rdb_one_two_obs.Changed=self.item_clicked
        self.rdb_one_two.Show()

        self.rdb_one_three=PushRadio(self.frm,Rect(Point(30,110),100,30),self.group_one)
        self.rdb_one_three_obs=RadioItemObserver(self.rdb_one_three)
        self.rdb_one_three_obs.RadioItemChanged=self.radio_item_change
        self.rdb_one_three_obs.RadioItemDoubleClicked=self.radio_item_double_clicked
        self.rdb_one_three_obs.Changed=self.item_clicked
        self.rdb_one_three.SetText("rdb three")
        self.rdb_one_three.Show()

        self.rdb_one_four=IconPushRadio(self.frm,Rect(Point(30,140),100,30),self.group_one)
        self.rdb_one_four_obs=RadioItemObserver(self.rdb_one_four)
        self.rdb_one_four_obs.RadioItemChanged=self.radio_item_change
        self.rdb_one_four_obs.RadioItemDoubleClicked=self.radio_item_double_clicked
        self.rdb_one_four_obs.Changed=self.item_clicked
        self.rdb_one_four.Show()

        self.frm.Show()     
        pass

    def radio_item_change(self,sender,e):
        print '--radio_item_change--'
        print type(sender)
        print type(e)
        print "prev:"+str(type(e.PreviousGroupSelection))

    def radio_item_double_clicked(self,sender,e):
        print '--radio_item_double_clicked--'
        print type(sender)
        print type(e)

    def item_clicked(self,sender,e):
        print '--item_clicked--'
        print type(sender)
        print type(e)

