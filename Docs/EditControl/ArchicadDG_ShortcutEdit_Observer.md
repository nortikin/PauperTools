## ShortcutEditObserver Class

### Videos
* Youttube: https://youtu.be/d6qyalsb0Vs

### Parent Class
* [ItemObserver](../ArchicadDG_Item_Observer.md)

### Children Class
* None

### Import
```
from ArchicadDG import ShortcutEditObserver
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

* **constructor([ShortcutEdit](ArchicadDG_ShortcutEdit.md) shortcutEdit)**
* Class constructor.

### Class Events

#### ShortcutHit([ShortcutEdit](ArchicadDG_ShortcutEdit.md) shortcutEdit,ShortcutHitEvent e)
* **e.Key[[Key.Code](../ArchicadDG_Key_Code.md)]**:
* **e.ModifierFlags[ULong]**:
* Event handler for the shortcut hit notification.

