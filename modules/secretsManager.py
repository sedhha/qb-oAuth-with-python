import json
from requests import post
from modules.utils import checkKeysInDictionary
from base64 import b64encode

class QuickBooksSecretManager:

    def __init__(self,path:str):
        
        self._path = path
        # Read JSON From the Path
        with open(self._path,'r') as f:              
            self._creds = json.load(f)
        
        credentialsKeys = ['client_id','client_secret',
        'realmId','accessToken','refreshToken', 'errorMessage','errorStatus','lastRunTime',
        'webhookToken']

        # Check if the keys are present in the JSON
        errorMessage = checkKeysInDictionary(credentialsKeys,self._creds)
        if errorMessage is not None:
            raise ValueError(f'{errorMessage} is not present in the JSON')
        self.getNewAccessToken()

    def getNewAccessToken(self):

        baseUri = 'https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer'
        basicToken = f'{self._creds["client_id"]}:{self._creds["client_secret"]}'
        basicTokenBytes = basicToken.encode('ascii')
        basicTokenB64 = b64encode(basicTokenBytes)
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + basicTokenB64.decode('ascii')
        }

        formData = {
            'grant_type': 'refresh_token',
            'refresh_token': self._creds["refreshToken"]
        }

        response = post(baseUri, headers=headers, data=formData)
        if response.status_code != 200:
            error = response.json()
            raise ValueError(f'Error in getting the Access Token. Error Code: {error["error"]}')
        else:
            result = response.json()

            accessToken = result['access_token']
            refreshToken = result['refresh_token']

            self._creds['accessToken'] = accessToken
            self._creds['refreshToken'] = refreshToken

            self.writeToFile()

    def writeToFile(self):
        with open(self._path,'w') as f:
            json.dump(self._creds,f)

        




