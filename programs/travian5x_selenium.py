from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('C://chromedriver//chromedriver.exe',options=option)


# driver=webdriver.Chrome('C://chromedriver//chromedriver.exe')
driver.get("https://toc.x5.international.travian.com/build.php?newdid=17043&id=32&gid=19")
# driver.close()#tab
# driver.quit()
print(driver.title)



# wait for  specific things to happen in the page before gos
# waiting for the login form to appear
# login_form =WebDriverWait(driver ,30).until(
#     EC.presence_of_all_elements_located((By.NAME,"name"))
# )


# searching hirachie
# id -> name --> class
namet=driver.find_element_by_name("name")
# namet = driver.find_element(By.NAME,"name")
namet.send_keys("tee")
time.sleep(5)

# namet.send_keys(Keys.RETURN)
passt=driver.find_element_by_name("password")
time.sleep(5)

# passt = driver.find_element(By.NAME,"password")
passt.send_keys("20112536123")
time.sleep(5)

passt.send_keys(Keys.RETURN)
# print(driver.page_source)  toprint html sourcecode
time.sleep(5)
driver.get("https://toc.x5.international.travian.com/build.php?newdid=17043&id=32&gid=19")
time.sleep(5)
so_num=driver.find_element_by_name('t2')

# so_num = driver.find_element(By.NAME,"t2")
so_num.send_keys("20")
so_num.send_keys(Keys.RETURN)
# insideVil.click()
time.sleep(5)
driver.get("https://toc.x5.international.travian.com/build.php?id=34&gid=20")
time.sleep(5)
so_num=driver.find_element_by_name('t6')
so_num.send_keys("20")
so_num.send_keys(Keys.RETURN)

time.sleep(2)
driver.quit()