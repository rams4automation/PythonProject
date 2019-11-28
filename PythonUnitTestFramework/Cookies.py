from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")

cokies=driver.get_cookies()
print(len(cokies))

print(cokies)

##driver.add_cookie("")

driver.delete_all_cookies()

cokies=driver.get_cookies()
print(len(cokies))
print(cokies)

driver.close()


