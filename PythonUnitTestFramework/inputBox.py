from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.toolsqa.com/automation-practice-form/")

driver.implicitly_wait(10)

driver.find_element_by_id("cookie_action_close_header").click()

time.sleep(5)

inputboxes=driver.find_elements_by_class_name("control-group")

print(inputboxes)

time.sleep(5)

driver.find_element_by_name("firstname").send_keys("mercury")
driver.find_element_by_id("lastname").send_keys("mercury")

time.sleep(5)

driver.close()