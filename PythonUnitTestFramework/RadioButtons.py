
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.toolsqa.com/automation-practice-form/")

driver.find_element_by_id("cookie_action_close_header").click()

time.sleep(5)

status=driver.find_element_by_id("sex-0").is_selected()

print(status)

time.sleep(9)

driver.find_element_by_id("sex-0").click()

time.sleep(9)

status=driver.find_element_by_id("sex-0").is_selected()

print(status)

time.sleep(5)



driver.close()
