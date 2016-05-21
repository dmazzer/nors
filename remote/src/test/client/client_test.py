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
from nors import load_configuration
from config.config import Nors_Configuration

import unittest

class Test_Client(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_init(self):
        config = load_configuration()
        c = Nors_Client(config)

    def tearDown(self):
        pass
        
        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg1 = sys.argv.pop()
        arg2 = sys.argv.pop()
    config = Nors_Configuration()
    unittest.main()
