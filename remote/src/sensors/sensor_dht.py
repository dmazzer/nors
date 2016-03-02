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
from sensorservice.sensorservice import Nors_SensorService
from genericsensor.genericsensor import Nors_GenericSensor

from grovepi import *


if __name__ == '__main__':
    
    from norsutils.logmsgs.logger import Logger

    logger = Logger()
    logger.log("NORS - Noticia Remote Management and Supervisor")
    logger.log("SENSOR - DHT Humidity and Temperature")
    
