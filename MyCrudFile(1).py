from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    ##CRUD Operations
    
    def __init__(self,username,password):
        #Connection Variables
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30099
        DB = 'AAC'
        COL = 'animals'
        
        #Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
     
    #Create Method
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            if insert != 0:
                return True
          
        else:
            return False
            
    #read method
    def read(self, data):
                result = self.database.animals.find(data, {'_id':False})
                return result
        
     #update method
    def update(self, data, newData):
        if data is not None:
            
            count = self.database.animals.update_many(data, newData)
            return count
        else:
            raise Exception("Nothing to update since data parameter is empty")
    
    #delete method
    def delete(self, data):
        if data is not None:
            count = self.database.animals.delete_many(data)
            return count
        else:
            raise Exception("Nothing to delete since data parameter is empty")
            
       
            