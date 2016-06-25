'''
Created on Jun 24, 2016

@author: mazzer
'''

from collections import namedtuple

class Stream():
    def __init__(self, sensor_id, timestamp):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.streams = {}
        
    def add(self,
            name,
            value):
        
        if name in self.streams:
            return False
        
        self.streams[name] = value
        
        
        