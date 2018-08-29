## SplitButton Class

### Button Inheritance Diagram

<img src="../../Imgs/button_inheritance_diagram.png" />

### Videos
* Youttube: https://youtu.be/I2uRGDRBfVM

### Parent Class
* [SplitButtonBase](ArchicadDG_SplitButtonBase.md)

### Children Class
* None

### Import
```
from ArchicadDG import SplitButton
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

* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect,[SplitButtonBase.ButtonForm](ArchicadDG_SplitButtonBase_ButtonForm.md) form)**
* **constructor([Panel](../ArchicadDG_Panel.md) panel,[Rect](../ArchicadDG_Rect.md) rect)**
* Class constructor.
-----

* **AppendItem(string itemText)**
* **None**
* 
-----

* **AppendSeparator()**
* **None**
* 
-----

* **InsertItem(short itemIndex,string itemText)**
* **None**
* 
-----

* **InsertSeparator(short itemIndex)**
* **None**
* 
-----

* **DeleteItem(short itemIndex)**
* **None**
* 
-----

* **DeleteAllItems()**
* **None**
* 
-----

* **GetItemCount()**
* **USize**
* 
-----

* **GetSelectedItem()**
* **UIndex**
* 
-----

* **SetItemText(short popupItem,string text)**
* **None**
* 
-----

* **GetItemText(short popupItem)**
* **string**
* 
-----

* **SetItemTextSize(short popupItem,[ArchicadDG.Font.Size](../ArchicadDG_Font_Size.md) size)**
* **None**
* 
-----

* **GetItemTextSize(short popupItem)**
* **[ArchicadDG.Font.Size](../ArchicadDG_Font_Size.md)**
* 
-----

* **SetItemTextStyle(short popupItem,[ArchicadDG.Font.Style](../ArchicadDG_Font_Style.md) style)**
* **None**
* 
-----

* **GetItemTextStyle(short popupItem)**
* **[ArchicadDG.Font.Style](../ArchicadDG_Font_Style.md)**
* 
-----

* **EnableItem(short popupItem)**
* **None**
* 
-----

* **DisableItem(short popupItem)**
* **None**
* 
-----

* **SetItemStatus(short popupItem, Boolean status)**
* **None**
* 
-----

* **IsItemEnabled(short popupItem)**
* **Boolean**
* 
-----

* **IsSeparatorItem(short popupItem)**
* **Boolean**
* 
-----

* **EnableDraw()**
* **None**
* 
-----

* **DisableDraw()**
* **None**
* 
-----