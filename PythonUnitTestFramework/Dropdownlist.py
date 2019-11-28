
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

time.sleep(9)

element=driver.find_element_by_id("select-demo")

drpdwn=Select(element)

time.sleep(9)

drpdwn.select_by_value("Sunday")

time.sleep(9)

##Count number of options

print(len(drpdwn.options))

## Capture all the options and print them as output

time.sleep(9)

all_options=drpdwn.options

for option in all_options:
    print(option.text)


driver.close()


