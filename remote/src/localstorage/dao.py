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
        self.db = self.connect(db, db_address)
        logger.log('done connecting to database')

    def connect(self, db, db_address):
        try:
            client = MongoClient(db_address)
            return client[str(db)]
        except pymongo.errors.ConnectionFailure:
            logger.log('Could not connect to sever ' + db_address)
            raise
        
        
    def insert(self, CollectionName, jsonstring):
        collection = self.db[str(CollectionName)]
        post_id = collection.insert(jsonstring)
        return post_id

    def update(self, CollectionName, SearchKey, SearchValue, FieldsJson):
        collection = self.db[str(CollectionName)]
        searchd = {SearchKey: SearchValue }
#         print searchd
#         print FieldsJson
#         print json.dumps(FieldsJson)
#         searchjson = ( searchd , { '$set': json.dumps(FieldsJson) } )
#         print searchjson
#         post_id = collection.update_one(searchd, '{ "$set": json.dumps(FieldsJson) }')
        post_id = collection.update_one(searchd, { "$set": FieldsJson})
        return post_id

    def update2(self, CollectionName, SearchDict, FieldsJson):
        collection = self.db[str(CollectionName)]
#         print searchd
#         print FieldsJson
#         print json.dumps(FieldsJson)
#         searchjson = ( searchd , { '$set': json.dumps(FieldsJson) } )
#         print searchjson
#         post_id = collection.update_one(searchd, '{ "$set": json.dumps(FieldsJson) }')
        post_id = collection.update_one(SearchDict, { "$set": FieldsJson})
        return post_id
    
    def getDateInRange(self, CollectionName, startDate, numberOfItems):
        '''
        Returns numberOfItems items from the database, if available data is less than numberOfItems, no data is returned. 
        '''
        searchd = {"date": {"$gt":str(startDate)}}
        return self.findDocument(CollectionName, searchd, numberOfItems)
        
    def findDocument(self, CollectionName, SearchString, SearchLimit=None):
        collection = self.db[str(CollectionName)]
        if SearchLimit is not None:
            collected = collection.find(SearchString).limit(SearchLimit)
        else:
            collected = collection.find(SearchString)
        collectedlist = []
        for data in collected:
            collectedlist.append(data)
        return collectedlist

    def findDocument2(self, CollectionName, SearchString, SearchLimit=None):
        collection = self.db[str(CollectionName)]
        if SearchLimit is not None:
            collected = collection.find(SearchString).limit(SearchLimit)
        else:
            collected = collection.find(SearchString)
        return collected

    
    def dropCollection(self, CollectionName):
        collection = self.db[str(CollectionName)]
        collection.drop()
        

sys.path.append('../')
from norsutils.logmsgs.logger import Logger
logger = Logger()
   
         
