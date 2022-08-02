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

    driver.get('https://opensource-demo.orangehrmlive.com/index.php/leave/viewHolidayList')

    # Klik Add
    driver.find_element(By.NAME,"btnAdd").click()
    time.sleep(1)

    #Isi Name
    driver.find_element(By.NAME,"holiday[description]").send_keys("Test Libur 001")
    time.sleep(1)
    
    #Isi date
    driver.find_element(By.NAME,"holiday[date]").clear()
    time.sleep(1)
    driver.find_element(By.NAME,"holiday[date]").send_keys("2022-07-23")
    time.sleep(1)

    # Klik Repeats Annually
    driver.find_element(By.NAME,"holiday[description]").click()
    time.sleep(1)
    driver.find_element(By.NAME,"holiday[recurring]").click()
    time.sleep(1)

    #Select Full Day / Half Day
    mondays=driver.find_element(By.NAME,"holiday[length]")
    mon=Select(mondays)
    mon.select_by_visible_text('Half Day')
    time.sleep(1)

    #Select Full Day / Half Day
    mondays=driver.find_element(By.NAME,"holiday[length]")
    mon=Select(mondays)
    mon.select_by_visible_text('Full Day')
    time.sleep(1)

    #Klik Save
    driver.find_element(By.ID,"saveBtn").click()
    time.sleep(1)


finally:
    driver.close()
    driver.quit()
