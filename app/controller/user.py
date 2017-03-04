import requests, os


class UserController:

     def getUser(self, user_code):

        host = '{0}/user'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/user'

        return requests.post(host, data={'user_code' : user_code} )
