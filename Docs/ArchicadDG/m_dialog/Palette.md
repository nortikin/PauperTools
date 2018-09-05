## Palette Class

### Parent Class
* [ModelessBase](ModelessBase.md)

### Import
```
from ArchicadDG import Palette
``` 

### Class Functions

* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType,[Dialog.FrameType](ArchicadDG_FrameType.md) frameType,[Dialog.SpecialFeatures](ArchicadDG_SpecialFeatures.md) specialFeatures)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType,[Dialog.FrameType](ArchicadDG_FrameType.md) frameType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CloseType](ArchicadDG_CloseType.md) closeType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect)**
* Class constructor.
```
```

* **SendBehind([Palette](ArchicadDG_Palette.md) behindPalette)**
* **None**
* Moves the palette dialog behind the specified palette dialog in the Z order.
```

```


* **GetNextPalette()**
* **[Palette](ArchicadDG_Palette.md)**
* Retrieves the next palette dialog.

```

```

* **GetPrevPalette()**
* **[Palette](ArchicadDG_Palette.md)**
* Retrieves the previous palette dialog.

```

```

* **GetNextVisiblePalette()**
* **[Palette](ArchicadDG_Palette.md)**
* Retrieves the next visible palette dialog.

```

```

* **GetPrevVisiblePalette()**
* **[Palette](ArchicadDG_Palette.md)**
* Retrieves the previous visible palette dialog.

```

```

* **DisableDock(short orientationFlag)**
* **short**
* 

```

```

* **Dock()**
* **None**
* 

```

```

* **UnDock()**
* **None**
* 
```

```

* **IsDocked()**
* **Boolean**
* 
```

```

* **GetCaptionType()**
* **short**
* 
```

```
