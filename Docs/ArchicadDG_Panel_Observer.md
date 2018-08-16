## PanelObserver Class

### Videos
* Youttube: https://youtu.be/khoufTCvBdY
* XiGua: https://url.cn/5MioU8r

### Import
```
from ArchicadDG import PanelObserver
``` 

### Example
[demo](../Scripts/Tests/dg_panel_observer_test.py)

### Testing
```
import Tests.dg_panel_observer_test as PanelObserver

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.pal=PanelObserver.FormPalette()
        self.pal.Show()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.pal=None
        print 'PyMain.FreeData' #must be print this message
        pass
        
```


### Class Functions

* **constructor([Panel](ArchicadDG_Panel.md) panel)**
* Class constructor.

### Class Events

#### CloseRequested([Panel](ArchicadDG_Panel.md) panel,PanelCloseRequestEvent e)
* **e.IsAccepted[Boolean]**:Retrieves whether the panel was accepted or not.
* **e.IsCancelled[Boolean]**:Retrieves whether the panel was cancelled or not.
* **e.Accepted[Boolean]**:if the application does not accept the close event, this value should be set to false, to avoid closing the dialog. By default this parameter is true. 
* Event handler for panel close requested notification.

#### HotkeyPressed([Panel](ArchicadDG_Panel.md) panel,PanelHotKeyEvent e)
* **e.KeyId[short]**:Retrieves the hotkey identifier.
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for hotkey pressed notification.

#### Idle([Panel](ArchicadDG_Panel.md) panel,PanelIdleEvent e)
* Event handler for panel idle notification.

#### Opened([Panel](ArchicadDG_Panel.md) panel,PanelOpenEvent e)
* **e.IsSavedPosition[Boolean]**:Tests whether the dialog position and size was restored from a previously saved rectangle or not.
* **e.IsDefaultPosition[Boolean]**:Tests whether the panel is opened in its default position.
* **e.IsAdjustedPosition[Boolean]**:Tests whether the restored position of the dialog was adjusted or not.
* Event handler for panel opened notification.

#### ResizeEntered([Panel](ArchicadDG_Panel.md) panel,PanelResizeEvent e)
* **e.IsUserResize[Boolean]**:Checks if the resize event occured as user interaction.
* **e.HorizontalChange[short]**:Retrieves the horizontal change.
* **e.VerticalChange[short]**:Retrieves the vertical change.
* Event handler for panel resize entered notification.

#### Resizing([Panel](ArchicadDG_Panel.md) panel,PanelResizingEvent e)
* **e.IsUserResize[Boolean]**:Checks if the resize event occured as user interaction.
* **e.HorizontalChange[short]**:Retrieves the horizontal change.
* **e.VerticalChange[short]**:Retrieves the vertical change.
* **e.GrowValues[[Point](ArchicadDG_Point.md)]**:Retrieves the grow values.
* Event handler for panel resizing notification.

#### Resized([Panel](ArchicadDG_Panel.md) panel,PanelResizeEvent e)
* **e.IsUserResize[Boolean]**:Checks if the resize event occured as user interaction.
* **e.HorizontalChange[short]**:Retrieves the horizontal change.
* **e.VerticalChange[short]**:Retrieves the vertical change.
* Event handler for panel resized notification.

#### ResizeExited([Panel](ArchicadDG_Panel.md) panel,PanelResizeEvent e)
* **e.IsUserResize[Boolean]**:Checks if the resize event occured as user interaction.
* **e.HorizontalChange[short]**:Retrieves the horizontal change.
* **e.VerticalChange[short]**:Retrieves the vertical change.
* Event handler for panel resize exited notification.

#### MoveEntered([Panel](ArchicadDG_Panel.md) panel,PanelMoveEvent e)
* **e.Rect[[Rect](ArchicadDG_Rect.md)]**:Retrieves the move rect.
* Event handler for panel move entered notification.

#### Moving([Panel](ArchicadDG_Panel.md) panel,PanelMoveEvent e)
* **e.Rect[[Rect](ArchicadDG_Rect.md)]**:Retrieves the move rect.
* Event handler for panel moving notification.

#### Moved([Panel](ArchicadDG_Panel.md) panel,PanelMoveEvent e)
* **e.Rect[[Rect](ArchicadDG_Rect.md)]**:Retrieves the move rect.
* Event handler for panel moved notification.

#### MoveExited([Panel](ArchicadDG_Panel.md) panel,PanelMoveEvent e)
* **e.Rect[[Rect](ArchicadDG_Rect.md)]**:Retrieves the move rect.
* Event handler for panel move exited notification.

#### ScaleChanged([Panel](ArchicadDG_Panel.md) panel,PanelScaleChangeEvent e)
* **e.OldScale[double]**:Retrieves the old scale.
* **e.NewScale[double]**:Retrieves the new scale.
* Event handler for panel scale changed notification.

