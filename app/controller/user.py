import requests, os
from flask import session


class UserController:

     def getUser(self, user_code):

        host = '{0}/user'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/user'

        return requests.post(host, data={'user_code' : user_code} )



     def updateUser(self, request):

          host = '{0}/user'.format(os.getenv('HOST'))
    
          if(os.getenv('HOST') == None):
               print  'Acesso local.'
	       host = 'http://omegagls.herokuapp.com/user'
	  

          user_code  = session['logged_code']
	  first_name = self.validateFormValue(request,'first_name')
	  last_name  = self.validateFormValue(request,'last_name')
          email      = self.validateFormValue(request,'email')
          password   = self.validateFormValue(request,'password')
          
	  return requests.put(host, data={'email' : email, 'password' : password, 'first_name' : first_name, 'last_name' : last_name, 'user_code':user_code} )



     def validateFormValue(self,request, formValue):

          validateValue = ''
          
	  try:
	       validateValue = request.form[formValue]

	  except:
               validateValue = ''
        
          return validateValue





