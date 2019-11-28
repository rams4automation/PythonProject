
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.eenadu.net/")

driver.maximize_window()

print(driver.title)       ## Eenadu

time.sleep(5)

driver.get("https://www.espncricinfo.com/")

print(driver.title)       ## espncricinfo

time.sleep(5)

driver.back()

print(driver.title)      ## Eenadu

time.sleep(5)

driver.forward()

time.sleep(5)

print(driver.title)     ## espncricinfo

driver.quit()