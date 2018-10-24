## PopUp Class

### Parent Class
* [Item](../m_item/Item.md)
* [ItemFontProperty](../m_item/ItemFontProperty.md)

### Import
```
from ArchicadDG import PopUp
``` 

### Class Functions

* **constructor([Panel](../m_panel/Panel.md) panel,[Rect](../Rect.md) rect,short vSize,short textOffset)**

* Class constructor.
-----

* **AppendItem()**
* **None**
* 
-----

* **InsertItem(short popupItem)**
* **None**
* 
-----

* **DeleteItem(short popupItem)**
* **None**
* 
-----

* **GetItemCount()**
* **short**
* 
-----

* **AppendSeparator()**
* **None**
* 
-----

* **InsertSeparator(short popupItem)**
* **None**
* 
-----

* **IsSeparator(short popupItem)**
* **Boolean**
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

* **SetItemFontStyle(short popupItem, [Font.Style](../Font/Style.md) style)**
* **None**
* 
-----

* **GetItemFontStyle(short popupItem)**
* **[Font.Style](../Font/Style.md)**
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

* **SetItemStatus(short popupItem,Boolean enable)**
* **None**
* 
-----

* **IsItemEnabled(short popupItem)**
* **Boolean**
* 
-----

* **SetItemCharCode(short popupItem,[ArchicadGS.GSCharCode](../../ArchicadGS/GSCharCode.md) charCode)**
* **None**
* 
-----

* **GetItemCharCode(short popupItem)**
* **[ArchicadGS.GSCharCode](../../ArchicadGS/GSCharCode.md)**
* 
-----

* **SelectItem(short popupItem)**
* **None**
* 
-----

* **GetSelectedItem()**
* **short**
* 
-----

* **DisableDraw()**
* **None**
* 
-----

* **EnableDraw()**
* **None**
* 
-----