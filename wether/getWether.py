import threading
import time
import OnePleaceWether as op

class getWether(threading.Thread):
    def __init__(self,uri):
        self.check_type_uri(uri)
        self.uri = uri
        self.wether = op.OnePleaceWether(uri)

    def run(self):
        wether = self.wether.get_wether_with_update()
        

    def get_wether(self):
        pass
    
    def check_type_uri(self, uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')
