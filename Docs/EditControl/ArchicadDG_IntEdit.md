## IntEdit Class

### Edit Control Inheritance Diagram

<img src="../../Imgs/edit_control_inheritance_diagram.png" />

### Videos
* Youttube: 
* XiGua: 

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
* Waiting for improvement

### Testing
* Waiting for improvement

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