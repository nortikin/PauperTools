## ListBoxObserver Class

### Parent Class
* [ItemObserver](../m_item/Item_Observer.md)

### Children Class
* None

### Import
```
from ArchicadDG import ListBoxObserver
``` 

### Class Functions

* **constructor([ListBox](ListBox.md) sender)**
* Class constructor.

### Class Events

#### ListBoxSelectionChanged([ListBox](ListBox.md) sender,ItemEvent e)
* 

#### ListBoxItemDragged([ListBox](ListBox.md) sender,ListBoxDragEvent e)
* **e.PreviousIndex[short]**:
* **e.NewIndex[short]**:

#### ListBoxClicked([ListBox](ListBox.md) sender,ListBoxEvent e)
* **e.ListItem[short]**:
* **e.MouseOffset[[Point](../Point.md)]**:
* **e.IsCommandPressed[Boolean]**:
* **e.IsOptionPressed[Boolean]**:
* **e.IsShiftPressed[Boolean]**:

#### ListBoxMouseDown([ListBox](ListBox.md) sender,ListBoxMouseDownEvent e)
* **e.IsHovered[Boolean]**:
* **e.ListItem[short]**:
* **e.MouseOffset[[Point](../Point.md)]**:
* **e.IsCommandPressed[Boolean]**:
* **e.IsOptionPressed[Boolean]**:
* **e.IsShiftPressed[Boolean]**:
* **e.Processed[Boolean]**:

#### ListBoxContextMenuRequested([ListBox](ListBox.md) sender,ListBoxContextMenuEvent e)
* **e.Position[[Point](../Point.md)]**:
* **e.Item[short]**:
* **e.HeaderItem[short]**:
* **e.IsInHeaderButton[Boolean]**:
* **e.Processed[Boolean]**:

#### ListBoxDoubleClicked([ListBox](ListBox.md) sender,ListBoxEvent e)
* **e.ListItem[short]**:
* **e.MouseOffset[[Point](../Point.md)]**:
* **e.IsCommandPressed[Boolean]**:
* **e.IsOptionPressed[Boolean]**:
* **e.IsShiftPressed[Boolean]**:

#### ListBoxMouseMoved([ListBox](ListBox.md) sender,ListBoxMouseMoveEvent e)
* **e.ListItem[short]**:
* **e.MouseOffset[[Point](../Point.md)]**:
* **e.IsCommandPressed[Boolean]**:
* **e.IsOptionPressed[Boolean]**:
* **e.IsShiftPressed[Boolean]**:
* **e.InArea[short]**:

#### ListBoxItemUpdate([ListBox](ListBox.md) sender,ListBoxItemUpdateEvent e)
* **e.ListItem[short]**:
* **e.Width[short]**:
* **e.Height[short]**:
* **e.IsUpdatedListItemHighlighted[Boolean]**:
* **e.ForeColor[[ArchicadGfx.Color](../../ArchicadGfx/Color.md)]**:
* **e.BackColor[[ArchicadGfx.Color](../../ArchicadGfx/Color.md)]**:

#### ListBoxTabFieldUpdate([ListBox](ListBox.md) sender,ListBoxTabItemUpdateEvent e)
* **e.ListItem[short]**:
* **e.TabFieldIndex[short]**:
* **e.Width[short]**:
* **e.Height[short]**:
* **e.IsUpdatedListItemHighlighted[Boolean]**:
* **e.TabItemText[string]**:
* **e.ForeColor[[ArchicadGfx.Color](../../ArchicadGfx/Color.md)]**:
* **e.BackColor[[ArchicadGfx.Color](../../ArchicadGfx/Color.md)]**:

#### ListBoxHoverStarted([ListBox](ListBox.md) sender,ListBoxHoverEvent e)
* **e.ListItem[short]**:

#### ListBoxHoverEnded([ListBox](ListBox.md) sender,ListBoxHoverEvent e)
* **e.ListItem[short]**:

#### ListBoxOverlayUpdate([ListBox](ListBox.md) sender,ListBoxItemUpdateEvent e)
* **e.ListItem[short]**:
* **e.Width[short]**:
* **e.Height[short]**:
* **e.IsUpdatedListItemHighlighted[Boolean]**:
* **e.ForeColor[[ArchicadGfx.Color](../../ArchicadGfx/Color.md)]**:
* **e.BackColor[[ArchicadGfx.Color](../../ArchicadGfx/Color.md)]**:
* **e.ImageRect[[Rect](../Rect.md)]**:

#### ListBoxHeaderItemClicked([ListBox](ListBox.md) sender,ListBoxHeaderItemClickEvent e)
* **e.HeaderItem[short]**:

#### ListBoxHeaderItemDragged([ListBox](ListBox.md) sender,ListBoxHeaderItemDragEvent e)
* **e.OldPos[short]**:
* **e.NewPos[short]**:

#### ListBoxHeaderButtonClicked([ListBox](ListBox.md) sender,ItemEvent e)
* 