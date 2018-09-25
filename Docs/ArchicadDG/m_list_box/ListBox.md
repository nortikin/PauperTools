## ListBox Class

### Parent Class
* [Item](../m_item/Item.md)
* [ItemFontProperty](../m_item/ItemFontProperty.md)
* [FocusableProperty](../m_item/FocusableProperty.md)

### Children Class
* [SingleSelListBox](SingleSelListBox.md)
* [MultiSelListBox](MultiSelListBox.md)

### Import
```
from ArchicadDG import ListBox
``` 

### Class Functions

* **AppendItem()**
* **Boolean**
* 
-----

* **InsertItem(short listItem)**
* **Boolean**
* 
-----

* **DeleteItem(short listItem)**
* **None**
* 
-----

* **GetItemCount()**
* **short**
* 
-----

* **InsertSeparator(short listItem)**
* **Boolean**
* 
-----

* **IsSeparator(short listItem)**
* **Boolean**
* 
-----

* **HasHeader()**
* **Boolean**
* 
-----

* **GetHeaderHeight()**
* **short**
* 
-----

* **SetHeaderSynchronState(Boolean isSynchron)**
* **None**
* 
-----

* **IsHeaderInSynchronState()**
* **Boolean**
* 
-----

* **SetHeaderPushableButtons(Boolean hasPushableButtons)**
* **None**
* 
-----

* **HasHeaderPushableButtons()**
* **Boolean**
* 
-----

* **SetHeaderDragableButtons(Boolean hasDragableButtons)**
* **None**
* 
-----

* **HasHeaderDragableButtons()**
* **Boolean**
* 
-----

* **SetHeaderItemCount(short itemCount)**
* **None**
* 
-----

* **GetHeaderItemCount()**
* **short**
* 
-----


* **SetHeaderItemText(short headerItem, string text)**
* **None**
* 
-----

* **GetHeaderItemText(short headerItem)**
* **string**
* 
-----

* **SetHeaderItemFont(short headerItem, [Font.Size](../Font/Size.md) size, [Font.Style](../Font/Style.md) style)**
* **None**
* 
-----

* **GetHeaderItemFontSize(short headerItem)**
* **[Font.Size](../Font/Size.md)**
* 
-----

* **GetHeaderItemFontStyle(short headerItem)**
* **[Font.Style](../Font/Style.md)**
* 
-----

* **SetHeaderItemStyle(short headerItem, [ListBox.Justification](ListBox_Justification.md) just, [ListBox.Truncation](ListBox_Truncation.md) trunc)**
* **None**
* 
-----

* **GetHeaderItemJustification(short headerItem)**
* **[ListBox.Justification](ListBox_Justification.md)**
* 
-----

* **GetHeaderItemTruncation(short headerItem)**
* **[ListBox.Truncation](ListBox_Truncation.md)**
* 
-----

* **SetHeaderItemSizeableFlag(short headerItem, Boolean isSizeable)**
* **None**
* 
-----

* **IsHeaderItemSizeable(short headerItem)**
* **Boolean**
* 
-----

* **SetHeaderItemSize(short headerItem, short size)**
* **None**
* 
-----

* **GetHeaderItemSize(short headerItem)**
* **short**
* 
-----

* **SetHeaderItemMinSize(short headerItem, short minSize)**
* **None**
* 
-----

* **GetHeaderItemMinSize(short headerItem)**
* **short**
* 
-----

* **SetHeaderItemArrowType(short headerItem, [ListBox.ArrowType](ListBox_ArrowType.md) arrowType)**
* **None**
* 
-----

* **GetHeaderItemArrowType(short headerItem)**
* **[ListBox.ArrowType](ListBox_ArrowType.md)**
* 
-----

* **EnableHeaderButton()**
* **None**
* 
-----

* **DisableHeaderButton()**
* **None**
* 
-----

* **IsHeaderButtonEnabled()**
* **Boolean**
* 
-----

* **SetTabFieldCount(short nTabFields)**
* **Boolean**
* 
-----

* **GetTabFieldCount()**
* **short**
* 
-----

* **SetTabFieldBeginPosition(short tabIndex, short begPos)**
* **None**
* 
-----

* **SetTabFieldEndPosition(short tabIndex, short endPos)**
* **None**
* 
-----

* **SetTabFieldJustification(short tabIndex, [ListBox.Justification](ListBox_Justification.md) just)**
* **None**
* 
-----

* **SetTabFieldTruncation(short tabIndex, [ListBox.Truncation](ListBox_Truncation.md) trunc)**
* **None**
* 
-----

* **SetTabFieldSeparator(short tabIndex, Boolean hasSeparator)**
* **None**
* 
-----

* **SetTabFieldStatus(short tabIndex, Boolean status)**
* **None**
* 
-----
* **GetTabFieldBeginPosition(short tabIndex)**
* **short**
* 
-----

* **GetTabFieldEndPosition(short tabIndex)**
* **short**
* 
-----

* **GetTabFieldJustification(short tabIndex)**
* **[ListBox.Justification](ListBox_Justification.md)**
* 
-----

* **GetTabFieldTruncation(short tabIndex)**
* **[ListBox.Truncation](ListBox_Truncation.md)**
* 
-----

