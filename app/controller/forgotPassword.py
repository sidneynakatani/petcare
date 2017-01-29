import requests, os, json


class ForgotPassController:

     
     def change(self, request):

        email = request.form['email']
        host = '{0}/forgotPass'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/forgotPass'

	return requests.post(host, data={ 'email' : email } )


     def update(self, request):

        password  = request.form['pass']
        hashId = request.form['hash']
        host = '{0}/forgotPass'.format(os.getenv('HOST'))
    
        if(os.getenv('HOST') == None):
             print  'Acesso local.'
	     host = 'http://omegagls.herokuapp.com/forgotPass'

	request = requests.put(host, data={ 'password' : password, 'hash' : hashId } )
        response = json.loads(request.text)
        updateStatus = response['updated']
        
        return updateStatus
	
