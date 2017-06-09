import requests, os, datetime
import pymongo
from pymongo import MongoClient

user     = os.getenv('MONGO_USER') 
password = os.getenv('MONGO_PASS')

class MessageController:


    def save(self, request):
         message = request.form['message']
         connection = 'mongodb://{0}:{1}@ds059205.mlab.com:59205/ragdoll'.format(user, password)
         client = MongoClient(connection)
         db = client.ragdoll
         post = {"message": message, "date": datetime.datetime.utcnow()}
         posts = db.posts
         post_id = posts.insert(post)
         print post_id


