from threading import *
import time
class new_thread(Thread):
    def __init__(self):
        self.running=True; # thread running control flag,default is True
        super(new_thread, self).__init__()
    def run(self):
        while self.running:
            # threading loop
            print "new_thread is running11111 1234"
            time.sleep(3)
        # thread stopping
        print "new_thread stop"
    def stop(self):
        self.running=False # stop thread 
        self.join() #wait thread exit

new_t=new_thread()

def run():
    new_t.start()

def stop():
    new_t.stop()
    
