import requests, os, calendar, time, json
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
   
	  pet_tags = '{0},{1},{2},{3},{4},{5}'.format(name, kind, address, city, country, status)
          folder = '/{0}/{1}/{2}/{3}'.format(name, kind, city, status)

          image_id = str(calendar.timegm(time.gmtime()))
          cloudinary.config(cloud_name = cloudName, api_key = apiKey, api_secret = apiSecret)
          cloudinary.uploader.upload(photo, folder= folder, public_id = image_id, tags = pet_tags)

	  host = '{0}/pet'.format(os.getenv('HOST'))

          if(os.getenv('HOST') == None):
               print  'Acesso local.'
               host = 'http://omegagls.herokuapp.com/pet'

          requests.post(host, data={ 'userId':code, 'imgId':image_id, 'name':name, 'kind':kind, 'status':status, 'address':address, 'quarter':quarter, 'city':city, 'state':state, 'country':country, 'zipCode':zipcode} )



     def getImages(self, request):

          apiKey = os.getenv('API_KEY') 
          apiSecret = os.getenv('API_SECRET')
          cloudName = os.getenv('CLOUD_NAME')

	  cloudinary.config(cloud_name = cloudName, api_key = apiKey, api_secret = apiSecret)
	  data = cloudinary.api.resources(max_results=50)
	  data = json.dumps(data, indent=3, sort_keys=True)
          return json.loads(data)

     def updateImageStatus(self, request):

	  name    = request.form['name']
          kind    = request.form['kind']
          city    = request.form['city']
          status  = request.form['status']
          image   = request.form['image_id']
          current_status = request.form['current_status']

	  currentStatus = '{0}/{1}/{2}/{3}/{4}'.format(name.strip(), kind.strip(), city.strip(), current_status.strip(), image)
          newStatus     = '{0}/{1}/{2}/{3}/{4}'.format(name.strip(), kind.strip(), city.strip(), status, image)
          
          apiKey = os.getenv('API_KEY') 
          apiSecret = os.getenv('API_SECRET')
          cloudName = os.getenv('CLOUD_NAME')

	  cloudinary.config(cloud_name = cloudName, api_key = apiKey, api_secret = apiSecret)
          cloudinary.uploader.rename(currentStatus, newStatus)



	
