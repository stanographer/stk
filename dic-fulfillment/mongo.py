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

