""" 
connect.py: Authenticate and register on remote server   

"""
__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS Project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"


from norsutils.logmsgs.logger import Logger
logger = Logger('debug')

import requests

class Nors_Connect():
    def __init__(self, server_ip, server_port, client_auth, client_id):
        
        logger.log('Sending GET command to server:', 'debug')
        headers = {'content-type': 'application/json'}
        r = requests.get('http://' +server_ip+':'+server_port+'/v1/server/info',headers=headers)
        logger.log('Response:', 'debug')
        logger.log(r.text, 'debug')
        logger.log('Headers:', 'debug')
        logger.log(r.headers, 'debug')
    
    def sign_in(self):
        pass
    
    def auth(self):
        pass
        
        


