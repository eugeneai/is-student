from components import StudentLoader
import rpyc

conn=rpyc.classic.connect("localhost")
comps=conn.modules.components
comps.load_default_config()

class StudentLoader(object):
    def __init__(self, obj):
        self.loader=comps.StudentLoader(obj)
    def load(self):
        print ("REMOTE LOAD")
        return self.loader.load()
    def store(self):
        print ("REMOTE STORE")
        return self.loader.store()
