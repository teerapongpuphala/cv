from bs4 import BeautifulSoup
import requests
import urllib.parse

userName = "cersei"
password = "22052537"
mainURL = "https://ts5.travian.asia"



def login(url):
    session = requests.Session()
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

    response= session.post(postUrl,data=postData)
    return response

def get_link_list(res):
    villList=[]
    soupDorfOutside= BeautifulSoup(res.content,"html.parser")
    villes=soupDorfOutside.findAll('div',class_='content')
    try:
        villagesBlock = villes[5].find_all('ul')[0].find_all('li')   
    except IndexError:
        villagesBlock = villes[4].find_all('ul')[0].find_all('li')   #chrome at 11.15 villes[4]

    dorf = "https://ts5.travian.asia/dorf1.php"
    for li in villagesBlock:
        name = li.a.span.text.strip()
        path = li.a['href']
        corX = li.find('span',class_='coordinateX').string.strip('(')
        corY = li.find('span',class_='coordinateY').string.strip(')')
        villLink = urllib.parse.urljoin(dorf,path)
        villList.append((name,villLink,corX,corY))
    return villList


url = "https://ts5.travian.asia/login.php"

res = login(url)
resultList = get_link_list(res)

i = 0
for name,link,x,y in resultList:
    print(str(i)+"  "+name+"      "+link+"      "+x+","+y)
    i+=1

choosenVilleLink = resultList[int(input("Number :  "))][1]

# ----------------------------------------------------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------------------------------------------
response = session.get("https://ts5.travian.asia/build.php?tt=2&id=39")
soup= BeautifulSoup(response.content,"html.parser")

formSendTroop = soup.form
actionSendTroop = formSendTroop.get("action")


postUrlTroop = urllib.parse.urljoin("https://ts5.travian.asia/build.php?tt=2&id=39",actionSendTroop)
print(postUrlTroop)

postTroopData={}

allInput = formSendTroop.find_all('input')

for element in allInput:
    if 'troop' in element["name"]: continue
    if element["name"] =='x' or element["name"] =='y' or element['name'] == 'c': continue
    postTroopData[element["name"]] = element["value"]
print(postTroopData)


trs = formSendTroop.table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        try:
            troopType = td.img.get('alt')
        except AttributeError:
            continue
        try:
            numbers = td.a.string.strip()
        except AttributeError:
            continue

        name = td.input["name"]
        postTroopData[name] = input(troopType+" : "+numbers+" |   ") 
        

sendToDo =formSendTroop.find('div',class_='option').input.get('name')
postTroopData[sendToDo] = input("2-support   : 3-attakt : 4-steal   :  ")
posXname =formSendTroop.div.div.find('div',class_="xCoord").input.get('name')
postTroopData[posXname]=input("X Position   : ")
posYname =formSendTroop.div.div.find('div',class_="yCoord").input.get('name')
postTroopData[posYname]=input("Y Position   : ")

buttonName = formSendTroop.button.get('name')
postTroopData[buttonName]="submit"

res22= session.post(postUrlTroop,data=postTroopData)

# -----------------------------------------------------------------------------------------------------------------------

url ='https://ts5.travian.asia/build.php?gid=16&tt=2'

soup = BeautifulSoup(res22.content,"html.parser")

form = soup.find_all('form')[0]

action = form.get('action')
method = form.get('method')

postUrlTroop = urllib.parse.urljoin("https://ts5.travian.asia",action)

confirmDicts={}

inputsList = soup.form.find_all('input')
for element in inputsList:
    confirmDicts[element["name"]] = element["value"]

formButton = soup.form.find_all('button')[2]
confirmDicts[formButton["name"]] = formButton['value']

resultEnd = session.post(postUrlTroop,data=confirmDicts)

