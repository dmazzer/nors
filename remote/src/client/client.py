""" 
client.py:  

"""
__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS Project"
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"


import requests
import json

class Nors_Client():
    def __init__(self):
        pass
    
    
    


r = requests.get('http://httpbin.org/ip')
print r.text

print '-----'
r = requests.get('http://127.0.0.1:8080/v1/clients?limit=1')
print r.text
print r.headers

print '-----'

data = json.dumps({'sensor_data':"{'test':'q'}"}) 
headers = {'content-type': 'application/json'}
r = requests.post('http://127.0.0.1:8080/v1/clients/client1', data, headers=headers)
print r.text


if __name__ == '__main__':
    
    sys.path.append('../')
    from norsutils.logmsgs.logger import Logger
    logger = Logger()
    logger.log("GenericSensor started by command line")
    sensor = Nors_GenericSensor()
    sensor.SignIn()

    def do_exit(sig, stack):
        raise SystemExit('Exiting')
    
    signal.signal(signal.SIGINT, do_exit)
    signal.signal(signal.SIGUSR1, do_exit)
    
    signal.pause()    
    
else:
    sys.path.append('../')
    from norsutils.logmsgs.logger import Logger
    logger = Logger()
