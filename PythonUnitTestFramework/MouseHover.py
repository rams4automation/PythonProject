from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://demoqa.com/menu/")

time.sleep(9)

Music=driver.find_element_by_xpath("//*[@id='ui-id-9']")
Rock=driver.find_element_by_xpath("//*[@id='ui-id-10']")
Alternative=driver.find_element_by_xpath("//*[@id='ui-id-11']")

time.sleep(9)

action=ActionChains(driver)
action.move_to_element(Music).move_to_element(Rock).move_to_element(Alternative).click().perform()

time.sleep(9)

driver.close()




