# import datetime
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('')

# class MongoDb:
#     def __init__(self, endpoint):
#         self.db = MongoClient(endpoint)['stk']
#         self.dictionaries = self.db.dictionaries

#     def set_dictionary(self, data):
#         dictionary_to_insert = {
#            'user': data.user,
#            'created_on': datetime.datetime.utcnow(), 
#            'last_modified': datetime.datetime.utcnow(),
#            'version': 1,
#            'previous_versions': [],
#            'file_type': data.file_type,
#            'data': data.dictionary
#         }

#         dictionary_id = self.dictionaries.insert_one(dictionary_to_insert).inserted_id

#         return {
#             'payload': dictionary_to_insert,
#             'dictionary_id': dictionary_id
#         }

#     def get_dictionary(self, key):
#         return self.dictionaries.find_one({ 'user': key })

#     def create_new_user(self, data):

class MongoDb:
    def __init__(self, endpoint):
        self.client = MongoClient(endpoint)
        self.db = self.client.stktin
        self.dictionaries = self.db.dictionaries
        self.id = ''

    def set_dictionary(self, sub, dictionary, file_extension):
        dictionary_to_insert = {
           '_id': sub,
           'name': '',
           'created_on': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S%z'), 
           'last_modified': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S%z'),
           'version': 1,
           'previous_versions': [],
           'file_extension': file_extension,
           'contents': dictionary,
        }

        print('clienttttt', self.client)
        print('db', self.db)
        print('TICTTTTTISDtsdsietioder', dictionary_to_insert)
        print('self.dictionariessssss', self.dictionaries)
        print('DIC to INSERTTTT',json.dumps(dictionary_to_insert))

        # set the dictionary id.
        dictionary_id = dictionary_to_insert['_id']

        print('dictionary id--------------------', dictionary_id)

        # create a mongo record.
        dic = self.dictionaries.insert_one(dictionary_to_insert).inserted_id
        
        return jsonify(
            status=True,
            message='Saved successfully!'
        ), 201

    def get_dictionary(self, key):
        return self.dictionaries.find_one({ 'user': key })
