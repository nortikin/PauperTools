## Dialog Class

### Parent Class
[Panel](ArchicadDG_Panel.md)

### Children Class
[ModalDialog](ArchicadDG_ModalDialog.md)
[ModelessBase](ArchicadDG_ModelessBase.md)

### Import
```
from ArchicadDG import Dialog
``` 

### Class Functions

* **constructor([Dialog.DialogType](ArchicadDG_DialogType.md) dialType,[Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.MinimizeType](ArchicadDG_MinimizeType.md) minimizeType,[Dialog.MaximizeType](ArchicadDG_MaximizeType.md) maximizeType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType,[Dialog.FrameType](ArchicadDG_FrameType.md) frameType,[Dialog.SpecialFeatures](ArchicadDG_SpecialFeatures.md) specialFeatures)**
* **constructor([Dialog.DialogType](ArchicadDG_DialogType.md) dialType,[Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.MinimizeType](ArchicadDG_MinimizeType.md) minimizeType,[Dialog.MaximizeType](ArchicadDG_MaximizeType.md) maximizeType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType,[Dialog.FrameType](ArchicadDG_FrameType.md) frameType)**
* **constructor([Dialog.DialogType](ArchicadDG_DialogType.md) dialType,[Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.MinimizeType](ArchicadDG_MinimizeType.md) minimizeType,[Dialog.MaximizeType](ArchicadDG_MaximizeType.md) maximizeType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType)**
* **constructor([Dialog.DialogType](ArchicadDG_DialogType.md) dialType,[Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.MinimizeType](ArchicadDG_MinimizeType.md) minimizeType,[Dialog.MaximizeType](ArchicadDG_MaximizeType.md) maximizeType)**
* **constructor([Dialog.DialogType](ArchicadDG_DialogType.md) dialType,[Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.MinimizeType](ArchicadDG_MinimizeType.md) minimizeType)**
* **constructor([Dialog.DialogType](ArchicadDG_DialogType.md) dialType,[Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType)**
* **constructor([Dialog.DialogType](ArchicadDG_DialogType.md) dialType,[Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType)**
* **constructor([Dialog.DialogType](ArchicadDG_DialogType.md) dialType,[Rect](ArchicadDG_Rect.md) rect)**
* Class constructor.
```
```

* **GetDialogType()**
* **[Dialog.DialogType](ArchicadDG_DialogType.md)**
* Retrieves the type of the dialog.
```

```


* **Center()**
* **None**
* Positions the dialog to the center of the screen or the application's client window.

```

```

* **Move(short hDisp,short vDisp)**
* **None**
* Moves the dialog with the given relative values.

```

```

* **Resize(short hGrow,short vGrow,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint,bool keepOld)**
* **short**
* Resizes the dialog with the given relative values.

```

```

* **Resize(short hGrow,short vGrow,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint)**
* **short**
* Resizes the dialog with the given relative values.

```

```

* **Resize(short hGrow,short vGrow)**
* **short**
* Resizes the dialog with the given relative values.

```

```

* **SetGrowType([Dialog.GrowType](ArchicadDG_GrowType.md) growType)**
* **None**
* Sets the grow type of the dialog.
```

```

* **GetGrowType()**
* **[Dialog.GrowType](ArchicadDG_GrowType.md)**
* Retrieves the grow type of the dialog.
```

```

* **GetOriginalClientWidth()**
* **short**
* Retrieves the original client area width of the dialog.
```

```

* **GetOriginalClientHeight()**
* **short**
* Retrieves the original client area height of the dialog.
```

```

* **SetMinClientSize(short minWidth,short minHeight)**
* **None**
* Sets the allowed minimal size of the client area.
```

```

* **SetMinClientWidth(short minWidth)**
* **None**
* Sets the allowed minimal width of the client area.
```

```

* **SetMinClientHeight(short minHeight)**
* **None**
* Sets the allowed minimal height of the client area.
```

```

* **GetMinClientWidth()**
* **short**
* Retrieves the allowed minimal width of the client area.
```

```

* **GetMinClientHeight()**
* **short**
* Retrieves the allowed minimal height of the client area.
```

```

* **SetClientPosition([Point](ArchicadDG_Point.md) pt)**
* **None**
* Sets the client area position.
```

```

* **SetClientPosition(short hPos,short vPos)**
* **None**
* Sets the client area position.
```

```

* **SetClientRect([Rect](ArchicadDG_Rect.md) rect,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint,bool keepOld)**
* **None**
* Sets the client area rectangle.
```

```

* **SetClientRect([Rect](ArchicadDG_Rect.md) rect,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint)**
* **None**
* Sets the client area rectangle.
```

```

* **SetClientRect([Rect](ArchicadDG_Rect.md) rect)**
* **None**
* Sets the client area rectangle.
```

```

* **SetClientSize(short width,short height,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint,bool keepOld)**
* **None**
* Sets the client area size.
```

```

* **SetClientSize(short width,short height,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint)**
* **None**
* Sets the client area size.
```

```

* **SetClientSize(short width,short height)**
* **None**
* Sets the client area size.
```

```

* **SetClientWidth(short width,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint,bool keepOld)**
* **None**
* Sets the client area width.
```

```

* **SetClientWidth(short width,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint)**
* **None**
* Sets the client area width.
```

```

* **SetClientWidth(short width)**
* **None**
* Sets the client area width.
```

```

* **SetClientHeight(short height,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint,bool keepOld)**
* **None**
* Sets the client area height.
```

```

* **SetClientHeight(short height,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint)**
* **None**
* Sets the client area height.
```

```

* **SetClientHeight(short height)**
* **None**
* Sets the client area height.
```

```

* **GetClientPosition()**
* **[Point](ArchicadDG_Point.md)**
* Retrieves the client area position.
```

```

* **GetClientRect()**
* **[Rect](ArchicadDG_Rect.md)**
* Retrieves the client area rectangle.
```

```

* **GetClientWidth()**
* **short**
* Retrieves the client area width.
```

```

* **GetClientHeight()**
* **short**
* Retrieves the client area height.
```

```

* **GetOriginalFrameWidth()**
* **short**
* Retrieves the original frame width of the dialog.
```

```

* **GetOriginalFrameHeight()**
* **short**
* Retrieves the original frame height of the dialog.
```

```

* **SetMinFrameHeight(short minHeight)**
* **None**
* Sets the allowed minimal height of the dialog frame rectangle.
```

```

* **GetMinFrameWidth()**
* **short**
* Retrieves the allowed minimal width of the dialog frame rectangle.
```

```

* **GetMinFrameHeight()**
* **short**
* Retrieves the allowed minimal height of the dialog frame rectangle.
```

```

* **SetFramePosition([Point](ArchicadDG_Point.md) pt)**
* **None**
* Sets the position of the dialog frame rectangle.
```

```

* **SetFramePosition(short hPos,short vPos)**
* **None**
* Sets the position of the dialog frame rectangle.
```

```

* **SetFrameRect([Rect](ArchicadDG_Rect.md) rect,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint,bool keepOld)**
* **None**
* Sets the dialog frame rectangle.
```

```

* **SetFrameRect([Rect](ArchicadDG_Rect.md) rect,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint)**
* **None**
* Sets the dialog frame rectangle.
```

```

* **SetFrameRect([Rect](ArchicadDG_Rect.md) rect)**
* **None**
* Sets the dialog frame rectangle.
```

```

* **SetFrameSize(short width,short height,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint,bool keepOld)**
* **None**
* Sets the size of the dialog frame rectangle.
```

```

* **SetFrameSize(short width,short height,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint)**
* **None**
* Sets the size of the dialog frame rectangle.
```

```

* **SetFrameSize(short width,short height)**
* **None**
* Sets the size of the dialog frame rectangle.
```

```

* **SetFrameWidth(short width,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint,bool keepOld)**
* **None**
* Sets the width of the dialog frame rectangle.
```

```

* **SetFrameWidth(short width,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint)**
* **None**
* Sets the width of the dialog frame rectangle.
```

```

* **SetFrameWidth(short width)**
* **None**
* Sets the width of the dialog frame rectangle.
```

```

* **SetFrameHeight(short height,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint,bool keepOld)**
* **None**
* Sets the height of the dialog frame rectangle.
```

```

* **SetFrameHeight(short height,[Dialog.FixPoint](ArchicadDG_FixPoint.md) fixPoint)**
* **None**
* Sets the height of the dialog frame rectangle.
```

```

* **SetFrameHeight(short height)**
* **None**
* Sets the height of the dialog frame rectangle.
```

```

* **GetFramePosition()**
* **[Point](ArchicadDG_Point.md)**
* Retrieves the position of the dialog frame rectangle.
```

```

* **GetFrameRect()**
* **[Rect](ArchicadDG_Rect.md)**
* Retrieves the dialog frame rectangle.
```

```

* **GetFrameWidth()**
* **short**
* Retrieves the width of the dialog frame rectangle.
```

```

* **GetFrameHeight()**
* **short**
* Retrieves the height of the dialog frame rectangle.
```

```

* **BeginMoveResizeItems()**
* **None**
* Disable update while moving or resizing dialog items.
```

```

* **EndMoveResizeItems()**
* **None**
* Enable update after moving or resizing dialog items.
```

```

* **SetTitle(string title)**
* **None**
* Sets the dialog title.
```

```

* **GetTitle()**
* **string**
* Retrieves the dialog title.
```

```

* **EnableIdleEvent(Boolean sendForInactiveApp)**
* **None**
* Enables idle event processing for the dialog.
```

```

* **EnableNormalUpdate()**
* **None**
* Enables normal update mechanism of partially updateable user items of the dialog.
```

```

* **DisableNormalUpdate()**
* **None**
* Disables normal update mechanism of partially updateable user items of the dialog.
```

```

* **SetPopupStyle()**
* **None**
* Sets the dialog popup style.
```

```

* **HasPopupStyle()**
* **Boolean**
* 
```

```

* **EnableGrowBox()**
* **None**
* Enables drawing the grow box if the dialog is resizeable.
```

```

* **DisableGrowBox()**
* **None**
* Disables drawing the grow box if the dialog is resizeable.
```

```

* **IsGrowBoxEnabled()**
* **Boolean**
* Checks the visibility state of the grow box.
```

```

* **SetGrowBoxSize(short size)**
* **Boolean**
* Sets the size of the grow box.
```

```

* **GetGrowBoxSize()**
* **short**
* Retrieves the size of the grow box.
```

```

* **SetGrowBoxForm([Dialog.GrowBoxForm](ArchicadDG_GrowBoxForm.md) form)**
* **None**
* Sets the form of the grow box.
```

```

* **GetGrowBoxForm()**
* **[Dialog.GrowBoxForm](ArchicadDG_GrowBoxForm.md)**
* Retrieves the form of the grow box.
```

```

* **RegisterDragAndDrop()**
* **None**
* Registers drop target capability to a dialog.
```

```

* **RevokeDragAndDrop()**
* **None**
* Removes drop target capability from a dialog.
```

```

* **EnableDraw()**
* **None**
* Enables drawing.
```

```

* **DisableDraw()**
* **None**
* Disables drawing.
```

```

* **Redraw()**
* **None**
* Redraws the item immediately.
```

```

* **SetCursorPosition([Point](ArchicadDG_Point.md) pt)**
* **None**
* Sets cursor postion
```

```

* **KeepInScreen()**
* **None**
* 
```

```

* **HasChangedDialogItems()**
* **Boolean**
* 
```

```

* **ResetDialogItemChanges()**
* **None**
* 
```

```
