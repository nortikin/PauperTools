## RealEditObserver Class

### Parent Class
* [ItemObserver](../m_item/Item_Observer.md)
* [EditDragSourceObserver](EditDragSource_Observer.md)
* [EditDropTargetObserver](EditDropTarget_Observer.md)

### Children Class
* None

### Import
```
from ArchicadDG import RealEditObserver
``` 

### Class Functions

* **constructor([RealEdit](RealEdit.md) realEdit)**
* Class constructor.

### Class Events

#### RealEditChanged([RealEdit](RealEdit.md) realEdit,RealEditChangeEvent e)
* **e.PreviousValue[double]**:Retrieves the value before the change event.
* **e.WasRelativeInput[Boolean]**:
* Event handler for the real edit changed notification.

