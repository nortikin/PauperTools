## ModalDialog Class

### Parent Class
* [Dialog](Dialog.md)

### Import
```
from ArchicadDG import ModalDialog
``` 

### Class Functions

* **constructor([Rect](../Rect.md) rect,[Dialog.GrowType](Dialog_GrowType.md) growType,[Dialog.CaptionType](Dialog_CaptionType.md) captionType,[Dialog.FrameType](Dialog_FrameType.md) frameType)**
* **constructor([Rect](../Rect.md) rect,[Dialog.GrowType](Dialog_GrowType.md) growType,[Dialog.CaptionType](Dialog_CaptionType.md) captionType)**
* **constructor([Rect](../Rect.md) rect,[Dialog.GrowType](Dialog_GrowType.md) growType)**
* **constructor([Rect](../Rect.md) rect)**
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

* **PostCloseRequest([ModalDialog.ModalResponse](ModalDialog_ModalResponse.md) response)**
* **None**
* Initiates to close the dialog by posting a close request event to it.

```

```

* **GetNextModalDialog()**
* **ModalDialog**
* Retrieves a dialog pointer to the next modal dialog.

```

```

* **GetPrevModalDialog()**
* **ModalDialog**
* Retrieves a dialog pointer to the previous modal dialog.

```

```
