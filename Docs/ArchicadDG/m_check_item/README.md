### Example
* [demo](../../../Scripts/Tests/dg_button_test.py)

### Testing
```

import Tests.dg_check_test as check_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.frm=check_test.Form()
        self.frm.Show()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass

```

## Class List

* [CheckItem](CheckItem.md)
* [CheckItemObserver](CheckItem_Observer.md)
* [CheckBox](CheckBox.md)
* [IconCheckBox](IconCheckBox.md)
* [PushCheck](PushCheck.md)
* [IconPushCheck](IconPushCheck.md)

## Enum List

* [PushCheck.ButtonForm](PushCheck_ButtonForm.md)
* [PushCheck.FrameType](PushCheck_FrameType.md)
* [PushCheck.Alignment](PushCheck_Alignment.md)
* [PushCheck.ArrowType](PushCheck_ArrowType.md)
* [IconPushCheck.ButtonForm](IconPushCheck_ButtonForm.md)
* [IconPushCheck.FrameType](IconPushCheck_FrameType.md)
