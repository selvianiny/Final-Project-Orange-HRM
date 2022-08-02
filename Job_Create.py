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

    driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/saveJobTitle')

    # isi Username
    driver.find_element(By.NAME,"jobTitle[jobTitle]").send_keys("UserTester001")
    time.sleep(1) 

    # isi Description
    driver.find_element(By.NAME,"jobTitle[jobDescription]").send_keys("This is Dummy Testing and the name is UserTester001")
    time.sleep(1) 

    # isi Job Specification
    driver.find_element(By.NAME,("jobTitle[jobSpec]")).send_keys("C:/Users/ghiya/Pictures/samplepict.jpg")
    time.sleep(1) 

    # isi Note
    driver.find_element(By.NAME,"jobTitle[note]").send_keys("This is Dummy Testing and the name is UserTester001")
    time.sleep(1) 

    # Klik Save
    driver.find_element(By.ID,"btnSave").click()
    time.sleep(1)

    time.sleep(10)

finally:
    driver.close()
    driver.quit()
