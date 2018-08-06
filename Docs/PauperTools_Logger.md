## Logger module

### Import
```
import PauperTools.Logger as Logger
``` 

### Example
[demo](../Scripts/Tests/logger_test.py)

### Testing
```
import Tests.logger_test as log_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        # logger module testing
        log_test.alert_test("alert_test message")

        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        print 'PyMain.FreeData' #must be print this message
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


