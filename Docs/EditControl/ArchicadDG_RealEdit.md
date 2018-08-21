## RealEdit Class

### Edit Control Inheritance Diagram

<img src="../../Imgs/edit_control_inheritance_diagram.png" />

### Videos
* Youttube: 
* XiGua: 

### Parent Class
* [EditControl](ArchicadDG_EditControl.md)
* [ItemVariousProperty](../ArchicadDG_ItemVariousProperty.md)

### Children Class
* [LengthEdit](ArchicadDG_LengthEdit.md)
* [AngleEdit](ArchicadDG_AngleEdit.md)
* [PolarAngleEdit](ArchicadDG_PolarAngleEdit.md)
* [MMPointEdit](ArchicadDG_MMPointEdit.md)

### Import
```
from ArchicadDG import RealEdit
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

* **SetMin(double min)**
* **None**
* Sets the minimal possible value.
-----

* **SetMax(double max)**
* **None**
* Sets the maximal possible value.
-----

* **SetValue(double val)**
* **None**
* Sets the current value.
-----

* **GetMin()**
* **double**
* Retrieves the minimal possible value.
-----

* **GetMax()**
* **double**
* Retrieves the maximal possible value.
-----

* **GetValue()**
* **double**
* Retrieves the current value.
-----