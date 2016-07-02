""" 
sensor.py: Sensor model class

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

from collections import namedtuple
from enum import Enum
import json

from .utils import EnumEncoder

SensorInterface = Enum('Interface', 
                 'analog digital virtual SPI i2c UART WiFi 6LoWPAN ZigBee LoRa other-wireless other-wired',
                 module=__name__) 

class Sensor():
    '''
    Sensor class
    Sensor model where properties are organized inside a named tuple
    '''
     
    def __init__(self, sensor_id, name, description, sensor_interface, pull_interval, read_interval):
        
        
        Model = namedtuple('Sensor',
                            'name sensor_id description interface pull_interval  read_interval stream')
        
        self.sensor = Model(name = name,
                            sensor_id = sensor_id,
                            description = description, 
                            interface = sensor_interface,
                            pull_interval = pull_interval,
                            read_interval = read_interval,
                            stream = [])  
        
    def add_stream(self,
                    name, 
                    description,
                    sensor_type=None, 
                    unit=None,
                    sensing_rate=None,
                    value_nominal=None,
                    value_normal_max=None,
                    value_normal_min=None,
                    value_max=None,
                    value_min=None,
                    resolution=None,
                    lower_threshold_non_critical=None,
                    upper_threshold_non_critical=None,
                    lower_threshold_critical=None,
                    upper_threshold_critical=None,
                    lower_threshold_fatal=None,
                    upper_threshold_fatal=None,
                    enabled_thresholds=None):
        
        self.sensor.stream.append({'name': name,
                                   'description': description,
                                   'sensor_type': sensor_type,
                                   'unit': unit,
                                   'sensing_rate': sensing_rate,
                                   'value_nominal': value_nominal,
                                   'value_nominal': value_nominal,
                                   'value_normal_max': value_normal_max,
                                   'value_normal_min': value_normal_min,
                                   'value_max': value_max,
                                   'value_min': value_min,
                                   'resolution': resolution,
                                   'lower_threshold_non_critical': lower_threshold_non_critical,
                                   'upper_threshold_non_critical': upper_threshold_non_critical,
                                   'lower_threshold_critical': lower_threshold_critical,
                                   'upper_threshold_critical': upper_threshold_critical,
                                   'lower_threshold_fatal': lower_threshold_fatal,
                                   'upper_threshold_fatal': upper_threshold_fatal,
                                   'enabled_thresholds': enabled_thresholds})
        

    def get_stream_num(self):
        return len(self.sensor.stream)
        
    def get_sensor(self):
        return self.sensor._asdict()
    
    def get_sensor_json(self, indentation=None):
        return json.dumps(self.get_sensor(), encoding='UTF-8', cls=EnumEncoder, indent=indentation)
    
    def get_property(self, property):
        return self.get_sensor()[property]
        
    def get_stream_property(self, stream_name, property):
        for item in self.get_sensor()['stream']:
            if item['name'] is stream_name:
                return item[property]
        return None
    
    def set_stream_property(self, stream_name, property, value):
        for item in self.get_sensor()['stream']:
            if item['name'] is stream_name:
                item['property'] = value
                return True
        return False
