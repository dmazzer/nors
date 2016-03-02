#!/usr/bin/env python2

""" 
nors.py: Noticia Remote Management and Supervisor

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "GPL"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys
import signal

sys.path.append('../')
from genericsensor.genericsensor import Nors_GenericSensor

from grovepi import *

class RealSensor():
    def __init__(self):
        sensor = Nors_GenericSensor('DHT', '1e693dee-e0b6-11e5-8f44-001dbaefa596',
                                         'Special', 5, 4, self.SensorRead, self.SensorDataProcessing)
        sensor.SignIn()
        

    def SensorRead(self):
        dht_sensor_port = 2        # Connect the DHt sensor to port 7
    
        try:
            [ temp,hum ] = dht(dht_sensor_port,0)        #Get the temperature and Humidity from the DHT sensor
            t = str(temp)
            h = str(hum)
            logger.log( "Temp = " + t + "  Humidity = " + h + "%")     
            return {'temp': t, 'hum': h}
        except (IOError,TypeError) as e:
            logger.log("Error")

    def SensorDataProcessing(self,sensor_data):
        return sensor_data
        

from norsutils.logmsgs.logger import Logger

logger = Logger()
logger.log("NORS - Noticia Remote Management and Supervisor")
logger.log("SENSOR - DHT Humidity and Temperature")

if __name__ == '__main__':
    print RealSensor.SensorRead()


def do_exit(sig, stack):
    raise SystemExit('Exiting')

signal.signal(signal.SIGINT, do_exit)
signal.signal(signal.SIGUSR1, do_exit)

signal.pause()    

    