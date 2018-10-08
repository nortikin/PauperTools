## ListView Class

### Parent Class
* [Item](../m_item/Item.md)
* [ItemFontProperty](../m_item/ItemFontProperty.md)
* [FocusableProperty](../m_item/FocusableProperty.md)

### Children Class
* [SingleSelListView](SingleSelListView.md)
* [MultiSelListView](MultiSelListView.md)

### Import
```
from ArchicadDG import ListView
``` 

### Class Functions

* **AppendItem()**
* **None**
* 
-----

* **InsertItem(short listItem)()**
* **None**
* 
-----

* **DeleteItem(short listItem)()**
* **None**
* 
-----

* **GetItemCount()**
* **short**
* 
-----

* **SetItemText(short listItem,string text)**
* **None**
* 
-----

* **GetItemText(short listItem)**
* **string**
* 
-----

* **GetItemImageType(short listItem)**
* **[ListView.ImageType](ListView_ImageType.md)**
* 
-----

* **SetItemImageOwnerDrawFlag(short listItem,Boolean flag)**
* **None**
* 
-----

* **IsItemImageOwnerDrawn(short listItem)**
* **Boolean**
* 
-----

* **SetItemFontStyle(short listItem, [Font.Style](../Font/Style.md) style)**
* **None**
* 
-----

* **GetItemFontStyle(short listItem)**
* **[Font.Style](../Font/Style.md)**
* 
-----

* **SetItemColor(short listItem,[ArchicadGfx.Color](../../ArchicadGfx/Color.md) color)**
* **None**
* 
-----

* **GetItemColor(short listItem)**
* **[ArchicadGfx.Color](../../ArchicadGfx/Color.md)**
* 
-----

* **SetBackground([ListView.Background](ListView_Background.md) background)**
* **None**
* 
-----

* **GetBackground()**
* **[ListView.Background](ListView_Background.md)**
* 
-----

* **SetSelectionStyle([ListView.SelectionStyle](ListView_SelectionStyle.md) selectionStyle)**
* **None**
* 
-----

* **GetSelectionStyle()**
* **[ListView.SelectionStyle](ListView_SelectionStyle.md)**
* 
-----

* **SetHelpStyle([ListView.HelpStyle](ListView_HelpStyle.md) helpStyle)**
* **None**
* 
-----

* **GetHelpStyle()**
* **[ListView.HelpStyle](ListView_HelpStyle.md)**
* 
-----

* **GetClientWidth()**
* **short**
* 
-----

* **GetClientHeight()**
* **short**
* 
-----

* **HasVerticalScrollBar()**
* **Boolean**
* 
-----

* **IsVerticalScrollBarVisible()**
* **Boolean**
* 
-----

* **EnableItem(short listItem)**
* **None**
* 
-----

* **DisableItem(short listItem)**
* **None**
* 
-----

* **SetItemStatus(short listItem,Boolean enable)**
* **None**
* 
-----

* **IsItemEnabled(short listItem)**
* **Boolean**
* 
-----

* **IsItemVisible(short listItem)**
* **Boolean**
* 
-----

* **SelectItem(short listItem)**
* **None**
* 
-----

* **SelectItems(array listItems)**
* **None**
* 
-----

* **DeselectItem(short listItem)**
* **None**
* 
-----

* **GetSelectedCount()**
* **short**
* 
-----

* **GetSelectedItem()**
* **short**
* 
-----

* **GetSelectedItem(short)**
* **short**
* 
-----

* **GetSelectedItem([ListView.ItemType](ListView_ItemType.md) itemType)**
* **short**
* 
-----

* **GetSelectedItems()**
* **array**
* 
-----

* **EnableMouseMoveEvent()**
* **None**
* 
-----

* **EnableHoverEvent()**
* **None**
* 
-----

* **EnablePressedEvent()**
* **None**
* 
-----

* **ClearHover()**
* **None**
* 
-----

* **SetHoverInWaitMillisecs(Int32 hoverInWaitMillisecs)**
* **None**
* 
-----

* **SetScrollPosition(short scrollPosition)**
* **None**
* 
-----

* **GetScrollPosition()**
* **short**
* 
-----

* **ScrollUp()**
* **None**
* 
-----

* **ScrollDown()**
* **None**
* 
-----

* **GetItemFromPosition([Point](../Point.md) pos)**
* **short**
* 
-----

* **SetViewMode([ListView.ViewMode](ListView_ViewMode.md) viewMode)**
* **None**
* 
-----

* **GetViewMode()**
* **[ListView.ViewMode](ListView_ViewMode.md)**
* 
-----

* **SetItemWidth(short itemWidth)**
* **None**
* 
-----

* **SetItemHeight(short itemHeight)**
* **None**
* 
-----

* **GetItemWidth()**
* **short**
* 
-----

* **GetItemHeight()**
* **short**
* 
-----

* **GetItemRect(short listItem)**
* **[Rect](../Rect.md)**
* 
-----

* **SetImageWidth(short imageWidth)**
* **None**
* 
-----

* **SetImageHeight(short imageHeight)**
* **None**
* 
-----

* **GetImageWidth()**
* **short**
* 
-----

* **GetImageHeight()**
* **short**
* 
-----

* **GetImageType()**
* **[ListView.ImageType](ListView_ImageType.md)**
* 
-----

* **SetImageGap(short imageGap)**
* **None**
* 
-----

* **GetImageGap()**
* **short**
* 
-----

* **SetTextTruncateWidth(short textTruncateWidth)**
* **None**
* 
-----

* **GetTextTruncateWidth()**
* **short**
* 
-----

* **GetSubImageCount()**
* **short**
* 
-----

* **GetSubImageRowCount()**
* **short**
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