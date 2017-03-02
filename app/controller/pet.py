import requests, os


class PetController:

     def getPets(self, user_code):

        host = '{0}/pets'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/pets'

        return requests.post(host, data={'user_code' : user_code} )
