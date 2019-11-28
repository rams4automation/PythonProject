
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

driver.maximize_window()

user_ele=driver.find_element_by_name("userName")

print(user_ele.is_displayed())

print(user_ele.is_enabled())

pwd_ele=driver.find_element_by_name("password")

print(pwd_ele.is_displayed())

print(pwd_ele.is_enabled())

############ Enter UserName and Password

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name("login").click()

time.sleep(5)

roundtripbutton=driver.find_element_by_name("tripType")

print(roundtripbutton.is_selected())

driver.close()
