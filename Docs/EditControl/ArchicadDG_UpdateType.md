## UpdateType Enum

### Import
```
from ArchicadDG import EditControl
``` 

## Example
```
from ArchicadDG import *
ft1=EditControl.Update
ft2=EditControl.UpdateType.NoUpdate
```

### Values
* **Update**:Content of the edit control is validated automatically in a short time (update delay time) after the last keypress.
* **NoUpdate**:Content of the edit control is validated only if it loses the keyboard focus.
* **NoDelay**:Content of the edit control is updated immediately.