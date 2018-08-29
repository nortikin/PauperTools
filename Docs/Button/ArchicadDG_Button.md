## Button Class

### Button Inheritance Diagram

<img src="../../Imgs/button_inheritance_diagram.png" />

### Videos
* Youttube: https://youtu.be/I2uRGDRBfVM

### Parent Class
* [ButtonItem](ArchicadDG_ButtonItem.md)
* [ItemFontProperty](../ArchicadDG_ItemFontProperty.md)
* [ItemTextProperty](../ArchicadDG_ItemTextProperty.md)
* [ItemIconProperty](../ArchicadDG_ItemIconProperty.md)

### Children Class
* None

### Import
```
from ArchicadDG import Button
``` 

### Example
* [demo](../../Scripts/Tests/dg_button_test.py)

### Testing
```
import Tests.dg_button_test as button_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.frm=button_test.FormPalette()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass

```

### Class Functions

* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect,[Button.ButtonType](ArchicadDG_Button_ButtonType.md) type,[Button.FrameType](ArchicadDG_Button_FrameType.md) frameType)**
* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect,[Button.ButtonType](ArchicadDG_Button_ButtonType.md) type)**
* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect)**
* Class constructor.
-----

* **SetAsDefault()**
* **None**
* 
-----

* **SetAsCancel()**
* **None**
* 
-----

* **SetAlignment([Button.Alignment](ArchicadDG_Button_Alignment.md) alignment)**
* **None**
* 
-----

* **GetAlignment()**
* **[Button.Alignment](ArchicadDG_Button_Alignment.md)**
* 
-----