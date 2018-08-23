## Item Class

### Parent Class
* [ItemBase](ArchicadDG_ItemBase.md)

### Children Class
* [EditControl](EditControl/ArchicadDG_EditControl.md)
* [ButtonItem](Button/ArchicadDG_ButtonItem.md)

### Import
```
from ArchicadDG import Item
``` 

### Class Functions

* **operator!=**
* **Boolean**
* Operator != for Point objects.

```

```

* **operator==**
* **Boolean**
* Operator == for Point objects.

```

```

* **Show()**
* **None**
* Makes the item visible.
```

```


* **Hide()**
* **None**
* Hides the item.

```

```

* **SetVisibility(Boolean show)**
* **None**
* Sets the visibility state of the item.

```

```

* **IsVisible()**
* **Boolean**
* Checks the visibility state of the item.

```

```

* **Flash()**
* **None**
* Flash the item.

```

```

* **Enable()**
* **None**
* Enables the item.

```

```

* **Disable()**
* **None**
* Disables the item.

```

```

* **SetStatus(Boolean enable)**
* **None**
* Sets the enabled/disabled status of the item.

```

```

* **IsEnabled()**
* **Boolean**
* Checks if item is enabled or disabled.

```

```

* **Move(short hDisp,short vDisp)**
* **None**
* Moves the item.

```

```

* **Resize(short hGrow,short vGrow)**
* **None**
* Resizes the item.

```

```

* **MoveAndResize(short hDisp,short vDisp,short hGrow,short vGrow)**
* **None**
* Moves and resizes the item.

```

```

* **SetPosition([ArchicadDG.Point](ArchicadDG_Point.md) pt)**
* **None**
* Sets the item position.

```

```

* **SetPosition(short hPos,short vPos)**
* **None**
* Sets the item position.

```

```

* **SetRect([ArchicadDG.Rect](ArchicadDG_Rect.md) rect)**
* **None**
* Sets the bounding rectangle of the item.

```

```

* **SetSize(short width,short height)**
* **None**
* Sets the size of the item.

```

```

* **SetWidth(short width)**
* **None**
* Sets the width of the item.

```

```

* **SetHeight(short height)**
* **None**
* Sets the height of the item.

```

```

* **GetPosition()**
* **[ArchicadDG.Point](ArchicadDG_Point.md)**
* Retrieves the position of the item.

```

```

* **GetRect()**
* **[ArchicadDG.Rect](ArchicadDG_Rect.md)**
* Retrieves the bounding rectangle of the item.

```

```
* **GetWidth()**
* **short**
* Retrieves the width of the item.

```

```
* **GetHeight()**
* **short**
* Retrieves the heigth of the item.

```

```
* **GetNativeRectInScreenSpace()**
* **[ArchicadDG.Rect](ArchicadDG_Rect.md)**
* Retrieves native rect in screen space of the item.

```

```
* **Invalidate()**
* **None**
* Invalidates the item.

```

```
* **Redraw()**
* **None**
* Redraws the item immediately.

```

```
* **ResetModified()**
* **None**
* Resets the modified flag of the item.

```

```
* **IsModified()**
* **Boolean**
* Checks if the item was modified or not.

```

```
* **SetHelp(short helpIndex)**
* **None**
* Sets the help index of the item.

```

```
* **GetTooltipString()**
* **string**
* Reads tooltip text of the dialog item from 'DLGH' resource.

```

```
* **GetAnchorString()**
* **string**
* Reads anchor string of the dialog item from 'DLGH' resource.

```

```
* **InvokeDragDrop()**
* **None**
* Starts a drag and drop operation.

```

```
* **GetResolutionFactor()**
* **double**
* Retrieves the resolution factor of the item.

```

```
* **GetScaleFactor()**
* **double**
* Retrieves the scale factor of the item.

```

```