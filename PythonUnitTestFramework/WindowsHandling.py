from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("http://demo.automationtesting.in/Windows.html")

time.sleep(5)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

Mainwindow=driver.current_window_handle

print(Mainwindow)

handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    driver.title
    print(driver.title)
    time.sleep(5)
    if driver.title == "Sakinalium | Home":
       driver.close()

time.sleep(5)

driver.quit()