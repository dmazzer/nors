#!/usr/bin/env python2

""" 
dao_test.py: dao test class

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys
import signal

sys.path.append('../')
from localstorage.dao import Nors_LocalStorage_DAO

import unittest

class Nors_LocalStorage_DAO_Test(unittest.TestCase):
    def setUp(self):
        self.storage = Nors_LocalStorage_DAO('nors_test_db', 'mongodb://localhost:27017/')
        
    def test_db_insert(self):
        test_data = {'field1': 100, 'filed2': 'lucky'}
        post_id = self.storage.insert('TestCollection', test_data)
        self.assertNotEqual(post_id, None)
        
    def test_db_find(self):
        
    
if __name__ == '__main__':
    unittest.main()
    