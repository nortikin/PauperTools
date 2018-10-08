## ListViewObserver Class

### Parent Class
* [ItemObserver](../m_item/Item_Observer.md)

### Children Class
* None

### Import
```
from ArchicadDG import ListViewObserver
``` 

### Class Functions

* **constructor([ListView](ListView.md) sender)**
* Class constructor.

### Class Events

#### ListViewSelectionChanged([ListView](ListView.md) sender,ItemEvent e)
* 

#### ListViewContextMenuRequested([ListView](ListView.md) sender,ListViewContextMenuEvent e)
* **e.Position[[Point](../Point.md)]**:
* **e.Item[short]**:
* **e.Processed[Boolean]**:

#### ListViewMouseDown([ListView](ListView.md) sender,ListViewMouseDownEvent e)
* **e.IsHovered[Boolean]**:
* **e.ListItem[short]**:
* **e.Processed[Boolean]**:

#### ListViewDoubleClicked([ListView](ListView.md) sender,ListViewDoubleClickEvent e)
* **e.ListItem[short]**:

#### ListViewMouseMoved([ListView](ListView.md) sender,ListViewMouseMoveEvent e)
* **e.ListItem[short]**:

#### ListViewItemUpdate([ListView](ListView.md) sender,ListViewUpdateEvent e)
* **e.ListItem[short]**:
* **e.Width[short]**:
* **e.Height[short]**:
* **e.ImageRect[[Rect](../Rect.md)]**:

#### ListViewHoverStarted([ListView](ListView.md) sender,ListViewHoverEvent e)
* **e.ListItem[short]**:

#### ListViewHoverEnded([ListView](ListView.md) sender,ListViewHoverEvent e)
* **e.ListItem[short]**:

#### ListViewPressed([ListView](ListView.md) sender,ListViewPressedEvent e)
* **e.ListItem[short]**:

#### ListViewOverlayUpdate([ListView](ListView.md) sender,ListViewUpdateEvent e)
* **e.ListItem[short]**:
* **e.Width[short]**:
* **e.Height[short]**:
* **e.ImageRect[[Rect](../Rect.md)]**:
