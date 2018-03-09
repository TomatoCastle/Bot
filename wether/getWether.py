import threading
import time
import OnePleaceWether as op
import datetime

class getWether(threading.Thread):
    def __init__(self,uri,pushing_time):
        self.check_type_uri(uri)
        self.uri = uri
        self.check_type_time(pushing_time)
        self.pushing_time = pushing_time
        self.wether = op.OnePleaceWether(uri)
        self.now_wehter_json = None

    def run(self):
        pass

    def is_rain(self):
        pass

    def check_get_time(self,pushing_time):
        return None

    def get_wether(self):
        #wether = self.wether.get_wether_with_update()
        pass
    
    def update_uri(self):
        pass

    def check_type_time(self, pushing_time):
        if not isinstance(uri,datetime.datetime):
            raise TypeError('\"Callingtime\"\'s type must be \"datetime\"')

    def check_type_uri(self, uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')
