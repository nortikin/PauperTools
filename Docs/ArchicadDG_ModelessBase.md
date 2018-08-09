## ModelessBase Class

### Parent Class
[Dialog](ArchicadDG_Dialog.md)

### Children Class
[Palette](ArchicadDG_Palette.md)
[ModelessDialog](ArchicadDG_ModelessDialog.md)

### Import
```
from ArchicadDG import ModelessBase
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

* **SendCloseRequest()**
* **None**
* Initiates to close the dialog by sending a close request event to it.
```

```


* **BringToFront()**
* **None**
* Moves the dialog to the top of the Z order of the same type of dialogs.

```

```

* **SendToBack()**
* **None**
* Moves the dialog to the bottom of the Z order of the same type of dialogs.

```

```

* **Show(short refDialId)**
* **None**
* Shows the dialog.

```

```

* **Show()**
* **None**
* Shows the dialog.

```

```

* **Hide()**
* **None**
* Hides the dialog.

```

```

* **SetVisibility(Boolean show)**
* **None**
* Sets the visibility state of the dialog.

```

```

* **IsVisible()**
* **Boolean**
* Retrieves the visibility state of the dialog.
```

```

* **Activate()**
* **None**
* Moves the dialog to the top of the Z order of the same type of dialogs and activates it.
```

```

* **IsActive()**
* **Boolean**
* Tests whether the dialog is active or not.
```

```

* **SetStatus([ModelessBase.DialogStatus](ArchicadDG_DialogStatus.md) status)**
* **None**
* Sets the normal, enabled or disabled status of the dialog.
```

```

* **GetStatus()**
* **[ModelessBase.DialogStatus](ArchicadDG_DialogStatus.md)**
* Retrieves the normal, enabled or disabled status of the dialog.
```

```
