import threading
import time
import OnePleaceWether as op

class getWether(threading.Thread):
    def __init__(self,uri):
        self.check_type_uri(uri)
        self.uri = uri
        self.wether = op.OnePleaceWether(uri)

    def check_type_uri(self,uri):
        pass

    def run(self):
        pass

    def get_wether(self):
        pass
    
    def check_uri_type(self, uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')
