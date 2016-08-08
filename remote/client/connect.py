""" 
connect.py: Authenticate and register on remote server   

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS Project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"


import json
import requests

from norsutils.logmsgs.logger import Logger
logger = Logger()

class Nors_Connect():
    def __init__(self, server_ip, 
                 server_port, 
                 server_api_path, 
                 server_token_path, 
                 client_auth,
                 client_information):
        
        
        self.server_ip = server_ip
        self.server_port = server_port
        self.server_api_path = server_api_path
        self.server_token_path = server_token_path  
        self.client_auth = client_auth 
        self.client_id = client_information.get_remote_property('remote_id')

        self.server_address = 'http://' + server_ip + ':' + server_port + server_api_path 
        
    def check_connection(self):
        
        logger.log('Sending GET command to server:', 'debug')
        headers = {'content-type': 'application/json'}
        
        rv, rt = self.get_resource('/server-info/')
        if rv == 200:
            return True
        else:
            return False
    
    
    def get_token(self):
        logger.log('----------------------------------------------------------', 'debug')
        logger.log('Requesting access token', 'debug')
        
        data = {"user": self.client_id, "pass": self.client_auth}
        request_string = 'http://' + self.server_ip + ':' + self.server_port + self.server_token_path
        logger.log('Request String: ' + request_string, 'debug')
        logger.log('Data String: ' + str(data), 'debug')
        
        try:
            r = requests.post(request_string, 
                         headers={'content-type': 'application/json'},
                         data=json.dumps(data)
                         )
        except requests.exceptions.RequestException as e:
            logger.log('Error connection to Server: ' + str(e), 'error')
            return None
        else:
            logger.log(r.text, 'debug')
            logger.log(r.headers, 'debug')
            if r.status_code == 200:
                return r.json()["access_token"]
        
    #@staticmethod
    def _token_manager(self, renew=False):
        if renew is True:
            token = self.get_token()
        else:
            #TODO: Implement some logic to manage token life cycle and dont get a new token every time
            token = self.get_token()
        
        return token
    
    def _get_resource(self, resource, token, data=None, headers={}):
        logger.log('----------------------------------------------------------', 'debug')
        logger.log('GET at resource ' + resource, 'debug')
        
        headers = headers.copy()
        headers['Authorization'] = 'JWT ' + token
        headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'
        
        # TODO:
        if data is not None:
            logger.log('GET WITH DATA NOT IMPLEMENTED', 'debug')
            
        request_string = self.server_address + str(resource)
        logger.log('Request String: ' + request_string, 'debug')
        
        try:
            r = requests.get(request_string, headers=headers)
        except requests.exceptions.RequestException as e:
            logger.log('Error connection to Server: ' + str(e), 'error')
            return requests.Response.raise_for_status() , None
        else:
            logger.log('Response:', 'debug')
            logger.log(r.text, 'debug')
            logger.log('Headers:', 'debug')
            logger.log(r.headers, 'debug')
            logger.log('Return Code:', 'debug')
            logger.log(r.status_code, 'debug')
        
            if r.status_code == 200:
                if r.headers.get('content-type') == 'application/json':
                    return r.status_code, r.json()
                else:
                    return r.status_code, r.text
            else:
                return r.status_code, None
            
        
    def _post_resource(self, resource, token, data_json, headers={}):
        logger.log('----------------------------------------------------------', 'debug')
        logger.log('POST at resource ' + resource, 'debug')
        
        headers = headers.copy()
        headers['Authorization'] = 'JWT ' + token
        headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'

#         headers = {'content-type': 'application/json',
#                    'Authorization': 'JWT ' + token}
        
        request_string = self.server_address + str(resource)
        logger.log('Request String: ' + request_string, 'debug')
        
        try:
            r = requests.post(request_string, data=data_json, headers=headers)
        except requests.exceptions.RequestException as e:
            logger.log('Error connection to Server: ' + str(e), 'error')
            return requests.Response.raise_for_status() , None
        else:
            logger.log('Response:', 'debug')
            logger.log(r.text, 'debug')
            logger.log('Headers:', 'debug')
            logger.log(r.headers, 'debug')
            logger.log('Return Code:', 'debug')
            logger.log(r.status_code, 'debug')
       
            if r.status_code == 200:
                if r.headers.get('content-type') == 'application/json':
                    return r.status_code, r.json()
                else:
                    return r.status_code, r.text
            else:
                return r.status_code, None
            

           
        
    def get_resource(self, resource, data=None):
        # TODO: If the return is 40x because an expired token, this should trigger a new token request
        t = token=self._token_manager(renew=True)
        if t is not None:
            return self._get_resource(resource, data=None, token=t)
        else:
            return None, None
    
    def post_resource(self, resource, data):
        if type(data) is dict:
            data_json = json.dumps(data, encoding='utf8')
        else:
#             logger.log('POST ERROR: data is not dict, sending as is...', 'debug')
            data_json = data
            
        t = token=self._token_manager(renew=True)
        if t is not None:
            return self._post_resource(resource, t, data_json)
        else:
            return None, None
    
    
        
            
            
                
        
