### Example
* [demo](../../../Scripts/Tests/dg_popup_test.py)

### Testing
```
import Tests.dg_popup_test as popup_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.frm=popup_test.Form();
        self.frm.Show()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass

```

## Class List

* [PopUp](PopUp.md)
* [PopUpObserver](PopUp_Observer.md)

