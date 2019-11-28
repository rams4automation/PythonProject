from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

driver.implicitly_wait(10)

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
wait=WebDriverWait(driver,10)

ele=wait.until(EC.element_to_be_clickable(By.name,'login'))

ele.click()

driver.close()