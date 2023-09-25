from ast import Return
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

to_vill ="1T"
from_vill_ids=["23751","24629"]
username ="tee"
password = "20112536123"

for i in from_vill_ids:
    market_url ="https://ts3.x1.asia.travian.com/build.php?newdid="+i+"&id=32&t=5&gid=17"

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome('C://chromedriver//chromedriver.exe',options=option)

    driver.get(market_url)


    namet = driver.find_element(By.NAME,"name")
    namet.send_keys(username)
    passt = driver.find_element(By.NAME,"password")
    passt.send_keys(password)
    time.sleep(6)
    passt.send_keys(Keys.RETURN)
    time.sleep(6)


    driver.get(market_url)
    for sub in ["r1","r2","r3","r4"]:
        element = driver.find_element(By.ID,sub)
        element.send_keys("1000")
        element.send_keys(Keys.RETURN)

    villname = driver.find_element(By.ID,"enterVillageName")
    villname.send_keys(to_vill)
    villname.send_keys(Keys.RETURN)
    time.sleep(5)
    confirmbutt = driver.find_element(By.ID,"enabledButton")
    confirmbutt.click()
    time.sleep(2)
    driver.quit()