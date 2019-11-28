from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(5)

driver.switch_to_frame(0)

path="C://Users//Ramesh//Desktop//siva//RelivingLetter.jpg"

driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-11']").send_keys(path)