import json
import string
class MyJSON():
    def __init__(self,filename,dictToWrite={}):
        self.filename = filename
        self.dictToWrite = dictToWrite
    
    def json_write(self):
        if self.dictToWrite != {}:
            with open(self.filename, 'w') as json_file:
                json.dump(self.dictToWrite, json_file)

    def add_dict_to_json(self,newDictToAdd):
        oldDicts = json.load(open(self.filename,encoding='utf-8'))
        oldDicts.update(newDictToAdd)
        with open(self.filename, 'w') as json_file:
            json.dump(oldDicts, json_file)
    
    def json_read(self,word):
        dictToSearch = json.load(open(self.filename,encoding='utf-8'))
        while True:
            try:
                resultList = dictToSearch[word.lower()]
                return word,resultList
            except KeyError:
                word = word[:-1]




