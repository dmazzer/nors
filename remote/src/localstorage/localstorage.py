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

from norsutils.logmsgs.logger import Logger
from localstorage.dao import Nors_LocalStorage_DAO

logger = Logger()


class Nors_LocalStorage():
    def __init__(self):

        self.local_db_collection_name = 'nors_local_storage'
        
        # TODO: self.max_db_entries is the max number of entries in DB, if exceeds 
        # new data is droped. The values 0 disable the entries limitation.
        self.max_db_entries = 10000

        # TODO: self.db_entries_ttl may be used to define the time to live
        # of each new entry, leaving to MongoDB automatically delete
        # documents after the time in seconds specified. This feature is
        # not yet implemented on DAO.    
        self.db_entries_ttl = 1 * (60 * 24)
        
        self.local_dao = Nors_LocalStorage_DAO(db=self.local_db_collection_name)

    def store(self, data_to_insert):
        self.local_dao.insert(self.local_db_collection_name, data_to_insert) 
    
    def __transfer_to_external_db(self):
        pass
    
    def __prepare_data_to_transfer(self):
        pass
    
    def __remove(self):
        pass
        
    
        
    