#### TopStatusGained([Panel](ArchicadDG_Panel.md) panel,PanelTopStatusEvent e)
* **e.PreviousTopStatusPanel[[Panel](ArchicadDG_Panel.md)]**:Retrieves the previous top status panel.
* **e.NextTopStatusPanel[[Panel](ArchicadDG_Panel.md)]**:Retrieves the next top status panel.
* **e.ByUser[Boolean]**:Checks
* Event handler for panel top status gained notification.

#### TopStatusLost([Panel](ArchicadDG_Panel.md) panel,PanelTopStatusEvent e)
* **e.PreviousTopStatusPanel[[Panel](ArchicadDG_Panel.md)]**:Retrieves the previous top status panel.
* **e.NextTopStatusPanel[[Panel](ArchicadDG_Panel.md)]**:Retrieves the next top status panel.
* **e.ByUser[Boolean]**:Checks
* Event handler for panel top status lost notification.

#### WheelTracked([Panel](ArchicadDG_Panel.md) panel,PanelWheelTrackEvent e)
* **e.XTrackValue[short]**:Retrieves the x track value.
* **e.YTrackValue[short]**:Retrieves the y track value.
* **e.MouseOffset[[Point](ArchicadDG_Point.md)]**:Retrieves the mouse position.
* **e.IsCommandPressed[Boolean]**:Checks if the command (control) button is pressed or not.
* **e.IsOptionPressed[Boolean]**:Checks if the option (alt) button is pressed or not.
* **e.IsShiftPressed[Boolean]**:Checks if the shift button is pressed or not.
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Mouse wheel track event for panels.

#### BackgroundPaint([Panel](ArchicadDG_Panel.md) panel,PanelBackgroundPaintEvent e)
* **e.Width[short]**:Retrieves the width.
* **e.Height[short]**:Retrieves the height.
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for panel background paint notification.

#### BackgroundPostPaint([Panel](ArchicadDG_Panel.md) panel,PanelBackgroundPaintEvent e)
* **e.Width[short]**:Retrieves the width.
* **e.Height[short]**:Retrieves the height.
* **e.Processed[Boolean]**:if the application has processed this event, this value should be set to true, to avoid the default event processing. By default the value of processed is false.
* Event handler for panel background post paint notification.

#### ContextHelpRequested([Panel](ArchicadDG_Panel.md) panel,PanelHelpEvent e)
* **e.Item[[Item](ArchicadDG_Item.md)]**:Retrieves a pointer to the item on which the help event occured.
* **e.Text[string]**:the application should specify a string here containing the tooltip text to be displayed. If the string is omitted DG tries to load the tooltip text from the resources.
* Event handler for panel context help requested notification.

#### ToolTipRequested([Panel](ArchicadDG_Panel.md) panel,PanelHelpEvent e)
* **e.Item[[Item](ArchicadDG_Item.md)]**:Retrieves a pointer to the item on which the help event occured.
* **e.Text[string]**:the application should specify a string here containing the tooltip text to be displayed. If the string is omitted DG tries to load the tooltip text from the resources.
* Event handler for panel tool tip requested notification.

#### ContextMenuRequested([Panel](ArchicadDG_Panel.md) panel,PanelContextMenuEvent e)
* **e.Panel[[Panel](ArchicadDG_Panel.md)]**:
* **e.Item[[Item](ArchicadDG_Item.md)]**:Retrieves a pointer to the item on which the context menu event occured.
* **e.Position[[Point](ArchicadDG_Point.md)]**:Retrieves the mouse position of the context menu event.
* **e.NeedHelp[Boolean]**:
* **e.Processed[Boolean]**: if the application has processed this event, this value should be set to true to avoid the default event processing. By default the value of processed is false.
* Event handler for context menu requested notification.

#### WheelTrackEntered([Panel](ArchicadDG_Panel.md) panel,PanelWheelEvent e)
* **e.Item[[Item](ArchicadDG_Item.md)]**:Retrieves the item above which the event occured.
* **e.Text[string]**:the application should specify a string here containing the tooltip text to be displayed. If the string is omitted DG tries to load the tooltip text from the resources.
* Event handler for mouse wheel track entered notification.

#### WheelTrackExited([Panel](ArchicadDG_Panel.md) panel,PanelWheelEvent e)
* **e.Item[[Item](ArchicadDG_Item.md)]**:Retrieves the item above which the event occured.
* **e.Text[string]**:the application should specify a string here containing the tooltip text to be displayed. If the string is omitted DG tries to load the tooltip text from the resources.
* Event handler for mouse wheel track exited notification.

#### ChangeRegistrationRequested([Panel](ArchicadDG_Panel.md) panel,ChangeRegistrationRequestedEvent e)
* **e.Item[[Item](ArchicadDG_Item.md)]**:Retrieves the item above which the event occured.
* **e.AllowRegistration[Boolean]**:
* Event handler for panel change registeration requested notification.

#### IsInputEnabled([Panel](ArchicadDG_Panel.md) panel,IsInputEnabledEvent e)
* **e.Item[[Item](ArchicadDG_Item.md)]**:Retrieves the item above which the event occured.
* **InputStatus**: return value(default return **InputStatus_Default**)
* Event handler for panel is input enabled notification.