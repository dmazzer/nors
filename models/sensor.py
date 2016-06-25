'''
Created on Jun 24, 2016

@author: mazzer
'''

from collections import namedtuple
from enum import Enum
import json

SensorInterface = Enum('Interface', 
                 'analog digital virtual SPI i2c UART WiFi 6LoWPAN ZigBee LoRa other-wireless other-wired',
                 module=__name__) 

class Sensor():
    '''
    Sensor class
    Sensor model where properties are organized inside a named tuple
    '''
     
    def __init__(self, sensor_id, name, description, sensor_interface):
        
        
        Model = namedtuple('Sensor',
                            'sensor_id name description stream interface')
        
        self.sensor = Model(name = name,
                            sensor_id = sensor_id,
                            description = description, 
                            interface = sensor_interface,
                            stream = [])  
        
    def add_stream(self,
                    name, 
                    description,
                    type=None, 
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
                                   'type': type,
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
    

class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return {"__enum__": str(obj)}
        return json.JSONEncoder.default(self, obj)

def as_enum(d):
    if "__enum__" in d:
        name, member = d["__enum__"].split(".")
        return getattr(globals()[name], member)
    else:
        return d
                                 
                                   
                                   
                                   