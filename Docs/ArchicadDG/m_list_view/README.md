### Example
* [demo](../../../Scripts/Tests/dg_list_view_test.py)

### Testing
```
import Tests.dg_list_view_test as list_view_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.frm=list_view_test.Form()
        self.frm.Show()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass

```

## Class List

* [ListView](ListView.md)
* [ListViewObserver](ListView_Observer.md)
* [SingleSelListView](SingleSelListView.md)
* [MultiSelListView](MultiSelListView.md)


## Enum List
* [ListView.Background](ListView_Background.md)
* [ListView.FrameType](ListView_FrameType.md)
* [ListView.HelpStyle](ListView_HelpStyle.md)
* [ListView.ImageType](ListView_ImageType.md)
* [ListView.ItemType](ListView_ItemType.md)
* [ListView.ScrollType](ListView_ScrollType.md)
* [ListView.SelectionStyle](ListView_SelectionStyle.md)
* [ListView.ViewMode](ListView_ViewMode.md)