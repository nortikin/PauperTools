
import Tests.dg_pushmenu_test as pushmenu_test

class PyMain(object):
    def __init__(self):
        print "PyMain.__init__" #must be print this message
        pass

    def RegisterInterface(self):
        print 'PyMain.RegisterInterface' #must be print this message
        pass
    
    def Initialize(self,reload):
        self.frm=pushmenu_test.Form()
        self.frm.Show()
        print 'PyMain.Initialize' #must be print this message
        pass

    def FreeData(self):
        self.frm=None
        print 'PyMain.FreeData' #must be print this message
        pass
