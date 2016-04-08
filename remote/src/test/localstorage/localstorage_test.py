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
from localstorage.dao import Nors_LocalStorage_DAO

import unittest

class Test_LocalStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Nors_LocalStorage('testDB')

        self.test_data1 = {'field1': 100, 'field2': 'lucky', 'date': '2016-04-06 06:40:41.758893'}
        self.test_data2 = {'field1': 200, 'field2': 'almost', 'date': '2016-04-06 06:42:41.758893'}
        self.test_data3 = {'field1': 300, 'field2': 'sunnny', 'date': '2016-04-06 06:44:41.758893'}
        self.test_data4 = {'field1': 400, 'field2': 'yards', 'date': '2016-04-06 06:46:41.758893'}
        
    def test_db_data_insert(self):
        self.assertNotEqual(self.storage.store(self.test_data1), None)
        self.assertNotEqual(self.storage.store(self.test_data2), None)
        self.assertNotEqual(self.storage.store(self.test_data3), None)
        self.assertNotEqual(self.storage.store(self.test_data4), None)

    def tearDown(self):
        storage = Nors_LocalStorage_DAO('testDB', 'mongodb://localhost:27017/')
        storage.dropCollection('testDB')
        storage.dropDB()
        
        

if __name__ == '__main__':
    unittest.main()
    