### Example
* [demo](../../../Scripts/Tests/dg_list_box_test.py)

### Testing
```
import Tests.dg_list_box_test as list_box_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.frm=list_box_test.Form()
        self.frm.Show()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass

```

## Class List

* [ListBox](ListBox.md)
* [ListBoxObserver](ListBox_Observer.md)
* [SingleSelListBox](SingleSelListBox.md)
* [MultiSelListBox](MultiSelListBox.md)


## Enum List
* [ListBox.ArrowType](ListBox_ArrowType.md)
* [ListBox.FrameType](ListBox_FrameType.md)
* [ListBox.HeaderFlag](ListBox_HeaderFlag.md)
* [ListBox.HelpStyle](ListBox_HelpStyle.md)
* [ListBox.ItemStatus](ListBox_ItemStatus.md)
* [ListBox.ItemType](ListBox_ItemType.md)
* [ListBox.Justification](ListBox_Justification.md)
* [ListBox.PartialItemType](ListBox_PartialItemType.md)
* [ListBox.ScrollType](ListBox_ScrollType.md)
* [ListBox.SpecialArea](ListBox_SpecialArea.md)
* [ListBox.SpecialIcons](ListBox_SpecialIcons.md)
* [ListBox.Truncation](ListBox_Truncation.md)