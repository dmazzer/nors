""" 
sensor_test.py: Sensor model test class

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


sys.path.append('../') # call test from 'test' folder
from models import remote

class Test_Remote(unittest.TestCase):
    def setUp(self):
        self.s = remote.Remote( 'ID', 'NAME', 'DESCRIPTION', 'ANYWHERE')
    
    def test_get(self):
        s1 = self.s.get()
        self.assertEqual(s1['name'], 'NAME')
        self.assertEqual(s1['remote_id'], 'ID')
        self.assertEqual(s1['description'], 'DESCRIPTION')
        self.assertEqual(s1['location'], 'ANYWHERE')
    
    def test_get_json(self):
        s1 = self.s.get_json(indentation=1)
        print(s1)
        
    def test_get_property(self):
        s1 = self.s.get_remote_property('description')
        self.assertEqual(s1, 'DESCRIPTION')
    
    def tearDown(self):
        pass
        

if __name__ == '__main__':
    unittest.main()
