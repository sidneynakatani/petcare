import requests, os, datetime
import hashlib
import pymongo
from pymongo import MongoClient

user     = os.getenv('MONGO_USER') 
password = os.getenv('MONGO_PASS')

class MessageController:


    def save(self, request):

         message = request.form['message']
         petId   = request.form['pet_id']
         timestamp = datetime.datetime.utcnow()
         
         hashId = hashlib.md5()      
         hashId.update(str(timestamp))
       

         connection = 'mongodb://{0}:{1}@ds059205.mlab.com:59205/ragdoll'.format(user, password)
         client = MongoClient(connection)
         db = client.ragdoll
         post = {"pet_id": petId, "message": message, "date": timestamp, "is_new":"true", "hashId" : hashId.hexdigest()}
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


    def getAll(self, pets):

          
          connection = 'mongodb://{0}:{1}@ds059205.mlab.com:59205/ragdoll'.format(user, password)
          client = MongoClient(connection)
          db = client.ragdoll
          posts = db.posts
          p = posts.find( { "pet_id": { "$in": pets } } )
          
          pets_list = []

          for pet in p:
               pets_list.append(pet)

          return pets_list


    def get(self, pets):

          
          connection = 'mongodb://{0}:{1}@ds059205.mlab.com:59205/ragdoll'.format(user, password)
          client = MongoClient(connection)
          db = client.ragdoll
          posts = db.posts
          p = posts.find( { "pet_id": { "$in": pets } , "is_new":"true"  } )
          
          pets_list = []

          for pet in p:
               pets_list.append(pet)

          return pets_list

    def markAsRead(self, request):
         petId  = request.form['pet_id']
         hashId = request.form['hash_id']

         timestamp = datetime.datetime.utcnow()
         timestamp = timestamp  + datetime.timedelta(days=5)

         
         connection = 'mongodb://{0}:{1}@ds059205.mlab.com:59205/ragdoll'.format(user, password)
         client = MongoClient(connection)
         db = client.ragdoll
         posts = db.posts
         db.posts.update(
              {"pet_id": petId, "hashId": hashId},
                  {
		   "$set": {
		    "is_new" : "false",
                    "date"   : timestamp
		    }
		  }
              )
         




