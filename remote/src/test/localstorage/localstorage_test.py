""" 
localstorage_test.py: LocalStorage test class

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys

sys.path.append('../')
from localstorage.localstorage import Nors_LocalStorage

import unittest

class Test_LocalStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Nors_LocalStorage()
        
    def test_db_connection(self):
        self.assertEqual(1, 1)
    
if __name__ == '__main__':
    unittest.main()
    