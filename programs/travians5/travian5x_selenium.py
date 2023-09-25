from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://toc.x5.international.travian.com/build.php?id=32&gid=19")
# driver.close()#tab
# driver.quit()
print(driver.title)



# wait for  specific things to happen in the page before go
# waiting for the login form to appear
# login_form =WebDriverWait(driver ,30).until(
#     EC.presence_of_all_elements_located((By.NAME,"name"))
# )


# searching hirachie
# id -> name --> class
namet=driver.find_element_by_name("name")
namet.send_keys("tee")
# namet.send_keys(Keys.RETURN)
passt=driver.find_element_by_name("password")
passt.send_keys("20112536123")
passt.send_keys(Keys.RETURN)
# print(driver.page_source)  toprint html sourcecode

driver.get("https://toc.x5.international.travian.com/build.php?id=32&gid=19")
so_num=driver.find_element_by_name('t2')
so_num.send_keys("20")
so_num.send_keys(Keys.RETURN)
# insideVil.click()

time.sleep(5)
driver.quit()