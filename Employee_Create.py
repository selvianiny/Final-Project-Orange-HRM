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

    driver.get('https://opensource-demo.orangehrmlive.com/index.php/pim/addEmployee')

    # isi Firstname
    driver.find_element(By.NAME,"firstName").send_keys("Selviany")
    time.sleep(1)

    # isi Middlename
    driver.find_element(By.NAME,"middleName").send_keys("Test001")
    time.sleep(1)

    # isi Lastname
    driver.find_element(By.NAME,"lastName").send_keys("Automation")
    time.sleep(1) 

    # isi Photofile
    driver.find_element(By.NAME,"photofile").send_keys("C:/Users/ghiya/Pictures/samplepict.jpg")
    time.sleep(1)

    # Klik Create Login Detail
    driver.find_element(By.ID,"chkLogin").click()
    time.sleep(1)

    # isi Username
    driver.find_element(By.NAME,"user_name").send_keys("SelvianyAutomation0001")
    time.sleep(1) 

    # isi Password
    driver.find_element(By.NAME,"user_password").send_keys("Selviany04.")
    time.sleep(1) 

    # isi Confirm Password
    driver.find_element(By.NAME,"re_password").send_keys("Selviany04.")
    time.sleep(1) 

    #Select Dropdown Status
    createstatus=driver.find_element(By.NAME,"status")
    cst=Select(createstatus)
    cst.select_by_visible_text('Enabled')
    time.sleep(1)

    # Klik Save
    driver.find_element(By.ID,"btnSave").click()
    time.sleep(1)

finally:
    driver.close()
    driver.quit()
