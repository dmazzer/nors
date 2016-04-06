#!/usr/bin/env python2

""" 
localstorage.py: LocalStorage - Local database storage and database management

"""

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

import sys
import signal

# sys.path.append('../')
# from genericsensor.genericsensor import Nors_GenericSensor

class Nors_LocalStorage():
    def __init__(self):
        '''
        UserDAO Constructor
        Receives the db_client (unique for all Cell Controllers), collection (one for each Cell Controller) and db_address
        '''
        
        self.logger = Logger()

        self.logger.log('connecting to database ' + db + ' at ' + db_address)

        client = MongoClient(db_address)
        self.db_client = client[str(db)]
        
        self.logger.log('done connecting to database')

    def insert(self, CollectionName, jsonstring):
        collection = self.db_client[str(CollectionName)]
        post_id = collection.insert_one(jsonstring).inserted_id
        return post_id
    
    def insert(self):
        pass 
    
    def remove(self):
        pass
    
    def count(self):
        pass
    
    
        
    