import requests, os


class ForgotPassController:

     
     def change(self, request):

        email = request.form['email']
        host = '{0}/forgotPass'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/forgotPass'

	return requests.post(host, data={ 'email' : email } )
	
