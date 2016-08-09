#!/usr/bin/env python2

""" 
sensor_dht.py: DHT11 Temperature and Humidity sensor driver

Sensror Info:
http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor
"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys
import signal

# sys.path.append('./genericsensor/')
# sys.path.append('./norsutils/')
# sys.path.append('../../')

from genericsensor.genericsensor import Nors_GenericSensor

from grovepi import *

from norsutils.logmsgs.logger import Logger

logger = Logger('debug')
logger.log("SENSOR - DHT Humidity and Temperature", 'info')

class RealSensor(Nors_GenericSensor):
    def __init__(self):
        
        self.sensor_name = 'DHT'
        
        super(RealSensor, self).__init__(
                                         gs_name = self.sensor_name,
                                         gs_id = '1e693dee-e0b6-11e5-8f44-001dbaefa596',
                                         gs_description = 'DHT Humidity and Temperature', 
                                         gs_interface = None,
                                         gs_pull_interval = 5, 
                                         gs_read_interval = 4)

    def SensorRead(self):
        dht_sensor_port = 2        # GrovePI port
    
        try:
            [ temp,hum ] = dht(dht_sensor_port,0)        #Get the temperature and Humidity from the DHT sensor
            t = str(temp)
            h = str(hum)
            logger.log( "Temp = " + t + "  Humidity = " + h + "%", 'debug')     
            return {'temp': t, 'hum': h}
        except (IOError,TypeError) as e:
            logger.log("Error reading sensor " + self.sensor_name, 'error')

    def SensorDataProcessing(self,sensor_data):
        return sensor_data
        

if __name__ == '__main__':
    sensor = RealSensor()

    def do_exit(sig, stack):
        raise SystemExit('Exiting')
    
    signal.signal(signal.SIGINT, do_exit)
    signal.signal(signal.SIGUSR1, do_exit)
    
    signal.pause()    

    
