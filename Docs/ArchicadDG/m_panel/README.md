## Form Inheritance Diagram

<img src="../../../Imgs/form_inheritance_diagram.png" width="384px" height="384px" />

## Panel Observer 

### Videos
* Youttube: https://youtu.be/khoufTCvBdY
* XiGua: https://url.cn/5MioU8r

### Example
* [panel observer](../../../Scripts/Tests/dg_panel_observer_test.py)

### Testing
```
import Tests.dg_panel_observer_test as PanelObserver

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.pal=PanelObserver.FormPalette()
        self.pal.Show()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.pal=None
        print 'PyMain.FreeData' #must be print this message
        pass
        
```

## Class List

* [Panel](Panel.md)
* [PanelObserver](Panel_Observer.md) 