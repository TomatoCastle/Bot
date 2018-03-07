import threading
import time
import OnePleaceWether as op

class getWether(threading.Thread):
    def __init__(self,uri):
        self.check_type_uri(uri)
        self.uri = uri
        self.wether = op.OnePleaceWether(uri)
        self.now_wehter_json = None

    def run(self):
        pass
        
    def check_wether_is_rain(self):
        pass

    def check_get_time(self):
        return None

    def get_wether(self):
        #wether = self.wether.get_wether_with_update()
        pass
    
    def update_uri(self):
        pass

    def check_type_uri(self, uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')
