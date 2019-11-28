from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.toolsqa.com/automation-practice-table/")

driver.find_element_by_id("cookie_action_close_header").click()

time.sleep(5)

rows=len(driver.find_elements_by_xpath("//*[@id='content']/table/tbody/tr"))
cols=len(driver.find_elements_by_xpath("//*[@id='content']/table/tbody/tr[1]/td"))

print(rows)
print(cols)

for r in range(1,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element_by_xpath("//*[@id='content']/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='     ')
    print()

time.sleep(5)

driver.close()