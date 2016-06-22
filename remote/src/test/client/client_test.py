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
import json
import unittest

sys.path.append('../')
from client.client import Nors_Client
from config.config import Nors_Configuration


class Test_Client(unittest.TestCase):
    def setUp(self):
        self.c = Nors_Client(config)
    
    def test_gettoken(self):
        token = self.c.conn.get_token()
        self.assertNotEqual(token, None)

    def test_get_protected_resource(self):
        rv, r = self.c.conn.get_resource('/sensors/')
        self.assertEqual(rv, 200)

    def test_post_protected_resource(self):
        data = json.dumps({"name":"p3", "idd":"1000"})
        rv, r = self.c.conn.post_resource('/sensors/', data)
#         r = self.c.conn.get_resource('/sensors/1')
        self.assertEqual(rv, 201)
    
    def tearDown(self):
        pass
        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg1 = sys.argv.pop()
        arg2 = sys.argv.pop()
    config = Nors_Configuration()
    unittest.main()
