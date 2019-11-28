from PythonUnitTestFramework import Excelutils

from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("http://newtours.demoaut.com/")

path="D://Python//TestData.xlsx"

rows= Excelutils.getRowCount(path, "Sheet2")

for r in range(2,rows+1):
    Username= Excelutils.ReadData(path, "Sheet2", r, 1)
    Password = Excelutils.ReadData(path, "Sheet2", r, 1)
    driver.find_element_by_name("userName").send_keys(Username)
    driver.find_element_by_name("password").send_keys(Password)
    time.sleep(5)
    driver.find_element_by_name("login").click()
    time.sleep(5)
    driver.back()
