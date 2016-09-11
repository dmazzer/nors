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
        
        #TODO: implement a token timeout to force token expiration
        # self.token_time_out = 300
        self.token = 'None'
        self.token_renew = True
        self._token_manager()
        
#     def check_connection(self):
#         
#         logger.log('Sending GET command to server:', 'debug')
#         headers = {'content-type': 'application/json'}
#         
#         rv, rt = self.get_resource('/server-info/')
#         if rv == 200:
#             return True
#         else:
#             return False
    
    
    def get_token(self):
        logger.log('----------------------------------------------------------', 'debug')
        logger.log('Requesting access token', 'debug')
        
        data = {"user": self.client_id, "pass": self.client_auth}
        request_string = 'http://' + self.server_ip + ':' + self.server_port + self.server_token_path
        logger.log('Request String: ' + request_string, 'debug')
        logger.log('Data String: ' + str(data), 'debug')
        
        r = None
        
        try:
            r = requests.post(request_string, 
                         headers={'content-type': 'application/json'},
                         data=json.dumps(data)
                         )
            
        except requests.exceptions.RequestException as e:
            logger.log('Error connection to Server: ' + str(e), 'error')
            return ''
        
        logger.log(r.text, 'debug')
        logger.log(r.headers, 'debug')
        if r.status_code == 200:
            return r.json()["access_token"]
        
        return ''
            
        
    def _token_manager(self):
        if self.token_renew is True:
            self.token_renew = False
            self.token = self.get_token()
            return self.token
        else:
            return self.token
        
    def renew_token(self):
        self.token_renew = True
    
    def get_resource(self, resource, data=None, headers={}):
        logger.log('----------------------------------------------------------', 'debug')
        logger.log('GET at resource ' + resource, 'debug')
        
        headers = headers.copy()
        headers['Authorization'] = 'JWT ' + self._token_manager()
        headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'
        
        if data is not None:
            logger.log('GET WITH DATA NOT IMPLEMENTED', 'debug')
            
        request_string = self.server_address + str(resource)
        logger.log('Request String: ' + request_string, 'debug')
        
        r = None

        try:
            r = requests.get(request_string, headers=headers)
        except requests.exceptions.RequestException as e:
            logger.log('Error when trying to connect to Server: ' + str(e), 'error')
            return None , None
        
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print "HTTP connection with Server error: ", e.message
            if r.status_code >= 400 and r.status_code < 500:
                logger.log('AUTH Response: ' + str(r.headers), 'debug')
                self.renew_token()
            return None , None

        logger.log('Response: ' + str(r.text), 'debug')
        logger.log('Headers: ' + str(r.headers), 'debug')
        logger.log('Return Code: ' + str(r.status_code), 'debug')
    
        if r.status_code == 200:
            if r.headers.get('content-type') == 'application/json':
                return r.status_code, r.json()
            else:
                return r.status_code, r.text
        else:
            return r.status_code, None
            
        return False        
        
    def post_resource(self, resource, data):
        if type(data) is dict:
            data_json = json.dumps(data, encoding='utf8')
        else:
            data_json = data
            
        rv, r = self._post_resource(resource, data_json)            
        return rv, r

    def _post_resource(self, resource, data_json, headers={}):
        logger.log('----------------------------------------------------------', 'debug')
        logger.log('POST at resource ' + resource, 'debug')
        
        headers = headers.copy()
        headers['Authorization'] = 'JWT ' + self._token_manager()
        headers['Content-Type'] = 'application/json'
        headers['Accept'] = 'application/json'

        request_string = self.server_address + str(resource)
        logger.log('Request String: ' + request_string, 'debug')
        
        r = None
        try:
            r = requests.post(request_string, data=data_json, headers=headers)
        except requests.exceptions.RequestException as e:
            logger.log('Error when trying to connect to Server: ' + str(e), 'error')
            return None , None
            
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print "HTTP connection with Server error: ", e.message
            if r.status_code >= 400 and r.status_code < 500:
                logger.log('AUTH Response: ' + str(r.headers), 'debug')
                self.renew_token()
            return None , None
            
        logger.log('Response: ' + str(r.text), 'debug')
        logger.log('Headers: ' + str(r.headers), 'debug')
        logger.log('Return Code: ' + str(r.status_code), 'debug')
   
        if r.status_code == 200:
            if r.headers.get('content-type') == 'application/json':
                return r.status_code, r.json()
            else:
                return r.status_code, r.text
        else:
            return r.status_code, None

        return False       
    