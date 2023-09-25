from bs4 import BeautifulSoup
import requests
import urllib
import re

def cambridge_th(word):                                             #using in collection_dict
    meaning_list = []
    eng_string=""
    eng_string_list=[]
    url = "https://dictionary.cambridge.org/dictionary/english-thai/"+word
    sauce = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sauce,"html.parser")
    
    boxes_thai_found = soup.find_all('div','def-body ddef_b ddef_b-t')
    if word:
        for box in boxes_thai_found:
            meaning_list.append(box.text)

    boxes_eng_found = soup.find_all('div','dpos-h di-head normal-entry')
    if word:
        for box in boxes_eng_found:
            eng_string =box.text.strip()
            eng_string_list = eng_string.split(" ")
            break

    return eng_string_list[0],meaning_list   #string,list

def cambridge_noth(word):
    meaning_list = []
    eng_string=''
    reg=''
    url="https://dictionary.cambridge.org/dictionary/english/"+word
    sauce = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sauce,"html.parser")
    boxes_found = soup.find_all('div','def-block ddef_block')
    if word:
        for box in boxes_found:
            if "src" in box.text.strip():
                continue
            meaning_list.append(box.text.strip())
            if '\n' in box.text:
                reg = re.sub('\n','',box.text)
            meaning_list.append(reg)

    boxes_eng_found =soup.find_all('span','hw dhw')
    if word:
        for box in boxes_eng_found:
            eng_string = box.text.strip()
            break
    
    return eng_string,meaning_list


def cambrigde_translate(word):                                 #using in write_jsonfile
    try:
        eng_string,meaning_list =cambridge_th(word)
    except IndexError:
        eng_string,meaning_list = cambridge_noth(word)
        
    meaning_string =' '.join(meaning_list)
    meaning_string = re.sub('\n','',meaning_string)
    meaning_string = re.sub('"',"-",meaning_string)
   
    return eng_string,meaning_string




# eng_string,meaning_list   = cambrigde_translate("mean")
# print(eng_string)
# print(meaning_list)