import json
from json.decoder import JSONDecodeError
class ProcessLogger:
    def __init__(self,path:str):
        self._path = path
        # Read JSON From the Path
        try:
            with open(self._path,'r') as f:
                
                try:
                    self._data = json.load(f)
                except JSONDecodeError:
                    self._data = {"logs":[]}
            # Create a New Dictionary if it is not present
                if not self._data:
                    self._data = {"logs":[]}
        except FileNotFoundError:
            self._data = {"logs":[]}
    
    def writeToFile(self, newData:dict):
        self._data["logs"].append(newData)
        with open(self._path,'w') as f:
            json.dump(self._data,f)
