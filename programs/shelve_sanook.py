import shelve
import os
import platform




def find_inshelve(word):
    beginChar = word[0]
    if platform.system() == 'Windows':filename = os.path.join(os.getcwd(),'app','data','sanookDAT',beginChar+'_sanook')
    else:filename = os.path.join(os.getcwd(),'app','data','sanookDB',beginChar+'sanook')

    shelveOBJ = shelve.open(filename)
    notFoundList =[]
    found = False
    while(not found):
        try:
            shelveOBJ[word]
            found =True
        except KeyError:
            result = " : [0] not found"
            notFoundList.append(word+" "+result)
            word = word[0:-1]

    return word,shelveOBJ[word],notFoundList



words =['cat','i','me','now','rihanna','callin','loved']


resultList=[]
for word in words: 
    resultList.append(find_inshelve(word))

for element in resultList:
    print(element)