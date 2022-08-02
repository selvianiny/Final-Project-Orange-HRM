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
from selenium.webdriver.common.keys import Keys




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

    driver.get('https://opensource-demo.orangehrmlive.com/index.php/performance/searchPerformancReview')

    # Klik Add
    driver.find_element(By.ID,"btnAdd").click()
    time.sleep(1)


    # isi Employee
    driver.find_element(By.NAME,"saveReview360Form[employee]").send_keys("Fiona ")
    time.sleep(1)
    driver.find_element(By.NAME,"saveReview360Form[employee]").send_keys("Grace")
    time.sleep(1)
    driver.find_element(By.NAME,"saveReview360Form[employee]").send_keys(Keys.ENTER)

    time.sleep(5)
    
    # isi Supervisor Reviewer
    driver.find_element(By.NAME,"saveReview360Form[supervisorReviewer]").send_keys("Odis ")
    time.sleep(1)
    driver.find_element(By.NAME,"saveReview360Form[supervisorReviewer]").send_keys("Adalwin")
    time.sleep(1)
    driver.find_element(By.NAME,"saveReview360Form[supervisorReviewer]").send_keys(Keys.ENTER)

    time.sleep(5)

    # isi Work Period Start Date 
    driver.find_element(By.NAME,"saveReview360Form[workPeriodStartDate]").clear()
    driver.find_element(By.NAME,"saveReview360Form[workPeriodStartDate]").send_keys("2022-07-31")
    time.sleep(1)
    driver.find_element(By.NAME,"saveReview360Form[workPeriodStartDate]").send_keys(Keys.ENTER)
    driver.find_element(By.NAME,"saveReview360Form[supervisorReviewer]").click()
    time.sleep(1)


    # isi Work Period End Date
    driver.find_element(By.NAME,"saveReview360Form[workPeriodEndDate]").clear()
    driver.find_element(By.NAME,"saveReview360Form[workPeriodEndDate]").send_keys("2022-12-10")
    time.sleep(1)
    driver.find_element(By.NAME,"saveReview360Form[workPeriodEndDate]").send_keys(Keys.ENTER)
    driver.find_element(By.NAME,"saveReview360Form[supervisorReviewer]").click()
    time.sleep(1)

    # isi Due Date
    driver.find_element(By.NAME,"saveReview360Form[dueDate]").clear()
    driver.find_element(By.NAME,"saveReview360Form[dueDate]").send_keys("2022-12-31")
    time.sleep(1)
    driver.find_element(By.NAME,"saveReview360Form[dueDate]").send_keys(Keys.ENTER)
    driver.find_element(By.NAME,"saveReview360Form[supervisorReviewer]").click()
    time.sleep(1)
    
    # Klik Active
    driver.find_element(By.ID,"activateBtn").click()
    time.sleep(1)

#==========================================================================================================

    # isi Employee Name
    driver.find_element(By.NAME,"performanceReview360SearchForm[employeeName]").send_keys("Fiona Grace")
    time.sleep(1)

    # isi Reviewer
    driver.find_element(By.NAME,"performanceReview360SearchForm[reviwerName]").send_keys("Odis Adalwin")
    time.sleep(1)

    # Klik Evaluate
    driver.find_element(By.LINK_TEXT,"Evaluate").click()
    time.sleep(1)

#==========================================================================================================

    # isi KPI
    driver.find_element(By.ID,"rating_118").send_keys("60")
    driver.find_element(By.ID,"comment_118").send_keys("Comment 118")
    driver.find_element(By.ID,"rating_119").send_keys("70")
    driver.find_element(By.ID,"comment_119").send_keys("Comment 119")
    driver.find_element(By.ID,"rating_120").send_keys("80")
    driver.find_element(By.ID,"comment_120").send_keys("Comment 120")
    driver.find_element(By.ID,"rating_121").send_keys("90")
    driver.find_element(By.ID,"comment_121").send_keys("Comment 121")
    driver.find_element(By.ID,"rating_122").send_keys("100")
    driver.find_element(By.ID,"comment_122").send_keys("Comment 122")
    driver.find_element(By.ID,"general_comment_1").send_keys("Comment General")
    time.sleep(1)

    # isi Final Comment
    driver.find_element(By.NAME,"reviewEvaluation[hrAdminComments]").send_keys("This is Final Comment")
    time.sleep(1)

    # isi Rating
    driver.find_element(By.NAME,"reviewEvaluation[finalRating]").send_keys("This is Final Rating")
    time.sleep(1)

    # isi Completed Date
    driver.find_element(By.NAME,"reviewEvaluation[completedDate]").send_keys("2022-10-20")
    time.sleep(1)

    # Klik Complete
    driver.find_element(By.ID,"completeBtn").click()
    time.sleep(1)

    time.sleep(5)

finally:
    driver.close()
    driver.quit()
