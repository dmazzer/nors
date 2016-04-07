""" 
dao.py: MongoDB DAO

"""
import pymongo

__author__ = "Daniel Mazzer"
__copyright__ = "Copyright 2016, NORS project"
__credits__ = ""
__license__ = "MIT"
__maintainer__ = "Daniel Mazzer"
__email__ = "dmazzer@gmail.com"

from pymongo import MongoClient

import sys
import json

class Nors_LocalStorage_DAO:
    def __init__(self, db='nors_localstorage', db_address='mongodb://localhost:27017/'):
        
        logger.log('connecting to LOCAL database ' + db + ' at ' + db_address)
        try:
            self.db_connection = MongoClient(db_address)
            self.db_client =  self.db_connection[str(db)]
            self.db_name = db
        except pymongo.errors.ConnectionFailure:
            logger.log('Could not connect to sever ' + db_address)
            raise

        logger.log('done connecting to database')

    def insert(self, CollectionName, jsonstring):
        collection = self.db_client[str(CollectionName)]
        post_id = collection.insert(jsonstring)
        return post_id

    def update(self, CollectionName, SearchDict, FieldsJson):
        collection = self.db_client[str(CollectionName)]
        post_id = collection.update_one(SearchDict, { "$set": FieldsJson})
        return post_id
    
    def get_itens_from_date(self, CollectionName, startDate, numberOfItems):
        '''
        Returns numberOfItems items from the database, if available data is less than numberOfItems, no data is returned. 
        '''
        searchd = {"date": {"$gt":str(startDate)}}
        return self.find(CollectionName, searchd, numberOfItems)
        
    def find(self, CollectionName, SearchString, SearchLimit=None):
        collection = self.db_client[str(CollectionName)]
        if SearchLimit is not None:
            collected = collection.find(SearchString).limit(SearchLimit)
        else:
            collected = collection.find(SearchString)
        return collected

    
    def dropCollection(self, CollectionName):
        collection = self.db_client[str(CollectionName)]
        collection.drop()
        
    def dropDB(self):
        database = self.db_connection.drop_database(self.db_name)
        

sys.path.append('../')
from norsutils.logmsgs.logger import Logger
logger = Logger()
   
         
