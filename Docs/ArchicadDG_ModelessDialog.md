## ModelessDialog Class

### Form Inheritance Diagram

<img src="../Imgs/form_inheritance_diagram.png" width="384px" height="384px" />

### Parent Class
* [ModelessBase](ArchicadDG_ModelessBase.md)

### Import
```
from ArchicadDG import ModelessDialog
``` 

### Class Functions

* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.MinimizeType](ArchicadDG_MinimizeType.md) minimizeType,[Dialog.MaximizeType](ArchicadDG_MaximizeType.md) maximizeType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType,[Dialog.FrameType](ArchicadDG_FrameType.md) frameType,[Dialog.SpecialFeatures](ArchicadDG_SpecialFeatures.md) specialFeatures)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.MinimizeType](ArchicadDG_MinimizeType.md) minimizeType,[Dialog.MaximizeType](ArchicadDG_MaximizeType.md) maximizeType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType,[Dialog.FrameType](ArchicadDG_FrameType.md) frameType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.MinimizeType](ArchicadDG_MinimizeType.md) minimizeType,[Dialog.MaximizeType](ArchicadDG_MaximizeType.md) maximizeType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.MinimizeType](ArchicadDG_MinimizeType.md) minimizeType,[Dialog.MaximizeType](ArchicadDG_MaximizeType.md) maximizeType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.MinimizeType](ArchicadDG_MinimizeType.md) minimizeType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect)**
* Class constructor.
```
```

* **SendBehind([ModelessDialog](ArchicadDG_ModelessDialog.md) behindModeless)**
* **None**
* Moves the dialog behind the specified dialog in the Z order.
```

```

* **GetNextModelessDialog()**
* **[ModelessDialog](ArchicadDG_ModelessDialog.md)**
* Retrieves the next modeless dialog.

```

```

* **GetPrevModelessDialog()**
* **[ModelessDialog](ArchicadDG_ModelessDialog.md)**
* Retrieves the previous modeless dialog.

```

```

* **GetNextVisibleModelessDialog()**
* **[ModelessDialog](ArchicadDG_ModelessDialog.md)**
* Retrieves the next visible modeless dialog.

```

```

* **GetPrevVisibleModelessDialog()**
* **[ModelessDialog](ArchicadDG_ModelessDialog.md)**
* Retrieves the previous visible modeless dialog.

```

```
* **GetRestoredClientPosition()**
* **[Point](ArchicadDG_Point.md)**
* Retrieves the position of the dialog client area, when the dialog is in restored state.

```

```

* **GetRestoredClientRect()**
* **[Rect](ArchicadDG_Rect.md)**
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
* **[Rect](ArchicadDG_Rect.md)**
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

* **SetState([ModelessDialog.DialogState](ArchicadDG_DialogState.md) state,Boolean beforeDock)**
* **None**
* Sets the minimized, maximized or restored state of the dialog.
```

```

* **SetState([ModelessDialog.DialogState](ArchicadDG_DialogState.md) state)**
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
* **[ModelessDialog.DialogState](ArchicadDG_DialogState.md)**
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

* **SetDockState([ModelessDialog.DockState](ArchicadDG_DockState.md) dockState)**
* **None**
* 
```

```

* **GetDockState()**
* **[ModelessDialog.DockState](ArchicadDG_DockState.md)**
* 
```

```