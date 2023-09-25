from bs4 import BeautifulSoup
import requests
import string
import re
import shelve
import json






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
        for element in translatedBoexes:
            translatedList = element.p.find_all(text=True)
            word_dicts[word] = translatedList
    return word_dicts




# def json_write(filename,dictToWrite):
#     with open(filename, 'w') as json_file:
#         json.dump(dictToWrite, json_file)




# char = 'a'
# site = 1
# word_dicts = get_sanook_dictionary(char,str(site))


# filename = char+"json"
# json_write(filename,word_dicts)


