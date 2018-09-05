## PanelObserver Class

### Import
```
from ArchicadDG import PanelObserver
``` 

### Class Functions

* **constructor([Panel](Panel.md) panel)**
* Class constructor.

### Class Events

#### CloseRequested([Panel](Panel.md) panel,PanelCloseRequestEvent e)
* **e.IsAccepted[Boolean]**:Retrieves whether the panel was accepted or not.
* **e.IsCancelled[Boolean]**:Retrieves whether the panel was cancelled or not.
* **e.Accepted[Boolean]**:if the application does not accept the close event, this value should be set to false, to avoid closing the dialog. By default this parameter is true. 
* Event handler for panel close requested notification.

#### HotkeyPressed([Panel](Panel.md) panel,PanelHotKeyEvent e)
* **e.KeyId[short]**:Retrieves the hotkey identifier.
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for hotkey pressed notification.

#### Idle([Panel](Panel.md) panel,PanelIdleEvent e)
* Event handler for panel idle notification.

#### Opened([Panel](Panel.md) panel,PanelOpenEvent e)
* **e.IsSavedPosition[Boolean]**:Tests whether the dialog position and size was restored from a previously saved rectangle or not.
* **e.IsDefaultPosition[Boolean]**:Tests whether the panel is opened in its default position.
* **e.IsAdjustedPosition[Boolean]**:Tests whether the restored position of the dialog was adjusted or not.
* Event handler for panel opened notification.

#### ResizeEntered([Panel](Panel.md) panel,PanelResizeEvent e)
* **e.IsUserResize[Boolean]**:Checks if the resize event occured as user interaction.
* **e.HorizontalChange[short]**:Retrieves the horizontal change.
* **e.VerticalChange[short]**:Retrieves the vertical change.
* Event handler for panel resize entered notification.

#### Resizing([Panel](Panel.md) panel,PanelResizingEvent e)
* **e.IsUserResize[Boolean]**:Checks if the resize event occured as user interaction.
* **e.HorizontalChange[short]**:Retrieves the horizontal change.
* **e.VerticalChange[short]**:Retrieves the vertical change.
* **e.GrowValues[[Point](../Point.md)]**:Retrieves the grow values.
* Event handler for panel resizing notification.

#### Resized([Panel](Panel.md) panel,PanelResizeEvent e)
* **e.IsUserResize[Boolean]**:Checks if the resize event occured as user interaction.
* **e.HorizontalChange[short]**:Retrieves the horizontal change.
* **e.VerticalChange[short]**:Retrieves the vertical change.
* Event handler for panel resized notification.

#### ResizeExited([Panel](Panel.md) panel,PanelResizeEvent e)
* **e.IsUserResize[Boolean]**:Checks if the resize event occured as user interaction.
* **e.HorizontalChange[short]**:Retrieves the horizontal change.
* **e.VerticalChange[short]**:Retrieves the vertical change.
* Event handler for panel resize exited notification.

#### MoveEntered([Panel](Panel.md) panel,PanelMoveEvent e)
* **e.Rect[[Rect](../Rect.md)]**:Retrieves the move rect.
* Event handler for panel move entered notification.

#### Moving([Panel](Panel.md) panel,PanelMoveEvent e)
* **e.Rect[[Rect](../Rect.md)]**:Retrieves the move rect.
* Event handler for panel moving notification.

#### Moved([Panel](Panel.md) panel,PanelMoveEvent e)
* **e.Rect[[Rect](../Rect.md)]**:Retrieves the move rect.
* Event handler for panel moved notification.

#### MoveExited([Panel](Panel.md) panel,PanelMoveEvent e)
* **e.Rect[[Rect](../Rect.md)]**:Retrieves the move rect.
* Event handler for panel move exited notification.

#### ScaleChanged([Panel](Panel.md) panel,PanelScaleChangeEvent e)
* **e.OldScale[double]**:Retrieves the old scale.
* **e.NewScale[double]**:Retrieves the new scale.
* Event handler for panel scale changed notification.

#### TopStatusGained([Panel](Panel.md) panel,PanelTopStatusEvent e)
* **e.PreviousTopStatusPanel[[Panel](Panel.md)]**:Retrieves the previous top status panel.
* **e.NextTopStatusPanel[[Panel](Panel.md)]**:Retrieves the next top status panel.
* **e.ByUser[Boolean]**:Checks
* Event handler for panel top status gained notification.

