## Logger module

### Videos
* Youtube: https://youtu.be/cAELRQT4ZoM
* XiGua: https://url.cn/5HCujoP

### Import
```
import PauperTools.Logger as Logger
``` 

### Testing
```
from PauperTools import Logger

class PyMain(object):
    def __init__(self):
        Logger.alert('PT.__init__')
        print 'LPT.__init__'
        pass

    def RegisterInterface(self):
        Logger.alert('PT.RegisterInterface')
        print 'LPT.RegisterInterface' #in reload mode;this function not called
        pass
    
    def Initialize(self,reload):
        Logger.alert('PT.Initialize mode:'+str(reload))
        print 'LPT.Initialize'
        pass

    def FreeData(self):
        Logger.alert('PT.FreeData')
        print 'LPT.FreeData'
        pass


```
### Static Functions

* **alert(string msg)**
* **None**
* alert message from info window
```
Logger.alert(msg)
```


* **write(string msg)**
* **None**
* print message to report window

```
Logger.write(msg)
```


