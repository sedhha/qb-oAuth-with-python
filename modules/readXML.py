import  xmltodict
from os import listdir


class XMLReader:

    def convertXMLToAPIJSONStructure(self,xmlBill:dict):
        line = []
        billLines = xmlBill["BillLine"]
        xmlBill["Amount"] = float(xmlBill["Amount"]) / 10
        if xmlBill["Amount"] < 0:
            xmlBill["Amount"] = xmlBill["Amount"] * -1

        if type(billLines) is not list:
            billLines = [billLines]
        for eachBillLine in billLines:

            eachBillLine["Amount"]= float(eachBillLine["Amount"]) / 10

            if eachBillLine["Amount"] < 0:
                eachBillLine["Amount"] = eachBillLine["Amount"] * -1

            billLine = {
                "DetailType": eachBillLine["Desc"],
                "Amount": eachBillLine["Amount"],
                eachBillLine["Desc"]: {
                    "AccountRef": {
                        "value": f'{eachBillLine["AccountRef"]}'
                        }
                }
            }
            line.append(billLine)
        
        return {
            "Line": line,
            "VendorRef": {
                "value": xmlBill["SupplierAccount"],
                "name": xmlBill["Supplier"]
            },
            "LinkedTxn": [
                {
            "TxnId":xmlBill["Number"], 
            }
            ],
            "TotalAmt": xmlBill["Amount"], 
            "TxnDate": xmlBill["TransactionDate"],
            "DueDate": xmlBill["DueDate"]

        }

    def readXMLBillFromFiles(self,path:str,movePath:str):
        files = listdir(path)
        xmlDictionaries = []
        for eachFile in files:
            with open(f'{path}/{eachFile}') as xml_file:
                data_dict = xmltodict.parse(xml_file.read())
                if type(data_dict['GLXML']['Bill']) is not list:

                    result = [
                        {
                            'dict':data_dict['GLXML']['Bill'],
                            'fromPath': f'{path}/{eachFile}',
                            'toPath': f'{movePath}/{eachFile}'
                        }
                        ]
                else:
                    result = list(map(data_dict['GLXML']['Bill'],lambda x: {
                    'dict':x,
                    'fromPath': f'{path}/{eachFile}',
                    'toPath': f'{movePath}/{eachFile}'
                    }))
                
                xmlDictionaries.extend(result)
                


        return xmlDictionaries

    def convertBillsToJSON(self,bills:list[dict]):
        jsonBills = []
        for everyBill in bills:
            convertedRequestBody = self.convertXMLToAPIJSONStructure(everyBill['dict'])
            jsonBills.append({
                'billObject': convertedRequestBody,
                'fromPath': everyBill['fromPath'],
                'toPath': everyBill['toPath']
            })
        return jsonBills
        
    
    
