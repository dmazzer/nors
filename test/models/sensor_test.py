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
from models import sensor

class Test_Client(unittest.TestCase):
    def setUp(self):
        self.s = sensor.Sensor('ID', 'NAME', 'DESCRIPTION', sensor.SensorInterface.analog)
    
    def test_get_sensor(self):
        s1 = self.s.get_sensor()
        self.assertEqual(s1['name'], 'NAME')
        self.assertEqual(s1['sensor_id'], 'ID')
        self.assertEqual(s1['description'], 'DESCRIPTION')
        self.assertEqual(s1['interface'], sensor.SensorInterface.analog)
        self.assertEqual(s1['stream'], [])
    
    def test_add_get_stream(self):
        self.assertEqual(self.s.get_stream_num(), 0)
        self.s.add_stream('st1', 'des1')
        self.assertEqual(self.s.get_stream_num(), 1)
        self.s.add_stream('st2', 'des2')
        self.assertEqual(self.s.get_stream_num(), 2)

    def test_get_sensor_json(self):
        s1 = self.s.get_sensor_json(indentation=1)
        print(s1)
        self.s.add_stream('st1', 'des1')
        s1 = self.s.get_sensor_json(indentation=1)
        print(s1)
        
        
    
    def tearDown(self):
        pass
        

if __name__ == '__main__':
    unittest.main()
