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

    driver.get('https://opensource-demo.orangehrmlive.com/index.php/performance/searchKpi')

    #Select Dropdown Job
    searchjob=driver.find_element(By.NAME,"kpi360SearchForm[jobTitleCode]")
    sj=Select(searchjob)
    sj.select_by_visible_text('QA Lead')
    time.sleep(5)

    # Klik Search
    driver.find_element(By.ID,"searchBtn").click()
    time.sleep(1)

    # Klik Add
    driver.find_element(By.ID,"btnAdd").click()
    time.sleep(1)

#==========================================================================================================
   
    #Select Dropdown Job
    jobtittle=driver.find_element(By.NAME,"defineKpi360[jobTitleCode]")
    jt=Select(jobtittle)
    jt.select_by_visible_text('QA Lead')
    time.sleep(2)

    # isi Key Performance Indicator
    driver.find_element(By.NAME,"defineKpi360[keyPerformanceIndicators]").send_keys("Automation Testing")
    

    # isi Minimum Rating
    driver.find_element(By.NAME,"defineKpi360[minRating]").clear()
    driver.find_element(By.NAME,"defineKpi360[minRating]").send_keys("50")
    

    # isi Maximum Rating 
    driver.find_element(By.NAME,"defineKpi360[maxRating]").clear()
    driver.find_element(By.NAME,"defineKpi360[maxRating]").send_keys("100")
    

    # Klik Make Default Scale
    driver.find_element(By.NAME,"defineKpi360[makeDefault]").click()
    time.sleep(1)

    # Klik Save
    driver.find_element(By.ID,"saveBtn").click()
    time.sleep(1)

    time.sleep(5)

finally:
    driver.close()
    driver.quit()
