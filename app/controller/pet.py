import requests, os


class PetController:

     def getPets(self, user_code):

        host = '{0}/pets'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/pets'

        return requests.post(host, data={'user_code' : user_code} )


     def updatePets(self, request):

        host = '{0}/pet'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/pet'

	petId  = request.form['petId']
        name   = request.form['name']
        kind   = request.form['kind']
        status = request.form['status']

        return requests.put(host, data={'petId' : petId, 'name' : name, 'kind': kind, 'status': status} )
