from bs4 import BeautifulSoup
import requests
import urllib.parse
from itistime import Itisthetime
import datetime




userName = "tee"
password = "20112536123"
mainURL = "https://ts3.x1.asia.travian.com/"



def login_get_villsdetail(url):
    # session = requests.Session()
    response = requests.get(url)

    soup= BeautifulSoup(response.content,"html.parser")

    formaction = soup.form['action']
    formmethod = soup.form['method']

    postUrl = urllib.parse.urljoin(url,formaction)

    nameInput = soup.form.tr.findAll('td')[1].input.get('name')
    passwordInput = soup.form.findAll('tr')[1].findAll('td')[1].input.get('name')
    buttonInput = soup.form.findAll('tr')[4].findAll('td')[1].button.get('name')

    postData={}
    postData[nameInput]=userName
    postData[passwordInput]=password
    postData[buttonInput]='submit'

    response= requests.post(postUrl,data=postData)

    villList=[]
    soupDorfOutside= BeautifulSoup(response.content,"html.parser")
    villes=soupDorfOutside.findAll('div',class_='content')
    print(villes)
    try:
        villagesBlock = villes[5].find_all('ul')[0].find_all('li')   
    except IndexError:
        villagesBlock = villes[4].find_all('ul')[0].find_all('li')   #chrome at 11.15 villes[4]

    dorf = "https://ts3.x1.asia.travian.com/dorf1.php"
    for li in villagesBlock:
        name = li.a.span.text.strip()
        path = li.a['href']
        corX = li.find('span',class_='coordinateX').string
        corY = li.find('span',class_='coordinateY').string
        villLink = urllib.parse.urljoin(dorf,path)
        villList.append((name,villLink,corX,corY))
    return villList

#1-get all vill details
url = "https://ts3.x1.asia.travian.com/login.php"
resultList = login_get_villsdetail(url)

#2-choose village's link
i = 0
for name,link,x,y in resultList:
    print(str(i)+"  "+name+"      "+link+"      "+x+","+y)
    i+=1

choosenVilleLink = resultList[int(input("Number :  "))][1]

#3-login with choosen vill's link  and make session to get to other link without loging out
session = requests.Session()
response = session.get(choosenVilleLink)
soup= BeautifulSoup(response.content,"html.parser")

formLogin = soup.form
formaction = formLogin['action']
formmethod = formLogin['method']

postUrl = urllib.parse.urljoin(url,formaction)

nameInput = formLogin.tr.findAll('td')[1].input.get('name')
passwordInput = formLogin.findAll('tr')[1].findAll('td')[1].input.get('name')
buttonInput = formLogin.findAll('tr')[4].findAll('td')[1].button.get('name')

postData={}
postData[nameInput]=userName
postData[passwordInput]=password
postData[buttonInput]='submit'

resOutside= session.post(postUrl,data=postData)

#4- choose type of send ,troop numbers 
response = session.get("https://ts3.x1.asia.travian.com/build.php?id=39&tt=2")
soup= BeautifulSoup(response.content,"html.parser")

formSendTroop = soup.form
actionSendTroop = formSendTroop.get("action")


postUrlTroop = urllib.parse.urljoin(mainURL,actionSendTroop)
# print(postUrlTroop)

postTroopData={}

allInput = formSendTroop.find_all('input')

for element in allInput:
    if 'troop' in element["name"]: continue
    if element["name"] =='x' or element["name"] =='y' or element['name'] == 'c': continue
    postTroopData[element["name"]] = element["value"]
# print(postTroopData)


trs = formSendTroop.table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        try: troopType = td.img.get('alt')
        except AttributeError: continue
        try: numbers = td.a.string.strip()
        except AttributeError: continue

        name = td.input["name"]
        postTroopData[name] = input(troopType+" : "+numbers+" |   ") 
        

sendToDo =formSendTroop.find('div',class_='option').input.get('name')
postTroopData[sendToDo] = input("2-support   : 3-attack : 4-steal   :  ")
posXname =formSendTroop.div.div.find('div',class_="xCoord").input.get('name')
postTroopData[posXname]=input("X Position   : ")
posYname =formSendTroop.div.div.find('div',class_="yCoord").input.get('name')
postTroopData[posYname]=input("Y Position   : ")

buttonName = formSendTroop.button.get('name')
postTroopData[buttonName]="submit"

resp= session.post(postUrlTroop,data=postTroopData)

#5-confirm and time calculation

soup = BeautifulSoup(resp.content,"html.parser")

form = soup.find_all('form')[0]

action = form.get('action')
method = form.get('method')

postUrlTroop = urllib.parse.urljoin(mainURL,action)


confirmDicts={}
inputsList = soup.form.find_all('input')
for element in inputsList:
    confirmDicts[element["name"]] = element["value"]

formButton = soup.form.find_all('button')[2]
confirmDicts[formButton["name"]] = formButton['value']


timeSpendString = form.find('div',class_='in').string.split(' ')[1]
print("Spending---------------------------"+timeSpendString+"------------------------------")
DateTmeDestinationString = input("Arrive time(inform tt-mm-ss) at : ")

myTime = Itisthetime(DateTmeDestinationString,timeSpendString)
# myTime.timeDelay = 3.45
# biger myTime.timeDelay ---> faster
# smaller myTime.timeDelay ---> slower

if(myTime.send_time()):
    resultEnd = session.post(postUrlTroop,data=confirmDicts)
    print("DONE!")
