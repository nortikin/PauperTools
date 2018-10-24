## PushMenuObserver Class

### Parent Class
* [ItemObserver](../m_item/Item_Observer.md)

### Children Class
* None

### Import
```
from ArchicadDG import PushMenuObserver
``` 

### Class Functions

* **constructor([PushMenu](PushMenu.md) sender)**
* Class constructor.

### Class Events

#### PushMenuChanged([PushMenu](PushMenu.md) sender,PushMenuCheckChangeEvent e)
* **e.WasStateChange[Boolean]**:
* **e.PreviousMenuItem[short]**:

#### PushMenuChanged([PushMenu](PushMenu.md) sender,PushMenuRadioChangeEvent e)
* **e.WasSelectionChange[Boolean]**:
* **e.PreviousMenuItem[short]**:
* **e.PreviousGroupSelection[[Item](../m_item/Item.md)]**:

#### PushMenuDoubleClicked([PushMenu](PushMenu.md) sender,ItemEvent e)


