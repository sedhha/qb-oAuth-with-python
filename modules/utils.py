def checkKeysInDictionary(keys:list[str],dictionary:dict):
    for key in keys:
        if key not in dictionary:
            return key