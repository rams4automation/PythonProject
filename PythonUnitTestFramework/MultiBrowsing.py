from selenium import webdriver

##driver=webdriver.chrome(executable_path="D:\\PythonProject\\Drivers\\chromedriver.exe")

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.google.com/")

driver.maximize_window()

print(driver.title)

driver.close()



