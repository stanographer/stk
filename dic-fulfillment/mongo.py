import datetime
import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
class MongoDb:
    def __init__(self, endpoint):
        self.db = MongoClient(endpoint)['stk']
        self.MONGO_ENDPOINT = os.environ.get('MONGO_ENDPOINT')
        self.cluster = MongoClient(self.MONGO_ENDPOINT)
        self.db = self.cluster['stk']
        self.dictionaries = self.db['dictionaries']

    def set_dictionary(self, sub, dictionary, file_extension):
        dictionary_to_insert = {
           '_id': sub,
           'name': '',
           'created_on': datetime.datetime.utcnow(), 
           'last_modified': datetime.datetime.utcnow(),
           'version': 1,
           'previous_versions': [],
           'file_extension': file_extension,
           'contents': dictionary,
        }

        # set the dictionary id.
        dictionary_id = dictionary_to_insert._id
        # create a mongo record.
        dictionary = self.dictionaries.insert_one(dictionary_to_insert)

        return {
            'payload': dictionary_to_insert,
            'dictionary_id': dictionary_id
        }

    def get_dictionary(self, key):
        return self.dictionaries.find_one({ 'user': key })

