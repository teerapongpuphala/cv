from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re,time


option = webdriver.ChromeOptions()
option.add_argument('headless')
driver=webdriver.Chrome("C://chromedriver//chromedriver.exe",options=option)
driver.get("https://translate.google.co.th/?sl=ko&tl=en&op=translate")
# driver.close()#tab
# driver.quit()
# print(driver.title)

ko_word=driver.find_element_by_class_name("er8xn")
with open('rossetta.txt','r',encoding='utf-8') as file:
    for line in file:
        result = re.sub(r'[0-9]','',line).lstrip().rstrip()
        if result==" " or result =="\n" or result=="":continue
        ko_word.send_keys(Keys.CONTROL,"A")
        ko_word.send_keys(Keys.BACKSPACE)
        ko_word.send_keys(result)
        
        wait_for_mean =WebDriverWait(driver ,30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,"Q4iAWc"))
        )

        eng_mean = driver.find_element_by_class_name("J0lOec")     
        fix_eng_mean = re.sub('\n',' ',eng_mean.text)
        with open('rossetta_kotoen.csv','a',encoding='utf-8') as new:
            new.write(result.strip()+","+fix_eng_mean+"\n")

driver.quit()