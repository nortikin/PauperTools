## EditControl Inheritance Diagram

<img src="../../../Imgs/edit_control_inheritance_diagram.png" />

## EditControl Examples

### Videos
* Youttube: https://youtu.be/d6qyalsb0Vs

### Example
* [demo](../../Scripts/Tests/dg_edit_test.py)

### Testing
```
import Tests.dg_edit_test as edit_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        #new Form
        self.frm=edit_test.PaletteForm()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        #free Form
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass

```

## Class List

* [EditControl](EditControl.md)
* [PosIntEdit](PosIntEdit.md) 
* [PosIntEditObserver](PosIntEdit_Observer.md)
* [IntEdit](IntEdit.md) 
* [IntEditObserver](IntEdit_Observer.md)
* [RealEdit](RealEdit.md) 
* [RealEditObserver](RealEdit_Observer.md)
* [LengthEdit](LengthEdit.md)
* [AngleEdit](AngleEdit.md)
* [PolarAngleEdit](PolarAngleEdit.md)
* [MMPointEdit](MMPointEdit.md)
* [TextEditBase](TextEditBase.md) 
* [TextEditBaseObserver](TextEditBase_Observer.md)
* [TextEdit](TextEdit.md)
* [PasswordEdit](PasswordEdit.md)
* [ShortcutEdit](ShortcutEdit.md) 
* [ShortcutEditObserver](ShortcutEdit_Observer.md)
* [MultiLineEdit](MultiLineEdit.md)
* [EditDragSourceObserver](EditDragSource_Observer.md)
* [EditDropTargetObserver](EditDropTarget_Observer.md)

## Enum List

* [EditControl.AbsRelType](EditControl_AbsRelType.md)
* [EditControl.FrameType](EditControl_FrameType.md)
* [EditControl.ReadOnlyType](EditControl_ReadOnlyType.md)
* [EditControl.UpdateType](EditControl_UpdateType.md)
* [LengthEdit.ChangeFontType](LengthEdit_ChangeFontType.md)
* [MultiLineEdit.ScrollType](MultiLineEdit_ScrollType.md)
