#!/usr/bin/env python2

""" 
sensor_bmp180.py: BMP180 Barometer Sensor

Sensror Info:
http://www.seeedstudio.com/wiki/Grove_-_Barometer_Sensor_(BMP180)
"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys
import signal

from genericsensor.genericsensor import Nors_GenericSensor

sys.path.append('../../GrovePi/Software/Python/grove_barometer_sensors/barometric_sensor_bmp180/')
sys.path.append('../GrovePi/Software/Python/grove_barometer_sensors/barometric_sensor_bmp180/')
import smbus
import RPi.GPIO as GPIO
from grove_i2c_barometic_sensor_BMP180 import BMP085

from norsutils.logmsgs.logger import Logger

logger = Logger('debug')
logger.log("SENSOR - BMP180 Barometer sensor", 'info')

class RealSensor(Nors_GenericSensor):
    def __init__(self):
        
        # Initialise the BMP085 and use STANDARD mode (default value)
        # bmp = BMP085(0x77, debug=True)
        # To specify a different operating mode, uncomment one of the following:
        # bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
        # bmp = BMP085(0x77, 1)  # STANDARD Mode
        # bmp = BMP085(0x77, 2)  # HIRES Mode
        # bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode
        self.bmp = BMP085(0x77, 1)
        
        rev = GPIO.RPI_REVISION
        if rev == 2 or rev == 3:
            self.bus = smbus.SMBus(1)
        else:
            self.bus = smbus.SMBus(0)
        
        self.sensor_name = 'BMP180'
        super(RealSensor, self).__init__(
                                         gs_name = self.sensor_name,
                                         gs_id = '51c8f22a-e191-11e5-914d-001dbaefa596',
                                         gs_description = 'BMP180 Barometer sensor', 
                                         gs_interface = None,
                                         gs_read_interval = 17)
        

    def SensorRead(self):
        try:
            temp = self.bmp.readTemperature()
            
            # Read the current barometric pressure level
            pressure = self.bmp.readPressure() / 100.0
            
            # To calculate altitude based on an estimated mean sea level pressure
            # (1013.25 hPa) call the function as follows, but this won't be very accurate
            # altitude = bmp.readAltitude()
            
            # To specify a more accurate altitude, enter the correct mean sea level
            # pressure level.  For example, if the current pressure level is 1023.50 hPa
            # enter 102350 since we include two decimal places in the integer value
            altitude = self.bmp.readAltitude(99191)
            logger.log( "Temp = " + str(temp) + "  Press = " + str(pressure) + " hPa" + "  Alt = " + str(altitude), 'debug')     
            return {'temp': temp, 'press': pressure, 'alt': altitude}
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

    
