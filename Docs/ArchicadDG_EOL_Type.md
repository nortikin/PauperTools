## Type Enum

### Import
```
from ArchicadDG.EOL import Type
``` 

## Example
```
from ArchicadDG import *
ft1=EOL.Default
ft2=EOL.Type.CR
```

### Values
* **Default**:Default end-of-line character. It is CRLF on Windows, CR on Macintosh.
* **CR**:CR (\x0D) end-of-line character.
* **CRLF**:CRLF (\x0D\x0A) end-of-line character pair.