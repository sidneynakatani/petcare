import requests, os, calendar, time
import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import session



class ImageController:

     def upload(self, request):

	  name    = request.form['name']
          kind    = request.form['kind']
	  address = request.form['address']
	  quarter = request.form['quarter']
	  city    = request.form['city']
	  state   = request.form['state']
	  country = request.form['country']
	  zipcode = request.form['zipcode']
	  status  = request.form['status']
	  code    = session['logged_code'] 
	  photo   = request.files['photo']

          apiKey = os.getenv('API_KEY') 
          apiSecret = os.getenv('API_SECRET')
          cloudName = os.getenv('CLOUD_NAME')
   
          image_id = str(calendar.timegm(time.gmtime()))
          cloudinary.config(cloud_name = cloudName, api_key = apiKey, api_secret = apiSecret)
          print cloudinary.uploader.upload(photo, public_id = image_id)

	  host = '{0}/pet'.format(os.getenv('HOST'))

          if(os.getenv('HOST') == None):
               print  'Acesso local.'
               host = 'http://omegagls.herokuapp.com/pet'

          requests.post(host, data={ 'userId':code, 'imgId':image_id, 'name':name, 'kind':kind, 'status':status, 'address':address, 'quarter':quarter, 'city':city, 'state':state, 'country':country, 'zipCode':zipcode} )



