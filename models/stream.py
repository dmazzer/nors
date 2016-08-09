""" 
stream.py: Stream model class

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import datetime
from recordtype import recordtype
import json

from .utils import EnumEncoder

class Stream():
    '''
    Stream class
    Stream model where sensor data are organized inside a named tuple
    '''
     
    def __init__(self, sensor_id, stream_names):
        '''
        sensor_id: the ID of the sensor that generates the stream
        stream_names: list of the stream names that the sensor generates 
        '''
        
        Model = recordtype('Stream',
                            'sensor_id timestamp streams')
        
        streams = dict((stream_names[i], 0) for i in range(0, len(stream_names) ))
        
        self.stream = Model(sensor_id = sensor_id,
                            timestamp = 0,
                            streams = streams)  
        
    def get_stream(self):
        return self.stream._asdict()
    
    def set_values(self, name_value_dict):
        for i in range(len(name_value_dict)):
            self.stream.streams[name_value_dict.keys()[i]] = name_value_dict[name_value_dict.keys()[i]] 
        self.stream.timestamp = self.getDateTime()
        
    def get_stream_json(self, indentation=None):
        return json.dumps(self.get_stream(), encoding='UTF-8', cls=EnumEncoder, indent=indentation)
    
    def getDateTime(self):
        return str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    
    def get_property(self, property):
        return self.get_stream()[property]
        
#     def get_stream_property(self, stream_name, property):
#         for item in self.get_stream()['stream']:
#             if item['name'] is stream_name:
#                 return item[property]
#         return None
#     
#     def set_stream_property(self, stream_name, property, value):
#         for item in self.get_stream()['stream']:
#             if item['name'] is stream_name:
#                 item['property'] = value
#                 return True
#         return False
#     
