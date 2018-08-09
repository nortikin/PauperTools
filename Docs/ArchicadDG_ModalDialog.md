## ModalDialog Class

### Parent Class
[Dialog](ArchicadDG_Dialog.md)

### Import
```
from ArchicadDG import ModalDialog
``` 

### Class Functions

* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType,[Dialog.FrameType](ArchicadDG_FrameType.md) frameType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType,[Dialog.CaptionType](ArchicadDG_CaptionType.md) captionType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect,[Dialog.GrowType](ArchicadDG_GrowType.md) growType)**
* **constructor([Rect](ArchicadDG_Rect.md) rect)**
* Class constructor.
```

```

* **Invoke()**
* **Boolean**
* Invokes the dialog.
```

```


* **Abort()**
* **None**
* Aborts the dialog.

```

```

* **PostCloseRequest([ModalDialog.ModalResponse](ArchicadDG_ModalResponse.md) response)**
* **None**
* Initiates to close the dialog by posting a close request event to it.

```

```

* **GetNextModalDialog()**
* **[ModalDialog](ArchicadDG_ModalDialog.md)**
* Retrieves a dialog pointer to the next modal dialog.

```

```

* **GetPrevModalDialog()**
* **[ModalDialog](ArchicadDG_ModalDialog.md)**
* Retrieves a dialog pointer to the previous modal dialog.

```

```
