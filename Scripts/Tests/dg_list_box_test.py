from ArchicadDG import *
from ArchicadGfx import *

class Form(Palette):
    def __init__(self):
        super(Form,self).__init__(Rect(Point(0,0),600,900))

        self.btn=Button(self,Rect(Point(0,0),80,30))
        self.btn.Show()
        
        self.sslb=MultiSelListBox(self,Rect(Point(10,60),580,430),ListBox.HVScroll,ListBox.NoPartialItems,ListBox.Header,80,ListBox.Frame)
        
        self.sslb.SetHeaderSynchronState(True)
        self.sslb.SetHeaderPushableButtons(True)
        self.sslb.SetHeaderDragableButtons(True)
        self.sslb.SetHeaderItemCount(3)
        self.sslb.SetTabFieldCount(4)
        self.sslb.SetTabFieldBeginPosition(1,0)
        self.sslb.SetTabFieldEndPosition(1,120)
        self.sslb.SetTabFieldSeparator(1,True)
        self.sslb.SetTabFieldBeginPosition(2,120)
        self.sslb.SetTabFieldEndPosition(2,240)  
        #self.sslb.SetTabFieldStatus(2,False)
        self.sslb.SetTabFieldBeginPosition(3,240)
        self.sslb.SetTabFieldEndPosition(3,360)  
        #self.sslb.EnableHeaderButton()

        self.sslb.SetHeaderItemSizeableFlag(1,True)
        self.sslb.SetHeaderItemSizeableFlag(2,True)
        #self.sslb.SetHeaderItemSizeableFlag(3,True)
        #self.sslb.SetHeaderItemSize(1,120)
        #self.sslb.SetHeaderItemSize(2,120)
        #self.sslb.SetHeaderItemSize(3,120)

        self.sslb.SetHeaderItemArrowType(1,ListBox.Up)
        
        self.sslb.SetHeaderItemText(1,"header1")
        self.sslb.SetHeaderItemText(2,"header2")
        self.sslb.SetHeaderItemText(3,"header3")

        #self.sslb.SetHeaderSynchronState(True)
        
        self.sslb.AppendItem()
        self.sslb.SetTabItemText(1,1,"123")
        self.sslb.SetTabItemText(1,2,"423")
        self.sslb.SetTabItemText(1,3,"523")

        self.sslb.AppendItem()
        self.sslb.SetTabItemText(2,1,"2123")
        self.sslb.SetTabItemText(2,2,"2423")
        self.sslb.SetTabItemText(2,3,"2523")
        #self.sslb.DeleteItem(2)

        self.sslb.AppendItem()
        self.sslb.SetTabItemText(3,1,"3123")
        self.sslb.SetTabItemText(3,2,"3423")
        self.sslb.SetTabItemText(3,3,"3523")

        #self.sslb.GrayItem(2)
        #self.sslb.DisableItem(3)
        #self.sslb.SetItemOwnerDrawFlag(1,True)
        #self.sslb.InsertSeparator(2)
        print 'GetTabItemText:'+ self.sslb.GetTabItemText(1,1)
        self.sslb.SetTabItemBackgroundColor(1,1,Color.Red)
        self.sslb.SetTabItemBackgroundColor(1,2,Color.Blue)
        self.sslb.SetTabItemColor(1,3,Color.Green)
        print 'GetHeaderItemCount:'+str(self.sslb.GetHeaderItemCount())

        #self.sslb.SetOnTabItem(1,self.btn)
        self.sslb.EnableMouseMoveEvent()
        self.sslb.EnableHoverEvent()
        self.sslb.Show()

        self.sslb_obs=ListBoxObserver(self.sslb)
        self.sslb_obs.ListBoxSelectionChanged=self.sel_change
        self.sslb_obs.ListBoxClicked=self.click
        self.sslb_obs.ListBoxMouseDown=self.mouse_down
        self.sslb_obs.ListBoxContextMenuRequested=self.context_menu
        self.sslb_obs.ListBoxDoubleClicked=self.double_click
        #self.sslb_obs.ListBoxMouseMoved=self.mouse_move
        self.sslb_obs.ListBoxItemUpdate=self.item_update
        self.sslb_obs.ListBoxHoverStarted=self.hover_started
        self.sslb_obs.ListBoxHeaderItemClicked=self.header_click
        self.sslb_obs.ListBoxHeaderItemDragged=self.header_drag
        self.sslb_obs.ListBoxHeaderButtonClicked=self.header_btn_click
        pass

    def header_btn_click(self,sender,e):
        print '--header_btn_click--'
        print type(e)
        print dir(e)

    def header_drag(self,sender,e):
        print '--header_drag--'
        print type(e)
        print dir(e)
    
    def header_click(self,sender,e):
        print '--header_click--'
        print type(e)
        print dir(e)

    def hover_started(self,sender,e):
        print '--hover_started--'
        print type(e)
        print dir(e)

    def item_update(self,sender,e):
        print '--item_update--'
        print type(e)
        print dir(e)

    def mouse_move(self,sender,e):
        print '--mouse_move--'
        print type(e)
        print dir(e)

    def double_click(self,sender,e):
        print '--double_click--'
        print type(e)
        print dir(e)
    
    def sel_change(self,sender,e):
        print '--sel_change--'
        print type(e)
        print dir(e)

    def click(self,sender,e):
        print '--click--'
        print type(e)
        print dir(e)

    def mouse_down(self,sender,e):
        print '--mouse_down--'
        print type(e)
        print dir(e)

    def context_menu(self,sender,e):
        print '--context_menu--'
        print type(e)
        print dir(e)
