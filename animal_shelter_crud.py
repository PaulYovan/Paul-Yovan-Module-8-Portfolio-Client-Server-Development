from pymongo import MongoClient
from bson.objectid import ObjectId
import pandas as pd
class AnimalShelter:
    def __init__(self, user, password):
        USER = user
        PASS = password
        HOST = 'nv-desktop-services.apporto.com' #variables
        PORT = 30460
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary  
            return True # Tells whether the create function ran successfully
        else:
            raise Exception("Nothing to save ...")

# Create method to implement the R in CRUD.     
    def read(self, data):
        if data:
            cursor = self.database.animals.find(data, {'_id':False})
        else:
            cursor = self.database.animals.find({}, {"_id": False})
        return cursor

# Update method to implement the U in CRUD.
    def update(self, data, new_values):
        updated_data = {"name":"Bingus","age_upon_outcome":"2 years"}
        if self.database.animals.count(data):
            self.database.animals.update(data, new_values)
            cursor = self.database.animals.find(updated_data)        
            json_data = dumps(cursor)
            return json_data
        else:
            raise Exception("Nothing to update ...") 
            
# Delete method to implement the D in CRUD
    def delete(self, data):
        result = self.database.animals.find_one_and_delete(data)
        # print the _id key only if the result is not None
        if("_id" in result):
            print("find_one_and_delete ID:",result["_id"])
        else:
            print("Nothing to delete")
            
    
      