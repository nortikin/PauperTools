## RealEdit Class

### Parent Class
* [EditControl](EditControl.md)
* [ItemVariousProperty](../m_item/ItemVariousProperty.md)

### Children Class
* [LengthEdit](LengthEdit.md)
* [AngleEdit](AngleEdit.md)
* [PolarAngleEdit](PolarAngleEdit.md)
* [MMPointEdit](MMPointEdit.md)

### Import
```
from ArchicadDG import RealEdit
``` 

### Class Functions

* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect,[EditControl.FrameType](EditControl_FrameType.md) frameType,[EditControl.AbsRelType](EditControl_AbsRelType.md) absRelType,[EditControl.UpdateType](EditControl_UpdateType.md) updateType,[EditControl.ReadOnlyType](EditControl_ReadOnlyType.md) readOnlyType)**
* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect,[EditControl.FrameType](EditControl_FrameType.md) frameType,[EditControl.AbsRelType](EditControl_AbsRelType.md) absRelType,[EditControl.UpdateType](EditControl_UpdateType.md) updateType)**
* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect,[EditControl.FrameType](EditControl_FrameType.md) frameType,[EditControl.AbsRelType](EditControl_AbsRelType.md) absRelType)**
* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect,[EditControl.FrameType](EditControl_FrameType.md) frameType)**
* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect)**
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