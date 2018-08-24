## IntEdit Class

### Edit Control Inheritance Diagram

<img src="../../Imgs/edit_control_inheritance_diagram.png" />

### Videos
* Youttube: https://youtu.be/d6qyalsb0Vs

### Parent Class
* [EditControl](ArchicadDG_EditControl.md)
* [ItemVariousProperty](../ArchicadDG_ItemVariousProperty.md)

### Children Class
* None

### Import
```
from ArchicadDG import IntEdit
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

* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect,[EditControl.FrameType](ArchicadDG_FrameType.md) frameType,[EditControl.AbsRelType](ArchicadDG_AbsRelType.md) absRelType,[EditControl.UpdateType](ArchicadDG_UpdateType.md) updateType,[EditControl.ReadOnlyType](ArchicadDG_ReadOnlyType.md) readOnlyType)**
* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect,[EditControl.FrameType](ArchicadDG_FrameType.md) frameType,[EditControl.AbsRelType](ArchicadDG_AbsRelType.md) absRelType,[EditControl.UpdateType](ArchicadDG_UpdateType.md) updateType)**
* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect,[EditControl.FrameType](ArchicadDG_FrameType.md) frameType,[EditControl.AbsRelType](ArchicadDG_AbsRelType.md) absRelType)**
* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect,[EditControl.FrameType](ArchicadDG_FrameType.md) frameType)**
* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect)**
* Class constructor.
-----

* **SetMin(Int32 min)**
* **None**
* Sets the minimal possible value.
-----

* **SetMax(Int32 max)**
* **None**
* Sets the maximal possible value.
-----

* **SetValue(Int32 val)**
* **None**
* Sets the current value.
-----

* **GetMin()**
* **Int32**
* Retrieves the minimal possible value.
-----

* **GetMax()**
* **Int32**
* Retrieves the maximal possible value.
-----

* **GetValue()**
* **Int32**
* Retrieves the current value.
-----