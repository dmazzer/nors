""" 
client.py:  

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS Project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

    # TODO: 
    # Conectar no DB local
    # Autenticar (registrar) no servidor
    # coletar dado do db local e enviar para o servidor
    # receber notificacao do servidor

import requests
import json
import sys

sys.path.append('../')
from norsutils.logmsgs.logger import Logger
logger = Logger('debug')

from connect import Nors_Connect
from models.remote import Remote

logger.log("NORS Client started", 'debug')

class Nors_Client():
    def __init__(self, config):
        
        self.config = config;
        self.load_configuration()
        
        client_information = Remote(self.client_id, self.client_name, self.client_description, self.client_location)
        
        self.conn = Nors_Connect(self.server_ip, 
                            self.server_port, 
                            self.server_api_path, 
                            self.server_token_path, 
                            self.client_auth,
                            client_information)
    
    
    def load_configuration(self):
        self.server_ip = self.config.ReadConfig('server', 'ip')
        self.server_port = self.config.ReadConfig('server', 'port')
        self.server_api_path = self.config.ReadConfig('server', 'api_path')
        self.server_token_path = self.config.ReadConfig('server', 'token_path')
        
        self.client_id = self.config.ReadConfig('client', 'id')
        self.client_auth = self.config.ReadConfig('client', 'auth')
        self.client_name = self.config.ReadConfig('client', 'nickname')
        self.client_description = self.config.ReadConfig('client', 'description')
        self.client_location = self.config.ReadConfig('client', 'location')

        
        

# r = requests.get('http://httpbin.org/ip')
# print r.text
# 
# print '-----'
# r = requests.get('http://127.0.0.1:8080/v1/clients?limit=1')
# print r.text
# print r.headers
# 
# print '-----'
# 
# data = json.dumps({'sensor_data':"{'test':'q'}"}) 
# headers = {'content-type': 'application/json'}
# r = requests.post('http://127.0.0.1:8080/v1/clients/client1', data, headers=headers)
# print r.text
    
