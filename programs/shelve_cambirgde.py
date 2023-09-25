import shelve
import os
from cambirdge_translate import fcambrigde_translate


import re
from cambirdege_th import fcambridge_th
from cambirdge_eng import fcambridge_eng
import string




def write_shelvedb(word,thaiMeaningList):  #write json file for each song 
    shelfFile = shelve.open(os.path.join(os.getcwd(),"app",'data','shelveDB','myDictsDB'))
    shelfFile[word] = thaiMeaningList
    shelfFile.close()

def check_shelveDB(word):
    foundDicts={}
    notFoundWord=''
    shelfFile = shelve.open(os.path.join(os.getcwd(),"app",'data','shelveDB','myDictsDB'))
    try:
        foundDicts[word] = [shelfFile[word]]
        shelfFile.close()
        return True,foundDicts
    except KeyError:
        notFoundWord = word
        shelfFile.close()
        return False,notFoundWord

def fcambrigde_translate(word):                    
    # wordType = re.compile(r'\s+(verb|adverb|noun|adjective)?.+').group()
    engWord,thaiMeaningList =fcambridge_th(word)
    #if engWord can be found
    if engWord != None and thaiMeaningList != []:
        # engWord = re.sub(wordType,'',engWord)
        return engWord,thaiMeaningList  

    #if engWord can't be found
    else:
        #first try check ing in form in
        if word[-2:] =="in":
            ingWord = word+'g'
            result , value = check_shelveDB(ingWord)
            if result:
                engWord = word
                thaiMeaningList =value[ingWord][0]
                # engWord = re.sub(wordType,'',engWord)
                return engWord ,thaiMeaningList

            else:    
                engWord,thaiMeaningList =fcambridge_th(ingWord)
                if engWord =="" or thaiMeaningList=="":
                    engWord,thaiMeaningList = fcambridge_eng(ingWord)
                    # engWord = re.sub(wordType,'',engWord)
                return engWord,thaiMeaningList

        # english cambirgde
        engWord, thaiMeaningList =fcambridge_eng(word)
        if not thaiMeaningList:
            engWord = word
            thaiMeaningList = ["NOT FOUND"]
        return engWord,thaiMeaningList



dictCollect ={}
notFoundList =[]
wordList = ["be","hand"]

for word in wordList:
    result,value = check_shelveDB(word)
    if result:
        dictCollect[word] = value[word][0]
    else:
        notFoundList.append(word)


print(notFoundList)
print(dictCollect.keys())

for word in notFoundList:
    eng,thaiMeaningList = fcambrigde_translate(word)
    result,value = check_shelveDB(eng)
    if result:
        write_shelvedb(word,value[eng][0])
        dictCollect[word] = (value[eng][0])
    else:    
        write_shelvedb(eng,thaiMeaningList)
        dictCollect[eng]=thaiMeaningList


shelfFile = shelve.open(os.path.join(os.getcwd(),'app','data','shelveDB','myDictsDB'))
for one in shelfFile:
    print(one)
    for element in shelfFile[one]:
        print(element)
    print("-----------------------------------------------------------------")

# print(len(dictCollect))
# print(dictCollect)