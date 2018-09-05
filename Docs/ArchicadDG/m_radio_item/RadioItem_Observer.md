## RadioItemObserver Class

### Parent Class
* [ItemObserver](../m_item/Item_Observer.md)
* [RadioDragSourceObserver](RadioDragSource_Observer.md)
* [RadioDropTargetObserver](RadioDropTarget_Observer.md)


### Children Class
* None

### Import
```
from ArchicadDG import RadioItemObserver
``` 

### Class Functions

* **constructor([RadioItem](RadioItem.md) item)**
* Class constructor.

### Class Events

#### RadioItemChanged([RadioItem](RadioItem.md) sender,RadioItemChangeEvent e)
* **e.PreviousGroupSelection[[Item](../m_item/Item.md)]**:
* Event handler for the radio item changed notification.

#### RadioItemDoubleClicked([RadioItem](RadioItem.md) sender,ItemEvent e)
* Event handler for the radio item double clicked notification.