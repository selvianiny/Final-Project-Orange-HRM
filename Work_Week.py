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

    driver.get('https://opensource-demo.orangehrmlive.com/index.php/leave/defineWorkWeek')

    # Klik Edit
    driver.find_element(By.ID,"saveBtn").click()
    time.sleep(1)

    #Select Monday
    mondays=driver.find_element(By.NAME,"WorkWeek[day_length_Monday]")
    mon=Select(mondays)
    mon.select_by_visible_text('Full Day')
    time.sleep(1)

    #Select Tuesday
    tuesdays=driver.find_element(By.NAME,"WorkWeek[day_length_Tuesday]")
    tue=Select(tuesdays)
    tue.select_by_visible_text('Half Day')
    time.sleep(1)

    #Select Wednesday
    wednesdays=driver.find_element(By.NAME,"WorkWeek[day_length_Wednesday]")
    wed=Select(wednesdays)
    wed.select_by_visible_text('Full Day')
    time.sleep(1)

    #Select Thursday
    thursdays=driver.find_element(By.NAME,"WorkWeek[day_length_Thursday]")
    thu=Select(thursdays)
    thu.select_by_visible_text('Half Day')
    time.sleep(1)

    #Select Friday
    fridays=driver.find_element(By.NAME,"WorkWeek[day_length_Friday]")
    fri=Select(fridays)
    fri.select_by_visible_text('Full Day')
    time.sleep(1)

    #Select Saturday
    saturdays=driver.find_element(By.NAME,"WorkWeek[day_length_Saturday]")
    sat=Select(saturdays)
    sat.select_by_visible_text('Non-working Day')
    time.sleep(1)

    #Select Sunday
    sundays=driver.find_element(By.NAME,"WorkWeek[day_length_Sunday]")
    sun=Select(sundays)
    sun.select_by_visible_text('Non-working Day')
    time.sleep(1)

    #Klik Save
    driver.find_element(By.ID,"saveBtn").click()
    time.sleep(1)


finally:
    driver.close()
    driver.quit()
