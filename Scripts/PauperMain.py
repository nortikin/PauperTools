import Tests.thread_test as threading_test
import Tests.logger_test as log_test
from PauperTools import Logger
class PyMain(object):
    def __init__(self):
        pass

    def RegisterInterface(self):
        print 'PauperMain:RegisterInterface'
        pass
    
    def Initialize(self):
        # logger module testing
        #log_test.alert_test("alert_test message")

        #threading testing
        #threading_test.run()
        print 'PauperMain:Initialize'
        pass

    def FreeData(self):
        #threading testing
        #threading_test.stop();
        print 'PauperMain:FreeData'
        pass
