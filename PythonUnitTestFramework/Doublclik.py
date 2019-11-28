from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://artoftesting.com/sampleSiteForSelenium")

time.sleep(9)

dblelement=driver.find_element_by_id("dblClkBtn")

action=ActionChains(driver)
action.double_click(dblelement).perform()

time.sleep(5)

driver.quit()

