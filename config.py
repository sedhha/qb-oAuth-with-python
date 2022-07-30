LOGGER_PATH = r'logs/process-logs.json'
SECRETS_PATH = r'secrets/secrets.json'
XML_FILE_PATH = r'files'
XML_REPLACE_PATH = r'inserted-files'
ENVIRONMENT='sandbox'

sampleBillObject = {
  "Line": [
    {
      "DetailType": "AccountBasedExpenseLineDetail", 
      "Amount": 200.0, 
      "Id": "1", 
      "AccountBasedExpenseLineDetail": {
        "AccountRef": {
          "value": "7"
        }
      }
    }
  ], 
  "VendorRef": {
    "value": "56"
  }
}