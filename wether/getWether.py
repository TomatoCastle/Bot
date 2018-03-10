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
        return self.get_wether()['today'] == '雨'
        #todo 3/10 雨時々の場合も雨と判定するようにする

    def is_now_pushing_time(self,pushing_time):
        now_time = datetime.datetime.now()
        return now_time.hour == pushing_time.hour
            and now_time.minute == pushing_time.minute

    def get_wether(self):
        return wether = self.wether.get_wether_with_update()
    
    def update_uri(self,uri):
        self.check_type_uri(uri)
        self.uri = uri
        self.wether = op.OnePleaceWether(uri)

    def check_type_time(self, pushing_time):
        if not isinstance(uri,datetime.datetime):
            raise TypeError('\"Callingtime\"\'s type must be \"datetime\"')

    def check_type_uri(self, uri):
        if not isinstance(uri,str):
            raise TypeError('\"uri\"\'s type must be \"str\"')
