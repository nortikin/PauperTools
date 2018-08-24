## ShortcutEdit Class

### Edit Control Inheritance Diagram

<img src="../../Imgs/edit_control_inheritance_diagram.png" />

### Videos
* Youttube: https://youtu.be/d6qyalsb0Vs

### Parent Class
* [TextEditBase](ArchicadDG_TextEditBase.md)
* [ItemTextLengthLimitProperty](../ArchicadDG_ItemTextLengthLimitProperty.md)

### Children Class
* None

### Import
```
from ArchicadDG import ShortcutEdit
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

* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect,short lengthLimit,[EditControl.FrameType](ArchicadDG_FrameType.md) frameType,[EditControl.UpdateType](ArchicadDG_UpdateType.md) updateType)**
* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect,short lengthLimit,[EditControl.FrameType](ArchicadDG_FrameType.md) frameType)**
* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect,short lengthLimit)**
* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect)**
* Class constructor.
-----