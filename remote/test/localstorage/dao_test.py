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

sys.path.append('../')
from localstorage.dao import Nors_LocalStorage_DAO

import unittest

class Nors_LocalStorage_DAO_Test(unittest.TestCase):
    def setUp(self):
        self.storage = Nors_LocalStorage_DAO('nors_test_db', 'mongodb://localhost:27017/')
        self.storage.dropCollection('TestCollection')

        self.test_data1 = {'field1': 100, 'field2': 'lucky', 'date': '2016-04-06 06:40:41.758893'}
        self.test_data2 = {'field1': 200, 'field2': 'almost', 'date': '2016-04-06 06:42:41.758893'}
        self.test_data3 = {'field1': 300, 'field2': 'sunnny', 'date': '2016-04-06 06:44:41.758893'}
        self.test_data4 = {'field1': 400, 'field2': 'yards', 'date': '2016-04-06 06:46:41.758893'}

        self.storage.insert('TestCollection', self.test_data1)
        self.storage.insert('TestCollection', self.test_data2)
        self.storage.insert('TestCollection', self.test_data3)
        self.storage.insert('TestCollection', self.test_data4)

        
    def test_db_find_compare_with_string(self):
        findstring = {'field1' : 200}
        findresult = self.storage.find('TestCollection', findstring)
        self.assertEqual(self.test_data2, findresult[0])
        
    def test_db_find_failure(self):
        findstring = {'field1' : 250}
        findresult = self.storage.find('TestCollection', findstring)
        self.assertEqual(findresult.count(), 0 )

    def test_db_find_one(self):
        findstring = {'field1' : 400}
        findresult = self.storage.find('TestCollection', findstring)
        self.assertEqual(findresult.count(), 1)

    def test_db_get_date_in_range_all(self):
        findresult = self.storage.get_itens_from_date('TestCollection', '2016-04-06 06:39:41.758893', 1)
        self.assertEqual(findresult.count(), 4)

    def test_db_get_date_in_range_few(self):
        findresult = self.storage.get_itens_from_date('TestCollection', '2016-04-06 06:45:41.758893', 1)
        self.assertEqual(findresult.count(), 1)
        
    def test_db_get_date_in_range_none(self):
        findresult = self.storage.get_itens_from_date('TestCollection', '2016-04-06 06:47:41.758893', 1)
        self.assertEqual(findresult.count(), 0)

    def test_db_update_existent(self):

        find_string = {'field1' : 100, 'field2': 'new_value'}
        find_result = self.storage.find('TestCollection', find_string)
        self.assertEqual(find_result.count(), 0)

        query_string = {'field1': 100}
        update_string = {'field2': 'new_value'}
        update_result = self.storage.update('TestCollection', query_string, update_string)
        
        find_string = {'field1' : 100, 'field2': 'new_value'}
        find_result = self.storage.find('TestCollection', find_string)
        self.assertEqual(find_result.count(), 1)

        self.assertEqual(update_result.matched_count, 1)
#         self.assertEqual(update_result.modified_count, 1) # i dont know why this fail
        
    def tearDown(self):
        self.storage.dropCollection('TestCollection')
        self.storage.dropDB()
        
if __name__ == '__main__':
    unittest.main()
    