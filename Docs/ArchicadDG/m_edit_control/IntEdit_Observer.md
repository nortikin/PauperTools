## IntEditObserver Class

### Parent Class
* [ItemObserver](../m_item/Item_Observer.md)
* [EditDragSourceObserver](EditDragSource_Observer.md)
* [EditDropTargetObserver](EditDropTarget_Observer.md)

### Children Class
* None

### Import
```
from ArchicadDG import IntEditObserver
``` 

### Class Functions

* **constructor([IntEdit](IntEdit.md) intEdit)**
* Class constructor.

### Class Events

#### IntEditChanged([IntEdit](IntEdit.md) intEdit,IntEditChangeEvent e)
* **e.PreviousValue[Int32]**:Retrieves the value before the change event.
* **e.WasRelativeInput[Boolean]**:
* Event handler for the pos int edit changed notification.

