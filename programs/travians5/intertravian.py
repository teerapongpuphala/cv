from cgi import print_environ
from ctypes.wintypes import PINT
from random import randint
from bs4 import BeautifulSoup
import requests
import urllib.parse

userName = "tee"
password = "20112536123"
mainURL = "https://toc.x5.international.travian.com"

session= requests.Session()
response = session.get(mainURL)
print(response)
soup= BeautifulSoup(response.content,"html.parser")

formaction = soup.form['action']
formmethod = soup.form['method']

postUrl = urllib.parse.urljoin(mainURL,formaction)

nameInput = soup.form.tr.findAll('td')[1].input.get('name')
passwordInput = soup.form.findAll('tr')[1].findAll('td')[1].input.get('name')
buttonInput = soup.form.findAll('tr')[4].findAll('td')[1].button.get('name')
postData={}
postData[nameInput]=userName
postData[passwordInput]=password
postData[buttonInput]='submit'

response= session.post(postUrl,data=postData)


bildding_list_check  = session.get("https://toc.x5.international.travian.com/dorf1.php")
list_soup = BeautifulSoup(bildding_list_check.content,"html.parser")
in_process = list_soup.find('div',class_='finishNow')

if in_process:
    print("in process")
    exit
else:
    for num in range(1,3):
        try:
            randid = randint(1,18)
            gid1 =[1,3,14,17]
            gid2 =[5,6,16,18]
            gid3 =[4,7,10,11]
            gid4 =[2,8,9,12,13,15]
            if randid in gid1: gid = "gid=1"
            if randid in gid2: gid = "gid=2"
            if randid in gid3: gid = "gid=3"
            if randid in gid4: gid = "gid=4"

            upgt_response =session.get("https://toc.x5.international.travian.com/build.php?id="+str(randid)+"&"+gid)
            print(upgt_response)
            bttpopup = BeautifulSoup(upgt_response.content,"html.parser")
            butt =  bttpopup.find('button',class_='textButtonV1 green build')
            post_id = butt['id']
            print(post_id)
            post_value = butt['value']
            if "หัวหน้าคนก่อสร้าง" in post_value:continue
            post_path = butt['onclick'].split("'")[1]
            print(post_id,post_value,post_path)

            sendurl = urllib.parse.urljoin("https://toc.x5.international.travian.com",post_path)
            postData={}
            postData["value"]=post_value
            postData["id"]=post_id

            response= session.post(sendurl,data=postData)
        except:
            print("Error")
            continue

