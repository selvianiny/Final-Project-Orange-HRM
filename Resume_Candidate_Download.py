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

    driver.get('https://opensource-demo.orangehrmlive.com/index.php/recruitment/viewCandidates')

    #Select Dropdown Vacancy
    searchvacancy=driver.find_element(By.NAME,"candidateSearch[jobVacancy]")
    sv=Select(searchvacancy)
    sv.select_by_visible_text('Senior QA Lead')
    time.sleep(5)
    searchvacancy=driver.find_element(By.NAME,"candidateSearch[jobVacancy]")
    sv=Select(searchvacancy)
    sv.select_by_visible_text('Senior QA Lead')
    time.sleep(5)

    #Find Candidate Name
    driver.find_element(By.NAME,"candidateSearch[candidateName]").send_keys("Peter Smith")
    time.sleep(1)

    #disctract Keyword
    driver.find_element(By.NAME,"candidateSearch[keywords]").click()
    time.sleep(2)

    # Klik Serach
    driver.find_element(By.ID,"btnSrch").click()
    time.sleep(5)

    # Klik Download
    driver.find_element(By.LINK_TEXT,"Download").click()
    time.sleep(1)
    
    time.sleep(5)

finally:
    driver.close()
    driver.quit()
