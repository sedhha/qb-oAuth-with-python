from modules.secretsManager import QuickBooksSecretManager
import config as cfg
from os.path import abspath, dirname
from os import chdir

def gotoCurrentDirectory():
    # Change the Directory to the Main Directory
    absPath = abspath(__file__)
    directoryName = dirname(absPath)
    chdir(directoryName)

def refreshTokens():
    QuickBooksSecretManager(cfg.SECRETS_PATH)

if __name__ == "__main__":
    gotoCurrentDirectory()
    refreshTokens()
