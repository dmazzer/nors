""" 
client_test.py: Client test class

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys

sys.path.append('../')
from client.client import Nors_Client
from config.config import Nors_Configuration

import unittest

# def load_configuration():
#     config = Nors_Configuration('config_client_test.ini')
#     server_ip = config.ReadConfig('server', 'ip')
#     server_port = config.ReadConfig('server', 'port')
#     
#     client_auth = config.ReadConfig('client', 'auth')
#     client_id = config.ReadConfig('client', 'id')

class Test_Client(unittest.TestCase):
    def setUp(self):
        self.c = Nors_Client(config)
    
    def test_init(self):
        self.c.conn.get_token()

    def tearDown(self):
        pass
        
        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg1 = sys.argv.pop()
        arg2 = sys.argv.pop()
    config = Nors_Configuration()
    unittest.main()