* **HasTabFieldSeparator(short tabIndex)**
* **Boolean**
* 
-----

* **IsTabFieldEnabled(short tabIndex)**
* **Boolean**
* 
-----

* **SetTabFieldOwnerDrawFlag(short tabIndex, Boolean ownerDraw)**
* **None**
* 
-----

* **GetTabFieldOwnerDrawFlag(short tabIndex)**
* **Boolean**
* 
-----

* **SetTabFieldToSearch(short tabIndex)**
* **None**
* 
-----

* **GetTabFieldToSearch()**
* **short**
* 
-----

* **SetTabItemText(short listItem, short tabIndex, string text)**
* **None**
* 
-----

* **GetTabItemText(short listItem, short tabIndex)**
* **string**
* 
-----

* **SetTabItemFontStyle(short listItem, short tabIndex, [Font.Style](../Font/Style.md) style)**
* **None**
* 
-----

* **GetTabItemFontStyle (short listItem, short tabIndex)**
* **[Font.Style](../Font/Style.md)**
* 
-----

* **SetTabItemColor(short listItem, short tabIndex, [ArchicadGfx.Color](../../ArchicadGfx/Color.md) color)**
* **None**
* 
-----

* **SetTabItemBackgroundColor(short listItem, short tabIndex,[ArchicadGfx.Color](../../ArchicadGfx/Color.md) color)**
* **None**
* 
-----

* **GetTabItemColor(short listItem, short tabIndex)**
* **[ArchicadGfx.Color](../../ArchicadGfx/Color.md)**
* 
-----

* **GetTabItemBackgroundColor(short listItem, short tabIndex)**
* **[ArchicadGfx.Color](../../ArchicadGfx/Color.md)**
* 
-----

* **SetOnTabItem(short tabIndex,[Item](../m_item/Item.md) item)**
* **None**
* 
-----

* **RemoveOnTabItem(short tabIndex)**
* **None**
* 
-----

* **GetOnTabItem(short tabIndex)**
* **[Item](../m_item/Item.md)**
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

* **SetItemBackgroundColor(short listItem,[ArchicadGfx.Color](../../ArchicadGfx/Color.md) color)**
* **None**
* 
-----

* **GetItemColor(short listItem)**
* **[ArchicadGfx.Color](../../ArchicadGfx/Color.md)**
* 
-----

* **GetItemBackgroundColor(short listItem)**
* **[ArchicadGfx.Color](../../ArchicadGfx/Color.md)**
* 
-----

* **SetItemStatus(short listItem, [ListBox.ItemStatus](ListBox_ItemStatus.md) status)**
* **None**
* 
-----

* **GetItemStatus(short listItem)**
* **[ListBox.ItemStatus](ListBox_ItemStatus.md)**
* 
-----

* **EnableItem(short listItem)**
* **None**
* 
-----

* **GrayItem(short listItem)**
* **None**
* 
-----

* **DisableItem(short listItem)**
* **None**
* 
-----

* **IsItemEnabled(short listItem)**
* **Boolean**
* 
-----

* **IsItemGrayed(short listItem)**
* **Boolean**
* 
-----

* **IsItemDisabled(short listItem)**
* **Boolean**
* 
-----

* **IsItemVisible(short listItem)**
* **Boolean**
* 
-----

* **SetItemOwnerDrawFlag(short listItem, Boolean isOwnerDrawn)**
* **None**
* 
-----

* **GetItemOwnerDrawFlag(short listItem)**
* **Boolean**
* 
-----

* **SetItemHeight (short itemHeight)**
* **None**
* 
-----

* **GetItemHeight()**
* **short**
* 
-----

* **GetItemWidth()**
* **short**
* 
-----

* **GetItemRect(short listItem)**
* **[Rect](../Rect.md)**
* 
-----

* **SetNoPartialItem()**
* **None**
* 
-----

* **EnableSeparatorLines(bool hasSeparatorLines)**
* **None**
* 
-----

* **HasSeparatorLines()**
* **Boolean**
* 
-----

* **SetSeparatorLineColor([ArchicadGfx.Color](../../ArchicadGfx/Color.md) color)**
* **None**
* 
-----

* **GetSeparatorLineColor()**
* **[ArchicadGfx.Color](../../ArchicadGfx/Color.md)**
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

* **GetSelectedItem(short listItem)**
* **short**
* 
-----

* **GetSelectedItem([ListBox.ItemType](ListBox_ItemType.md) type)**
* **short**
* 
-----

* **GetSelectedItems()**
* **array**
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

* **RedrawItem(short listItem)**
* **None**
* 
-----

* **RedrawTabItem(short listItem, short tabIndex)**
* **None**
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

* **SetHScrollPosition(short scrollPosition)**
* **None**
* 
-----

* **GetHScrollPosition()**
* **short**
* 
-----

* **GetItemFromPosition([Point](../Point.md) pos)**
* **short**
* 
-----

* **SetHelpStyle([ListBox.HelpStyle](ListBox_HelpStyle.md) helpStyle)**
* **None**
* 
-----

* **GetHelpStyle()**
* **[ListBox.HelpStyle](ListBox_HelpStyle.md)**
* 
-----

