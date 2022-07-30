# Main Program for qbServer
# 1. Keep Refreshing the tokens coming from Quickbooks and store them in Secrets
# 2. On Demand Run the Code to push the files to Quickbooks

from modules.logger import ProcessLogger
from modules.Quickbooks import QuickbooksClient
from modules.readXML import XMLReader
import config as cfg
from os.path import abspath, dirname,exists
from os import chdir,replace,makedirs

def gotoCurrentDirectory():
    # Change the Directory to the Main Directory
    absPath = abspath(__file__)
    directoryName = dirname(absPath)
    chdir(directoryName)

def moveFileToFolder(fromPath:str,toPath:str):

    # Check if the file exists to toPath and if not create and then move the file from Path
    dirPath = toPath.split("/")[0]
    if not exists(dirPath):
        makedirs(dirPath)
    replace(fromPath,toPath)


def readXMLAndGetBills():
    xmlReader = XMLReader()
    xmlDictionaries = xmlReader.readXMLBillFromFiles(cfg.XML_FILE_PATH, cfg.XML_REPLACE_PATH)
    jsonBills = xmlReader.convertBillsToJSON(xmlDictionaries)
    return jsonBills

def uploadBillsToQuickBooks(bills:list[dict]):
    qbBillManager = QuickbooksClient(cfg.SECRETS_PATH, cfg.ENVIRONMENT)
    logger = ProcessLogger(cfg.LOGGER_PATH)
    for eachBill in bills:
        try:
            qbBillManager.createBillInQuickBooks(eachBill['billObject'])
            replace(eachBill['fromPath'], eachBill['toPath'])
        except ValueError as e:
            # Log Exception into JSON
            logger.writeToFile({
                "billObject": eachBill,
                "errorMessage": str(e)
            })
            moveFileToFolder(eachBill['fromPath'], eachBill['toPath'])

        



if __name__ == '__main__':
    gotoCurrentDirectory()
    bills = readXMLAndGetBills()
    uploadBillsToQuickBooks(bills)


