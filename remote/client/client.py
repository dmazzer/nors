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

from threading import Thread
import Queue
import time
import sys

# sys.path.append('../')
from norsutils.logmsgs.logger import Logger
logger = Logger('debug')

from connect import Nors_Connect

sys.path.append('../')
sys.path.append('../../')
from models.remote import Remote
from models.stream import Stream

logger.log("NORS Client started", 'debug')

class Nors_Client():
    def __init__(self, config, local_storage, autoinit_check_for_local_data=True):
        
        logger.log('Client/Remote started', 'debug')
        
        self.config = config
        self.local_storage = local_storage

        self.server_ip = self.config.ReadConfig('server', 'ip')
        self.server_port = self.config.ReadConfig('server', 'port')
        self.server_api_path = self.config.ReadConfig('server', 'api_path')
        self.server_token_path = self.config.ReadConfig('server', 'token_path')
        
        self.client_id = self.config.ReadConfig('client', 'id')
        self.client_auth = self.config.ReadConfig('client', 'auth')
        self.client_name = self.config.ReadConfig('client', 'name')
        self.client_description = self.config.ReadConfig('client', 'description')
        self.client_location = self.config.ReadConfig('client', 'location')
        
        self.check_for_local_data_interval = float(self.config.ReadConfig('options', 'check_for_local_data_interval'))
        self.send_local_data_interval = float(self.config.ReadConfig('options', 'send_local_data_interval'))
        
        client_information = Remote(self.client_id, self.client_name, self.client_description, self.client_location)

        self.conn = Nors_Connect(self.server_ip, 
                            self.server_port, 
                            self.server_api_path, 
                            self.server_token_path, 
                            self.client_auth,
                            client_information)

#         if self.conn.check_connection() is True:
#             #precisa???
#             pass

        # Usually the ckeck_for_local_data should always run at class init,
        # this verification is done to allow a way to test _update_remote 
        # as a method instead of a thead
        if autoinit_check_for_local_data == True:
            self.check_for_local_data()

    def check_for_local_data(self):
        timer_thread = Thread(target=self.check_for_local_data_worker, name='CheckForLocalData')
        timer_thread.daemon = True
        timer_thread.start()

#     def check_for_local_data_worker(self):
#         self.next_call = time.time()
#         while True:
#             self.next_call = self.next_call + self.check_for_local_data_interval;
#             
#             self._update_remote()
#             
#             timer_delta = self.next_call - time.time()
#             if timer_delta > 0:
#                 time.sleep(self.next_call - time.time())
    
    def check_for_local_data_worker(self):
        while True:
            self._update_remote()
            time.sleep(self.check_for_local_data_interval)
    
    def _update_local(self):
        pass

    def _update_remote(self):
        # TODO: Before send the data must be arranged against a model 
        connection_failed = False
        data_to_send = self.local_storage.get_first()
        while (len(data_to_send) > 0 ) and (connection_failed is False):
            data_id = data_to_send[0]['_id']
            data_to_send[0].pop('_id')
            logger.log('Update Remote: sending id: ' + str(data_id), 'debug')
            rv, r = self.conn.post_resource('/streams/', data_to_send[0])
            
            if rv == 201:
                result = self.local_storage.delete(data_id)
                if result == 0:
                    logger.log('Item not found on database', 'debug')
                else:
                    logger.log('Item deleted from database', 'debug')
            else:
                connection_failed = True
                logger.log('Post data to server failed', 'error')
                
                # check if the failure reason is an expired token 
                if rv == 401:
                    print (r)
                    print (rv)
            
            data_to_send = self.local_storage.get_first()
            
            time.sleep(self.send_local_data_interval)
            
        return connection_failed

    def _pop_sensor_data(self):
        pass
    
    def _push_actuator_data(self):
        pass
