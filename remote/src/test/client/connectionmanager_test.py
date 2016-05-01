"""
connectionmanager_test.py: Connection Manager test class

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys

sys.path.append('../')
from client.connectionmanager import Nors_ConnectionManager

import unittest

class Nors_ConnectionManager_Test(unittest.TestCase):
    def setUp(self):
        cm = Nors_ConnectionManager()


        
    def tearDown(self):
        pass
        
if __name__ == '__main__':
    unittest.main()
    