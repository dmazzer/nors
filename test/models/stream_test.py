""" 
stream_test.py: Stream model test class

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
from models import stream

class Test_Stream(unittest.TestCase):
    def setUp(self):
        self.s1 = stream.Stream(sensor_id='ID1', stream_names=['NAME'])
        self.s2 = stream.Stream(sensor_id='ID2', stream_names=['NAME1', 'NAME2', 'NAME3'])
    
    def test_get_stream(self):
        ss1 = self.s1.get_stream()
        self.assertEqual(str(ss1),"{'timestamp': 0, 'sensor_id': 'ID1', 'streams': {'NAME': 0}}")
        ss2 = self.s2.get_stream()
        self.assertEqual(str(ss2),"{'timestamp': 0, 'sensor_id': 'ID2', 'streams': {'NAME2': 0, 'NAME3': 0, 'NAME1': 0}}")
        
    def test_get_stream_json(self):
        ss1 = self.s1.get_stream_json()
        self.assertEqual(json.loads(ss1),{u'timestamp': 0, u'sensor_id': u'ID1', u'streams': {u'NAME': 0}})
        
    def test_set_values(self):
        self.s1.set_values({'NAME': 10})
        ss1 = self.s1.get_stream_json()
        ss1d = json.loads(ss1)
        self.assertEqual(ss1d['streams']['NAME'], 10)
        
        self.s2.set_values({'NAME1': 1,'NAME2': 2,'NAME3': 3})
        ss2 = self.s2.get_stream_json()
        ss2d = json.loads(ss2)
        self.assertEqual(ss2d['streams']['NAME1'], 1)
        self.assertEqual(ss2d['streams']['NAME2'], 2)
        self.assertEqual(ss2d['streams']['NAME3'], 3)
    
    def tearDown(self):
        pass
        

if __name__ == '__main__':
    unittest.main()
