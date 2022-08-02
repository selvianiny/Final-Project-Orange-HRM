from datetime import date, datetime
import os
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement




s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window ()

driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
try:
    # isi Username
    driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
    time.sleep(1) 

    # isi password
    driver.find_element(By.NAME,"txtPassword").send_keys("admin123")
    time.sleep(1)

    # Klik Login
    driver.find_element(By.ID,"btnLogin").click()
    time.sleep(1)

#==========================================================================================================

    driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/payGrade')

    # isi Username
    driver.find_element(By.NAME,"payGrade[name]").send_keys("Test Grade 0001")
    time.sleep(1) 

    # Klik Save
    driver.find_element(By.ID,"btnSave").click()
    time.sleep(1)

    # Klik Add
    driver.find_element(By.ID,"btnAddCurrency").click()
    time.sleep(1)

    # isi Currency
    driver.find_element(By.NAME,"payGradeCurrency[currencyName]").send_keys("IDR - Indonesian Rupiah")
    time.sleep(1) 

    # isi Minimum Salary
    driver.find_element(By.NAME,"payGradeCurrency[minSalary]").send_keys("5000000")
    time.sleep(1) 

    # isi Maximum Salary
    driver.find_element(By.NAME,"payGradeCurrency[maxSalary]").send_keys("15000000")
    time.sleep(1) 

    # Klik Add
    driver.find_element(By.ID,"btnSaveCurrency").click()
    time.sleep(1)

finally:
    driver.close()
    driver.quit()
