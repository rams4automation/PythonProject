
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

driver.implicitly_wait(10)

# 1st Method to get Screenshot
##driver.save_screenshot("D://Python//Homepage.png")

# 2nd Method to get Screenshots
driver.get_screenshot_as_file("D://Python//Homepage2.jpg")

driver.close()

