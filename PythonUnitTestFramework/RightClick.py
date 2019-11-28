from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

time.sleep(5)

button=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

action=ActionChains(driver)

action.context_click(button).perform()

time.sleep(5)

driver.close()