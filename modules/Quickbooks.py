import json
from modules.utils import checkKeysInDictionary
from requests import post

class QuickbooksClient:

    def __init__(self,path:str,env:str):
        # Read JSON From the given Path
        self._env = env
        self._path = path
        with open(path,'r') as f:
            self._creds = json.load(f)
        # Check if the keys are present in the JSON
        credentialsKeys = ['client_id','client_secret',
        'realmId','accessToken','refreshToken', 'errorMessage','errorStatus','lastRunTime',
        'sandboxUri','productionUri', 'webhookToken']
        errorMessage = checkKeysInDictionary(credentialsKeys,self._creds)
        if errorMessage is not None:
            raise ValueError(f'{errorMessage} is not present in the JSON')
    

    def createBillInQuickBooks(self,billObject):

        baseUri = self._creds['productionUri']

        if self._env != 'production':
            baseUri = self._creds['sandboxUri']
        self.readCredentialsFromJSON()
        endpoint = f'{baseUri}/v3/company/{self._creds["realmId"]}/bill?minorversion=65'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self._creds["accessToken"]}',
        }
        response = post(endpoint, headers=headers, json=billObject)
        if(response.status_code != 200):
            raise ValueError(f"Unable to Push the Data to Quickbooks: {response.text}")

        print("Transaction for Bill Object: ", billObject)
        return response

    def readCredentialsFromJSON(self):
        with open(self._path,'r') as f:
            self._creds = json.load(f)
        