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

    # Klik Add
    driver.find_element(By.NAME,"btnAdd").click()
    time.sleep(1)

    # isi Firstname
    driver.find_element(By.NAME,"addCandidate[firstName]").send_keys("Selviany")
    time.sleep(1)

    # isi Middlename
    driver.find_element(By.NAME,"addCandidate[middleName]").send_keys("Candidate 001")
    time.sleep(1)

    # isi Lastname
    driver.find_element(By.NAME,"addCandidate[lastName]").send_keys("Automation")
    time.sleep(1) 

    # isi Email
    driver.find_element(By.NAME,"addCandidate[email]").send_keys("Candidate.selviany@gmail.com")
    time.sleep(1) 

    # isi Contact No
    driver.find_element(By.NAME,"addCandidate[contactNo]").send_keys("081320424426")
    time.sleep(1) 

    #Select Dropdown Job Vacancy
    jobvacancy=driver.find_element(By.NAME,"addCandidate[vacancy]")
    jv=Select(jobvacancy)
    jv.select_by_visible_text('Payroll Administrator')
    time.sleep(1)

    # isi Resume
    driver.find_element(By.NAME,"addCandidate[resume]").send_keys("C:/Users/ghiya/Pictures/sample.pdf")
    time.sleep(1)

    # isi Keywords
    driver.find_element(By.NAME,"addCandidate[keyWords]").send_keys("Automation is Best")
    time.sleep(1) 

    # isi Comment
    driver.find_element(By.NAME,"addCandidate[comment]").send_keys("This Comment is Automation")
    time.sleep(1)

    #Isi Date Of Aplication
    driver.find_element(By.NAME,"addCandidate[appliedDate]").clear()
    time.sleep(1)
    driver.find_element(By.NAME,"addCandidate[appliedDate]").send_keys("2022-07-23")
    time.sleep(1)
    driver.find_element(By.NAME,"addCandidate[firstName]").click()
    time.sleep(1)

    # Klik Consent to keep data
    driver.find_element(By.ID,"addCandidate_consentToKeepData").click()
    time.sleep(1)
    
    # Klik Save
    driver.find_element(By.ID,"btnSave").click()
    time.sleep(1)

    time.sleep(5)

finally:
    driver.close()
    driver.quit()
