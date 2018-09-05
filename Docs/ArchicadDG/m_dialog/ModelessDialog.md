## ModelessDialog Class

### Parent Class
* [ModelessBase](ModelessBase.md)

### Import
```
from ArchicadDG import ModelessDialog
``` 

### Class Functions

* **constructor([Rect](../Rect.md) rect,[Dialog.GrowType](Dialog_GrowType.md) growType,[Dialog.CloseType](Dialog_CloseType.md) closeType,[Dialog.MinimizeType](Dialog_MinimizeType.md) minimizeType,[Dialog.MaximizeType](Dialog_MaximizeType.md) maximizeType,[Dialog.CaptionType](Dialog_CaptionType.md) captionType,[Dialog.FrameType](Dialog_FrameType.md) frameType,[Dialog.SpecialFeatures](Dialog_SpecialFeatures.md) specialFeatures)**
* **constructor([Rect](../Rect.md) rect,[Dialog.GrowType](Dialog_GrowType.md) growType,[Dialog.CloseType](Dialog_CloseType.md) closeType,[Dialog.MinimizeType](Dialog_MinimizeType.md) minimizeType,[Dialog.MaximizeType](Dialog_MaximizeType.md) maximizeType,[Dialog.CaptionType](Dialog_CaptionType.md) captionType,[Dialog.FrameType](Dialog_FrameType.md) frameType)**
* **constructor([Rect](../Rect.md) rect,[Dialog.GrowType](Dialog_GrowType.md) growType,[Dialog.CloseType](Dialog_CloseType.md) closeType,[Dialog.MinimizeType](Dialog_MinimizeType.md) minimizeType,[Dialog.MaximizeType](Dialog_MaximizeType.md) maximizeType,[Dialog.CaptionType](Dialog_CaptionType.md) captionType)**
* **constructor([Rect](../Rect.md) rect,[Dialog.GrowType](Dialog_GrowType.md) growType,[Dialog.CloseType](Dialog_CloseType.md) closeType,[Dialog.MinimizeType](Dialog_MinimizeType.md) minimizeType,[Dialog.MaximizeType](Dialog_MaximizeType.md) maximizeType)**
* **constructor([Rect](../Rect.md) rect,[Dialog.GrowType](Dialog_GrowType.md) growType,[Dialog.CloseType](Dialog_CloseType.md) closeType,[Dialog.MinimizeType](Dialog_MinimizeType.md) minimizeType)**
* **constructor([Rect](../Rect.md) rect,[Dialog.GrowType](Dialog_GrowType.md) growType,[Dialog.CloseType](Dialog_CloseType.md) closeType)**
* **constructor([Rect](../Rect.md) rect,[Dialog.GrowType](Dialog_GrowType.md) growType)**
* **constructor([Rect](../Rect.md) rect)**
* Class constructor.
```
```

* **SendBehind(ModelessDialog behindModeless)**
* **None**
* Moves the dialog behind the specified dialog in the Z order.
```

```

* **GetNextModelessDialog()**
* **ModelessDialog**
* Retrieves the next modeless dialog.

```

```

* **GetPrevModelessDialog()**
* **ModelessDialog**
* Retrieves the previous modeless dialog.

```

```

* **GetNextVisibleModelessDialog()**
* **ModelessDialog**
* Retrieves the next visible modeless dialog.

```

```

* **GetPrevVisibleModelessDialog()**
* **ModelessDialog**
* Retrieves the previous visible modeless dialog.

```

```
* **GetRestoredClientPosition()**
* **[Point](../Point.md)**
* Retrieves the position of the dialog client area, when the dialog is in restored state.

```

```

* **GetRestoredClientRect()**
* **[Rect](../Rect.md)**
* Retrieves the rectangle of the dialog client area, when the dialog is in restored state.

```

```

* **GetRestoredClientWidth()**
* **short**
* Retrieves the width of the dialog client area, when the dialog is in restored state.

```

```

* **GetRestoredClientHeight()**
* **short**
* Retrieves the height of the dialog client area, when the dialog is in restored state.

```

```

* **GetRestoredFrameRect()**
* **[Rect](../Rect.md)**
* Retrieves the dialog frame rectangle, when the dialog is in restored state.

```

```

* **Maximize(Boolean beforeDock)**
* **None**
* Maximizes the dialog.
```

```

* **Maximize()**
* **None**
* Maximizes the dialog.
```

```

* **Minimize()**
* **None**
* Minimizes the dialog.
```

```

* **Restore()**
* **None**
* Restores the dialog from minimized or maximized state.
```

```

* **SetState([ModelessDialog.DialogState](ModelessDialog_DialogState.md) state,Boolean beforeDock)**
* **None**
* Sets the minimized, maximized or restored state of the dialog.
```

```

* **SetState([ModelessDialog.DialogState](ModelessDialog_DialogState.md) state)**
* **None**
* Sets the minimized, maximized or restored state of the dialog.
```

```

* **IsMaximizedState()**
* **Boolean**
* Tests whether the dialog is in maximized state or not.
```

```

* **IsMinimizedState()**
* **Boolean**
* Tests whether the dialog is in minimized state or not.
```

```

* **IsRestoredState()**
* **Boolean**
* Tests whether the dialog is in restored state or not.
```

```

* **GetState()**
* **[ModelessDialog.DialogState](ModelessDialog_DialogState.md)**
* Retrieves the minimized, maximized or restored state of the dialog.
```

```

* **Dock()**
* **None**
* 
```

```

* **Undock()**
* **None**
* 
```

```

* **IsDocked()**
* **Boolean**
* 
```

```

* **SetDockState([ModelessDialog.DockState](ModelessDialog_DockState.md) dockState)**
* **None**
* 
```

```

* **GetDockState()**
* **[ModelessDialog.DockState](ModelessDialog_DockState.md)**
* 
```

```