## ModelessBase Class

### Parent Class
* [Dialog](Dialog.md)

### Children Class
* [Palette](Palette.md)
* [ModelessDialog](ModelessDialog.md)

### Import
```
from ArchicadDG import ModelessBase
``` 

### Class Functions

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

* **SetStatus([ModelessBase.DialogStatus](ModelessBase_DialogStatus.md) status)**
* **None**
* Sets the normal, enabled or disabled status of the dialog.
```

```

* **GetStatus()**
* **[ModelessBase.DialogStatus](ModelessBase_DialogStatus.md)**
* Retrieves the normal, enabled or disabled status of the dialog.
```

```
