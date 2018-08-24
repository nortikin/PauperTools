## IntEditObserver Class

### Videos
* Youttube: https://youtu.be/d6qyalsb0Vs

### Parent Class
* [ItemObserver](../ArchicadDG_Item_Observer.md)
* [EditDragSourceObserver](ArchicadDG_EditDragSource_Observer.md)
* [EditDropTargetObserver](ArchicadDG_EditDropTarget_Observer.md)

### Children Class
* None

### Import
```
from ArchicadDG import IntEditObserver
``` 

### Example
* [demo](../../Scripts/Tests/dg_edit_test.py)

### Testing
```
import Tests.dg_edit_test as edit_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        #new Form
        self.frm=edit_test.PaletteForm()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        #free Form
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass

```

### Class Functions

* **constructor([IntEdit](ArchicadDG_IntEdit.md) intEdit)**
* Class constructor.

### Class Events

#### IntEditChanged([IntEdit](ArchicadDG_IntEdit.md) intEdit,IntEditChangeEvent e)
* **e.PreviousValue[Int32]**:Retrieves the value before the change event.
* **e.WasRelativeInput[Boolean]**:
* Event handler for the pos int edit changed notification.

