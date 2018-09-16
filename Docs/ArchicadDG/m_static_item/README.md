### Example
* [demo](../../../Scripts/Tests/dg_static_test.py)

### Testing
```
import Tests.dg_static_test as static_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.frm=static_test.Form();
        self.frm.Show()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass

```

## Class List

* [StaticText](StaticText.md)
* [StaticTextObserver](StaticText_Observer.md)
* [CenterText](CenterText.md)
* [LeftText](LeftText.md)
* [RightText](PushRadio.md)
* [GroupBox](GroupBox.md)
* [Separator](Separator.md)

## Enum List
* [StaticText.VAlignType](StaticText_VAlignType.md)
* [StaticText.Truncation](StaticText_Truncation.md)
* [StaticText.FrameType](StaticText_FrameType.md)
* [GroupBox.GroupBoxType](GroupBox_GroupBoxType.md)