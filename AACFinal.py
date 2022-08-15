from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:47666' % (username, password))
        self.database = self.client['AAC']


    # Complete this create method to implement the C in CRUD.
    def create(self, animal_data):
        if animal_data is not None:
            print("----------------------- Inserting New Animal ------------------")
            self.database.animals.insert(animal_data)  # data should be dictionary
            print("-------------- Done -------------------------------------------")
        else:
            raise Exception("Failed to add Data")
            
            
    def read(self, criteria):
        if criteria is not None:
            data = self.database.animals.find(criteria)  # data should be dictionary 
            for document in data:
                print(">>")
                print(document)
                print()
        else:
            raise Exception("nothing to read, hint is empty") 
            
        
    # Method to implement the U in CRUD
    def update(self, criteria,new_data):
        if criteria is not None and new_data is not None:
            self.database.animals.update_many(criteria,{'$set':new_data}) 
            self.read(new_data)
            
    # Method to implement the D in CRUD
    def delete(self, data):
        #Verify that the record to be deleted has been supplied
        if data is not None:
            # delete the documents matching data criteria and print no. of documents deleted in json format
            delete_result = self.database.animals.delete_many(data)
            result = "Documents deleted: "+ json.dumps(delete_result.deleted_count)
            #print("Documents deleted ", json.dumps(delete_result.deleted_count))
            return result
        else:
            raise Exception("No record found")