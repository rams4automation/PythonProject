
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

driver.implicitly_wait(10)

time.sleep(9)

links=driver.find_elements(By.TAG_NAME, "a")
print("Number of links :", len(links))

for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT, "REGISTER").click()

time.sleep(5)

driver.close()





