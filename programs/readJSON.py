
from myjson import MyJSON
import json
import os
import string


words = string.ascii_letters
resultsList=[]

for word in words:

    fileLocation = os.path.join(os.getcwd(),'alldicts_added',f'{word[0]}_dictionary.json')
    
    dictOBJ = MyJSON(fileLocation)
    resultTuple = dictOBJ.json_read(word)
    resultsList.append(resultTuple)
    
for key,meaningList in resultsList:
    print(key)
    for meaning in meaningList:
        print(meaning)
    print('---------------------------')
