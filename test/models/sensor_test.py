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

class Test_Sensor(unittest.TestCase):
    def setUp(self):
        self.s = sensor.Sensor( 'ID', 'NAME', 'DESCRIPTION', sensor.SensorInterface.analog, 2, 1)
    
    def test_get_sensor(self):
        s1 = self.s.get_sensor()
        self.assertEqual(s1['name'], 'NAME')
        self.assertEqual(s1['sensor_id'], 'ID')
        self.assertEqual(s1['description'], 'DESCRIPTION')
        self.assertEqual(s1['interface'], sensor.SensorInterface.analog)
        self.assertEqual(s1['stream'], [])
        self.assertEqual(s1['pull_interval'], 2)
        self.assertEqual(s1['read_interval'], 1)
    
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
        
    def test_get_property(self):
        s1 = self.s.get_property('description')
        self.assertEqual(s1, 'DESCRIPTION')

    def test_get_stream_property1(self):
        self.s.add_stream('st1', 'des1', value_max=2)
        self.s.add_stream('st2', 'des2', value_max=3)
        s1 = self.s.get_stream_property('st1', 'value_max')
        self.assertEqual(s1, 2)
    
    def test_get_stream_property2(self):
        self.s.add_stream('st1', 'des1', value_max=2)
        self.s.add_stream('st2', 'des2', value_max=3)
        s1 = self.s.get_stream_property('st2', 'value_max')
        self.assertEqual(s1, 3)
        
    def test_get_stream_property3(self):
        self.s.add_stream('st1', 'des1', value_max=2)
        self.s.add_stream('st2', 'des2', value_max=3)
        s1 = self.s.get_stream_property('st3', 'value_max')
        self.assertEqual(s1, None)

    def test_set_stream_property1(self):
        self.s.add_stream('st1', 'des1', value_max=2)
        self.s.add_stream('st2', 'des2', value_max=3)
        
        s1 = self.s.get_stream_property('st1', 'value_max')
        self.assertEqual(s1, 2)
        
        s1 = self.s.set_stream_property('st1', 'value_max', 5)
        self.assertEqual(s1, True)
        
        s1 = self.s.get_stream_property('st1', 'value_max')
        self.assertEqual(s1, 5)
    
    def tearDown(self):
        pass
        

if __name__ == '__main__':
    unittest.main()
