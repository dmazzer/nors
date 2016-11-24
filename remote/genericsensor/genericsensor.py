""" 
genericsensor.py: Generic Sensor representation and registration application

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "GPL"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import datetime
import zmq
import sys
from threading import Thread
import Queue
import time
from uuid import uuid1
import json
import random

sys.path.append('../')
from norsutils.logmsgs.logger import Logger
logger = Logger('info')

sys.path.append('../../')
from models import sensor as SensorModel

class Nors_GenericSensorStorage(object):
    '''
    GenericSensorStorage class.
    
    This class is a simple implementation that may evolve to more elaborated 
    sensor data storage through overriding put and get methods.
    This cass may be used to store data in the context of the sensor class,
    before the data be stored locally in the database. 
    '''
    
    def __init__(self):
        self.sensor_data_storage = {}
    
    def put(self, sensor_data):
        self.sensor_data_storage = sensor_data
    
    def get(self):
        return self.sensor_data_storage

class Nors_GenericSensor(object):
    '''
    GenericSensor class, serve as a starting point to create a specific sensor reading class.
   
    A real sensor reading application must implements SensorRead and SensorDataProcessing
    '''
    
    def __init__(self, 
                 gs_name = 'Generic Sensor', 
                 gs_id = '', 
                 gs_description = 'generic sensor', 
                 gs_interface = SensorModel.SensorInterface.virtual,
                 gs_pull_interval = 5, 
                 gs_read_interval = 1):

        logger.log('GenericSensor started', 'debug')
        
        self.q = Queue.Queue()
        self.SensorDataStorage = Nors_GenericSensorStorage()
        
        if gs_id == '':
            sensor_id = str(uuid1())
        else:
            sensor_id = gs_id
            
        self.sensor_model = SensorModel.Sensor(sensor_id, 
                                              gs_name, 
                                              gs_description, 
                                              gs_interface, 
                                              gs_pull_interval, 
                                              gs_read_interval)
        
        logger.log(self.sensor_model.get_sensor_property('name') + ' UUID: ' + sensor_id)
        #logger.log(self.sensor_properties['name'] + ' UUID: ' + sensor_id)

        self.ipc_sensor_catalog = "ipc:///tmp/SensorCatalogService.pipe"
        self.ipc_sensor_pulling = "ipc:///tmp/" + sensor_id + ".pipe"
        
        self.SignIn()

    def SensorDataProcessing(self, sensor_data):
        logger.log(self.sensor_model.get_sensor_property('name') + ': Default sensor data processing', 'debug')
        return sensor_data
    
    def SensorRead(self):
        logger.log(self.sensor_model.get_sensor_property('name') + ': Default sensor data read', 'debug')
        return random.uniform(-1,1)
    
    def SignIn(self):
        '''
        SignIn - Register a sensor in SensorService
        '''
        
        logger.log('Registering sensor: ' + self.sensor_model.get_sensor_property('name'), 'debug')
        
        # ZeroMQ Context
        context = zmq.Context()
        
        # Define the socket using the "Context"
        socket = context.socket(zmq.REQ)
        socket.setsockopt(zmq.LINGER, 0)
        socket.connect(self.ipc_sensor_catalog)
        
        # Send a "message" using the socket
        socket.send_json(self.sensor_model.get_sensor_json())
        
        poller = zmq.Poller()
        poller.register(socket, zmq.POLLIN)

        if poller.poll(10*1000): # 10s timeout in milliseconds
            result = socket.recv_json()
        else:
            raise IOError(self.sensor_model.get_sensor_property('name') + ': Timeout processing auth request')

        if result['result'] == 'registered':
            logger.log(self.sensor_model.get_sensor_property('name') + ': Sensor Registered', 'debug')
            t = Thread(target=self.SensorWork, name='SensorWork', args=(self.q, ))
            t.daemon = True
            t.start()
        else:
            raise IOError(self.sensor_model.get_sensor_property('name') + ': Sensor NOT Registered')

        # starting thread to respond for sensor data pull requests
        tt = Thread(target=self.SensorPullWork, name='SensorPullWork', args=(self.q, ))
        tt.daemon = True
        tt.start()
                
    def SensorWork(self, q):
        '''
        SensorWork - Read a fisical sensor, call data processing and send data to storage
        '''
        
        while True:
            time.sleep(self.sensor_model.get_sensor_property('read_interval'))
            sensor_data = self.SensorRead()
            sensor_data_processed = self.SensorDataProcessing(sensor_data)
            self.SensorDataStorage.put(sensor_data_processed)
            
    def SensorPullWork(self, q):
        '''
        SensorPullWork - Transmits sensor data to SensorService when queryed (listener)
        '''
        
        # ZeroMQ Context
        context = zmq.Context()
        
        # Define the socket using the "Context"
        socket = context.socket(zmq.REP)
#         socket.setsockopt(zmq.LINGER, 0)
        socket.bind(self.ipc_sensor_pulling)
        
        while True:
            msg = socket.recv_json()
            if msg['query'] == 'sensor_data':
                sensor_data = {'sensor_data': self.SensorDataStorage.get()}
                socket.send_json(json.dumps(self.SensorDataInformation(sensor_data)))

    def SensorDataInformation(self, sensor_data):
        sensor_data['date'] = self.getDateTime()
        sensor_data['sensor_id'] = self.sensor_model.get_sensor_property('sensor_id')
        return sensor_data 

    def getDateTime(self):
        return str(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    