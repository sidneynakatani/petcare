import requests, os
import cloudinary
import cloudinary.uploader
import cloudinary.api



class ImageController:

     def upload(self, request):
          

          apiKey = os.getenv('API_KEY') 
          apiSecret = os.getenv('API_SECRET')
          cloudName = os.getenv('CLOUD_NAME')
   
          photo = request.files['photo']
          cloudinary.config(cloud_name = cloudName, api_key = apiKey, api_secret = apiSecret)
          print cloudinary.uploader.upload(photo, public_id = 'sample_id')


