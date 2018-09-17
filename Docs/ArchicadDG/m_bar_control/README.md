### Example
* [demo](../../../Scripts/Tests/dg_bar_control_test.py)

### Testing
```
import Tests.dg_bar_control_test as bar_control_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.frm=bar_control_test.Form()
        self.frm.Show()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass

```

## Class List

* [BarControl](BarControl.md)
* [BarControlObserver](BarControl_Observer.md)
* [SingleSpin](SingleSpin.md)
* [EditSpin](EditSpin.md)
* [Slider](Slider.md)
* [ScrollBar](ScrollBar.md)
* [ScrollBarObserver](ScrollBar_Observer.md)
* [ProgressBar](ProgressBar.md)

## Enum List
* [ScrollBar.ThumbType](ScrollBar_ThumbType.md)
* [ScrollBar.FocusableType](ScrollBar_FocusableType.md)
* [ScrollBar.AutoScrollType](ScrollBar_AutoScrollType.md)
* [ProgressBar.FrameType](ProgressBar_FrameType.md)