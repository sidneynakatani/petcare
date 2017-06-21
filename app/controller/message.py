import requests, os, datetime
import pymongo
from pymongo import MongoClient

user     = os.getenv('MONGO_USER') 
password = os.getenv('MONGO_PASS')

class MessageController:


    def save(self, request):
         message = request.form['message']
         petId   = request.form['pet_id']
         connection = 'mongodb://{0}:{1}@ds059205.mlab.com:59205/ragdoll'.format(user, password)
         client = MongoClient(connection)
         db = client.ragdoll
         post = {"pet_id": petId, "message": message, "date": datetime.datetime.utcnow(), "is_new":"true"}
         posts = db.posts
         post_id = posts.insert(post)
         print post_id


    def count(self, pets):
         
          connection = 'mongodb://{0}:{1}@ds059205.mlab.com:59205/ragdoll'.format(user, password)
          client = MongoClient(connection)
          db = client.ragdoll
          posts = db.posts
          p = posts.find( { "pet_id": { "$in": pets } , "is_new":"true"  } )
          return p.count()
