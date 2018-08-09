## DialogStatus Enum

### Import
```
from ArchicadDG import ModelessBase
``` 

## Example
```
from ArchicadDG import *
gt1=ModelessBase.Normal
gt2=ModelessBase.DialogStatus.Enabled
```

### Values
* **Normal**:If the onlyUpdate parameter of ModelessHandler is false, all the messages are handled for the dialog. If onlyUpdate is true in ModelessHandler, only update messages are handled for the dialog.
* **Enabled**:All the messages are handled for the dialog.
* **Disabled**:No messages are handled for the dialog.
* **Edited**:only edited messages are handled for the dialog.