## PosIntEditObserver Class

### Parent Class
* [ItemObserver](../m_item/Item_Observer.md)
* [EditDragSourceObserver](EditDragSource_Observer.md)
* [EditDropTargetObserver](EditDropTarget_Observer.md)

### Children Class
* None

### Import
```
from ArchicadDG import PosIntEditObserver
``` 

### Class Functions

* **constructor([PosIntEdit](PosIntEdit.md) posIntEdit)**
* Class constructor.

### Class Events

#### PosIntEditChanged([PosIntEdit](PosIntEdit.md) posIntEdit,PosIntEditChangeEvent e)
* **e.PreviousValue[UInt32]**:Retrieves the value before the change event.
* **e.WasRelativeInput[Boolean]**:
* Event handler for the pos int edit changed notification.

