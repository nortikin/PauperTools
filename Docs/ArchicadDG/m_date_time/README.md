### Example
* [demo](../../../Scripts/Tests/dg_datetime_test.py)

### Testing
```
import Tests.dg_datetime_test as datetime_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.frm=datetime_test.Form()
        self.frm.Show()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass

```

## Class List

* [DateTime](DateTime.md)
* [DateTimeObserver](DateTime_Observer.md)
* [DateControl](DateControl.md)
* [TimeControl](TimeControl.md)
* [CalendarControl](CalendarControl.md)