#### TopStatusLost([Panel](Panel.md) panel,PanelTopStatusEvent e)
* **e.PreviousTopStatusPanel[[Panel](Panel.md)]**:Retrieves the previous top status panel.
* **e.NextTopStatusPanel[[Panel](Panel.md)]**:Retrieves the next top status panel.
* **e.ByUser[Boolean]**:Checks
* Event handler for panel top status lost notification.

#### WheelTracked([Panel](Panel.md) panel,PanelWheelTrackEvent e)
* **e.XTrackValue[short]**:Retrieves the x track value.
* **e.YTrackValue[short]**:Retrieves the y track value.
* **e.MouseOffset[[Point](../Point.md)]**:Retrieves the mouse position.
* **e.IsCommandPressed[Boolean]**:Checks if the command (control) button is pressed or not.
* **e.IsOptionPressed[Boolean]**:Checks if the option (alt) button is pressed or not.
* **e.IsShiftPressed[Boolean]**:Checks if the shift button is pressed or not.
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Mouse wheel track event for panels.

#### BackgroundPaint([Panel](Panel.md) panel,PanelBackgroundPaintEvent e)
* **e.Width[short]**:Retrieves the width.
* **e.Height[short]**:Retrieves the height.
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for panel background paint notification.

#### BackgroundPostPaint([Panel](Panel.md) panel,PanelBackgroundPaintEvent e)
* **e.Width[short]**:Retrieves the width.
* **e.Height[short]**:Retrieves the height.
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for panel background post paint notification.

#### ContextHelpRequested([Panel](Panel.md) panel,PanelHelpEvent e)
* **e.Item[[Item](../m_item/Item.md)]**:Retrieves a pointer to the item on which the help event occured.
* **e.Text[string]**:the application should specify a string here containing the tooltip text to be displayed. If the string is omitted DG tries to load the tooltip text from the resources.
* Event handler for panel context help requested notification.

#### ToolTipRequested([Panel](Panel.md) panel,PanelHelpEvent e)
* **e.Item[[Item](../m_item/Item.md)]**:Retrieves a pointer to the item on which the help event occured.
* **e.Text[string]**:the application should specify a string here containing the tooltip text to be displayed. If the string is omitted DG tries to load the tooltip text from the resources.
* Event handler for panel tool tip requested notification.

#### ContextMenuRequested([Panel](Panel.md) panel,PanelContextMenuEvent e)
* **e.Panel[[Panel](Panel.md)]**:
* **e.Item[[Item](../m_item/Item.md)]**:Retrieves a pointer to the item on which the context menu event occured.
* **e.Position[[Point](../Point.md)]**:Retrieves the mouse position of the context menu event.
* **e.NeedHelp[Boolean]**:
* **e.Processed[Boolean]**: if the application has processed this event, this value should be set to true to avoid the default event processing. By default the value of processed is false.
* Event handler for context menu requested notification.

#### WheelTrackEntered([Panel](Panel.md) panel,PanelWheelEvent e)
* **e.Item[[Item](../m_item/Item.md)]**:Retrieves the item above which the event occured.
* **e.Text[string]**:the application should specify a string here containing the tooltip text to be displayed. If the string is omitted DG tries to load the tooltip text from the resources.
* Event handler for mouse wheel track entered notification.

#### WheelTrackExited([Panel](Panel.md) panel,PanelWheelEvent e)
* **e.Item[[Item](../m_item/Item.md)]**:Retrieves the item above which the event occured.
* **e.Text[string]**:the application should specify a string here containing the tooltip text to be displayed. If the string is omitted DG tries to load the tooltip text from the resources.
* Event handler for mouse wheel track exited notification.

#### ChangeRegistrationRequested([Panel](Panel.md) panel,ChangeRegistrationRequestedEvent e)
* **e.Item[[Item](../m_item/Item.md)]**:Retrieves the item above which the event occured.
* **e.AllowRegistration[Boolean]**:
* Event handler for panel change registeration requested notification.

#### IsInputEnabled([Panel](Panel.md) panel,IsInputEnabledEvent e)
* **e.Item[[Item](../m_item/Item.md)]**:Retrieves the item above which the event occured.
* **InputStatus**: return value(default return **InputStatus_Default**)
* Event handler for panel is input enabled notification.