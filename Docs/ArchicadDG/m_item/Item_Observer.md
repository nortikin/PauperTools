## ItemObserver Class

### Children Class
* [ShortcutEditObserver](../m_edit_control/ShortcutEdit_Observer.md)
* [TextEditBaseObserver](../m_edit_control/TextEditBase_Observer.md)
* [RealEditObserver](../m_edit_control/RealEdit_Observer.md)
* [PosIntEditObserver](../m_edit_control/PosIntEdit_Observer.md)
* [IntEditObserver](../m_edit_control/IntEdit_Observer.md)
* [ButtonItemObserver](../m_button/ButtonItem_Observer.md)
* [RadioItemObserver](../m_radio_item/RadioItem_Observer.md)
* [CheckItemObserver](../m_check_item/CheckItem_Observer.md)

### Import
```
from ArchicadDG import ItemObserver
``` 

### Example
* Waiting for improvement

### Testing
* Waiting for improvement

### Class Functions

* **constructor([Item](Item.md) item)**
* Class constructor.

### Class Events

#### ChangeRequested([Item](Item.md) item,ItemMouseDownEvent e)
* **e.IsHovered[Boolean]**:
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for the item change requested notification.

#### Changed([Item](Item.md) item,ItemEvent e)
* Event handler for the item changed notification.

#### CharEntered([Item](Item.md) item,ItemCharEnterEvent e)
* **e.CharCode[UShort]**:Retrieves the character code entered before.
* **e.DenyChar[Boolean]**: the application should set this value to true to deny the entering of the character. By default the value of denyChar is false.
* Event handler for the char entered notification.

#### Clicked([Item](Item.md) item,ItemEvent e)
* Event handler for the clicked notification.

#### MouseDown([Item](Item.md) item,ItemMouseDownEvent e)
* **e.IsHovered[Boolean]**:
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for the mouse down notification.

#### ContextHelpRequested([Item](Item.md) item,ItemHelpEvent e)
* **e.SubItem[short]**:Retrieves the 1-based listItem index in case of a help request above a ListView or a ListBox.
* **e.TreeItem[Int32]**:
* **e.TabBarItemId[Int32]**:
* **e.Context[string]**:it should contain the required help anchor to be passed to the help engine to display the desired context sensitive help information. It is advisable to store tooltip and help anchor pairs in DHLP resource, and use the DGGetDynamicHelpStrings function to retrieve them, and pass to the event.
* Event handler for the context help requested notification.

#### ContextMenuRequested([Item](Item.md) item,ItemContextMenuEvent e)
* **e.Position[[Point](../Point.md)]**:Retrieves the context menu position.
* **e.NeedHelp[Boolean]**:If the user selected the "What's this"/"Help" item in the context menu, the programmer can signal the DG module to bring up the context sensitive help information for the item/dialog. So if you want DG to launch the help system with the data related to the item/dialog (this is probably because user clicked help command in the context menu) you should set this variable true and the processed variable to false. Othervise leave it untouched. By default the value of needHelp is false.
* **e.Processed[Boolean]**: if the application has processed this event, this value should be set to true to avoid the default event processing. By default the value of processed is false.
* Event handler for the context menu requested notification.

#### DoubleClicked([Item](Item.md) item,ItemEvent e)
* Event handler for the double clicked notification.

#### FocusGained([Item](Item.md) item,ItemEvent e)
* Event handler for the focus gained notification.

#### FocusLost([Item](Item.md) item,ItemEvent e)
* Event handler for the focus lost notification.

#### MouseMoved([Item](Item.md) item,ItemEvent e)
* Event handler for the mouse moved notification.

#### ToolTipRequested([Item](Item.md) item,ItemHelpEvent e)
* **e.SubItem[short]**:Retrieves the 1-based listItem index in case of a help request above a ListView or a ListBox.
* **e.TreeItem[Int32]**:
* **e.TabBarItemId[Int32]**:
* **e.Context[string]**:it should contain the required help anchor to be passed to the help engine to display the desired context sensitive help information. It is advisable to store tooltip and help anchor pairs in DHLP resource, and use the DGGetDynamicHelpStrings function to retrieve them, and pass to the event.
* Event handler for the tool tip requested notification.

#### TrackEntered([Item](Item.md) item,ItemEvent e)
* Event handler for the track entered notification.

#### Tracked([Item](Item.md) item,ItemEvent e)
* Event handler for the tracked notification.

#### TrackExited([Item](Item.md) item,ItemEvent e)
* Event handler for the track exited notification.

#### Update([Item](Item.md) item,ItemEvent e)
* Event handler for the update notification.

#### WheelTrackEntered([Item](Item.md) item,ItemWheelEvent e)
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for the wheel track entered notification.

#### WheelTracked([Item](Item.md) item,ItemWheelTrackEvent e)
* **e.XTrackValue[short]**:Retrieves the currently x tracked value.
* **e.YTrackValue[short]**:Retrieves the currently y tracked value.
* **e.MouseOffset[[Point](../Point.md)]**:Retrieves the mouse position.
* **e.IsCommandPressed[Boolean]**:Checks if command (control) button is pressed.
* **e.IsOptionPressed[Boolean]**:Checks if option (alt) button is pressed.
* **e.IsShiftPressed[Boolean]**:Checks if shift button is pressed.
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for the mouse wheel tracked notification.

#### WheelTrackExited([Item](Item.md) item,ItemWheelEvent e)
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for the wheel track exited notification.

#### ResolutionFactorChanged([Item](Item.md) item,ItemResolutionFactorChangeEvent e)
* **e.OldResolutionFactor[double]**:
* Event handler for the resolution factor changed notification.

#### HoverStarted([Item](Item.md) item,ItemEvent e)
* Event handler for the hover started notification.

#### HoverEnded([Item](Item.md) item,ItemEvent e)
* Event handler for the hover ended notification.

#### Pressed([Item](Item.md) item,ItemEvent e)
* Event handler for the pressed notification.

#### OverlayUpdate([Item](Item.md) item,ItemEvent e)
* Event handler for the overlay update notification.