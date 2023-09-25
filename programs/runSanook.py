from bs4 import BeautifulSoup
import requests
import string
import re
import json
import os
import time


from myjson import MyJSON


def get_sanook_dictionary(char,site):
    word_dicts ={}
    url = f"https://dictionary.sanook.com/search/dict-all/char/{char}/{site}"
    print(url)
    response = requests.get(url,verify = False)
    soup = BeautifulSoup(response.content, "html.parser")
    classGropAll = soup.find('div', class_="group-all")
    liTag = classGropAll.find_all('li')
    #WORD
    for w in liTag:
        word = w.string
        # print(word)
        if word =="char": continue       # PAGE 19 of C problem with c word "char"  this doesn't link to the meaning but to root /char/
        link = w.a['href']
        link = re.sub('https', 'http', link)

        res = requests.get(link,verify = False)
        sou = BeautifulSoup(res.content, "html.parser")
        translatedBoexes = sou.find_all('section', class_="trans-box_s-pdt40")
        translatedList =[]
        for element in translatedBoexes:
            blogs = element.p.find_all(text=True)
            for meaning in blogs:
                translatedList.append(meaning)
            word_dicts[word] = translatedList
    return word_dicts

# sss= get_sanook_dictionary('z','1')
# print(len(sss["zebra"]))


def run_sanook(char,firstPage,max):
    while(firstPage < max+1):
        word_dicts ={}
        jsonObi = MyJSON(f"{char}{firstPage}_{firstPage}.json",word_dicts)
        jsonObi.json_write()

        for page in range(firstPage,firstPage+1):
            word_dicts = get_sanook_dictionary(char,page)
            jsonObi.add_dict_to_json(word_dicts)

        firstPage = firstPage+1

# get seperate small files
# run_sanook('r',1,44)

begin = time.time()
run_sanook('z',1,1)
print(time.time()-begin)


# ## gather all to a big file
# char = "x"
# fromSite = 1
# toSite = 1
# sumDicts={}
# for page in range(fromSite,toSite+1):
#     filenamePattern = os.path.join(os.getcwd(),'alldicts',char,f'{char}{page}_{page}.json')
#     openJsonDict = json.load(open(filenamePattern,encoding='utf-8'))
#     sumDicts.update(openJsonDict)

# print(len(sumDicts))
# jsonobj = MyJSON(f'{char}_dictionary.json',sumDicts)
# jsonobj.json_write()

# ####count check number
# for char in string.ascii_lowercase:
#     jsonCount = json.load(open(f'{char}_dictionary.json',encoding='utf-8'))
#     print(char,len(jsonCount))