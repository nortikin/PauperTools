## IntEdit Class

### Parent Class
* [EditControl](EditControl.md)
* [ItemVariousProperty](../m_item/ItemVariousProperty.md)

### Children Class
* None

### Import
```
from ArchicadDG import IntEdit
``` 

### Class Functions

* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect,[EditControl.FrameType](EditControl_FrameType.md) frameType,[EditControl.AbsRelType](EditControl_AbsRelType.md) absRelType,[EditControl.UpdateType](EditControl_UpdateType.md) updateType,[EditControl.ReadOnlyType](EditControl_ReadOnlyType.md) readOnlyType)**
* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect,[EditControl.FrameType](EditControl_FrameType.md) frameType,[EditControl.AbsRelType](EditControl_AbsRelType.md) absRelType,[EditControl.UpdateType](EditControl_UpdateType.md) updateType)**
* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect,[EditControl.FrameType](EditControl_FrameType.md) frameType,[EditControl.AbsRelType](EditControl_AbsRelType.md) absRelType)**
* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect,[EditControl.FrameType](EditControl_FrameType.md) frameType)**
* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect)**
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