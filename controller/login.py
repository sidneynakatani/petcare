import requests, os


class LoginController:

     def auth(self, request):

	email = request.form['email']
        password = request.form['password']
        host = '{0}/login'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/login'

        return requests.post(host, data={'email' : email, 'pass' : password} )

     
     def register(self, request):

        firstName = request.form['firstName']
	lastName = request.form['lastName']
	email = request.form['email']
	password = request.form['password']

	host = '{0}/register'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/register'

	return requests.post(host, data={'email' : email, 'password' : password, 'firstName' : firstName, 'lastName' : lastName} )

     def access(self, request):

        hashId = request.args.get('id')
        host = '{0}/register'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/register'

	return requests.post(host, data={ 'hashId' : hashId } )
	
