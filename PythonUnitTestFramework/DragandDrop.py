from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

time.sleep(5)

source_ele=driver.find_element_by_xpath("//*[@id='box6']")
taget_ele=driver.find_element_by_xpath("//*[@id='box106']")

action=ActionChains(driver)
action.drag_and_drop(source_ele,taget_ele).perform()

time.sleep(5)

driver.close()