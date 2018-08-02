## Thread 

### Example
[demo](Scripts/Tests/thread_test.py)


### Testing
```
import Tests.thread_test as threading_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        #threading testing
        threading_test.run()
        
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        #threading testing
        threading_test.stop();
        print 'PyMain.FreeData' #must be print this message
        pass

```
