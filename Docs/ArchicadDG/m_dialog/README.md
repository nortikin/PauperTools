## Form Inheritance Diagram

<img src="../../../Imgs/form_inheritance_diagram.png" width="384px" height="384px" />

## Palette Example
### Videos
* Youttube: https://youtu.be/pPnnZp-fLGY
* XiGua: https://url.cn/54P5PTU

### Example
* [palette demo](../../../Scripts/Tests/dg_palette_test.py)

### Testing
```
from Tests.dg_palette_test import *

class PyMain(object):
    def __init__(self):
        self.pal=FormPalette()
        pass

    def RegisterInterface(self):
        pass
    
    def Initialize(self,reload):
        pass

    def FreeData(self):
        self.pal=None # free FormPalette
        pass
```

## Class List

* [Dialog](Dialog.md)
* [ModalDialog](ModalDialog.md)
* [ModelessBase](ModelessBase.md)
* [ModelessDialog](ModelessDialog.md)
* [ModelessDialog](ModelessDialog.md)


## Enum List

* [Dialog.CaptionType](Dialog_CaptionType.md)
* [Dialog.CloseType](Dialog_CloseType.md)
* [Dialog.DialogType](Dialog_DialogType.md)
* [Dialog.FixPoint](Dialog_FixPoint.md)
* [Dialog.FrameType](Dialog_FrameType.md)
* [Dialog.GrowBoxForm](Dialog_GrowBoxForm.md)
* [Dialog.GrowType](Dialog_GrowType.md)
* [Dialog.MaximizeType](Dialog_MaximizeType.md)
* [Dialog.MinimizeType](Dialog_MinimizeType.md)
* [Dialog.SpecialFeatures](Dialog_SpecialFeatures.md)
* [ModalDialog.ModalResponse](ModalDialog_ModalResponse.md)
* [ModelessBase.DialogStatus](ModelessBase_DialogStatus.md)
* [ModelessDialog.DialogState](ModelessDialog_DialogState.md)
* [ModelessDialog.DockState](ModelessDialog_DockState.md)
