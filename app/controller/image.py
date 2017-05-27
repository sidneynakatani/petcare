import requests, os, calendar, time, json
import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import session

import urllib

apiKey    = os.getenv('API_KEY') 
apiSecret = os.getenv('API_SECRET')
cloudName = os.getenv('CLOUD_NAME')

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

       
   
	  pet_tags = '^N_{0},^E_{1},^A_{2},^C_{3},^P_{4},^S_{5}'.format(name, kind, address, city, country, status)
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

	  cloudinary.config(cloud_name = cloudName, api_key = apiKey, api_secret = apiSecret)
	  data = cloudinary.api.resources(max_results=50, tags='True')
	  data = json.dumps(data, indent=3, sort_keys=True)
          return json.loads(data)

     def updateImageStatus(self, request):
          print "teste"
	  name    = request.form['name']
          kind    = request.form['kind']
          status  = request.form['status']
          image   = request.form['image_id']

          current_name   = request.form['current_name']
          current_kind   = request.form['current_kind']
          current_city   = request.form['current_city']
          current_status = request.form['current_status']
          current_street   = request.form['current_street']
          current_country  = request.form['current_country']

	  currentStatus = '{0}/{1}/{2}/{3}/{4}'.format(current_name.strip(), current_kind.strip(), current_city.strip(), current_status.strip(), image)
          newStatus     = '{0}/{1}/{2}/{3}/{4}'.format(name.strip(), kind.strip(), current_city.strip(), status, image)
          pet_tags      = "'^N_{0},^E_{1},^A_{2},^C_{3},^P_{4},^S_{5}'".format(name.strip(), kind.strip(), current_street.strip(), current_city.strip(), current_country.strip(), status.strip())
          
	  cloudinary.config(cloud_name = cloudName, api_key = apiKey, api_secret = apiSecret)
          cloudinary.api.update(urllib.quote(currentStatus), tags = pet_tags)
          cloudinary.uploader.rename(currentStatus, newStatus)
          


     def getImageByTag(self, request):
           
	  city =  '^C_' + request.form['city'] 
	  tags =  urllib.quote(city.strip())
         
	  cloudinary.config(cloud_name = cloudName, api_key = apiKey, api_secret = apiSecret)
          data = cloudinary.api.resources_by_tag(tags, tags='True')
          data = json.dumps(data, indent=3, sort_keys=True)
          return json.loads(data)  
		  
		  



	
