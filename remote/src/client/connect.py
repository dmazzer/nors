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
    def __init__(self, server_ip, 
                 server_port, 
                 server_api_path, 
                 server_token_path, 
                 client_auth, 
                 client_id):
        
        
        self.server_ip = server_ip
        self.server_port = server_port
        self.server_api_path = server_api_path, 
        self.server_token_path = server_token_path  
        self.client_auth = client_auth 
        self.client_id = client_id

        self.server_address = 'http://' + server_ip + ':' + server_port + server_api_path 
        
        logger.log('Sending GET command to server:', 'debug')
        headers = {'content-type': 'application/json'}
        r = requests.get('http://' +server_ip+':'+server_port+'/server-info',headers=headers)
        logger.log('Response:', 'debug')
        logger.log(r.text, 'debug')
        logger.log('Headers:', 'debug')
        logger.log(r.headers, 'debug')
    
    def get_token(self):
        logger.log('Requesting access token', 'debug')
        
        data = {"user": self.client_id, "pass": self.client_auth}
        
        r = requests.post('http://' + self.server_ip + ':' + self.server_port + self.server_token_path, 
                         headers={'content-type': 'application/json'},
                         data={"user": "user1", "pass": "abcxyz"}
                         )
        
        logger.log(r.text, 'debug')
        logger.log(r.headers, 'debug')
        
        if r.status_code == 200:
            return r.json()["token"]
            



