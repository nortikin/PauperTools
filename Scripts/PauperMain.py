import Tests.thread_test as threading_test
import Tests.logger_test as log_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self):
        # logger module testing
        #log_test.alert_test("alert_test message")

        #threading testing
        #threading_test.run()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        #threading testing
        #threading_test.stop();
        print 'PyMain.FreeData' #must be print this message
        pass