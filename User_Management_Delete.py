from datetime import date, datetime
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException



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

    driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers')

    # isi Serach Username
    driver.find_element(By.NAME,"searchSystemUser[userName]").send_keys("NewSelviany")
    time.sleep(1)

    #Select Dropdown User Role
    searchuserrole=driver.find_element(By.NAME,"searchSystemUser[userType]")
    sur=Select(searchuserrole)
    sur.select_by_visible_text('Admin')
    time.sleep(1)

    # isi Serach Employee Name
    driver.find_element(By.NAME,"searchSystemUser[employeeName][empName]").send_keys("Admin A")
    time.sleep(1)

    #Select Dropdown Status
    searchstatus=driver.find_element(By.NAME,"searchSystemUser[status]")
    sst=Select(searchstatus)
    sst.select_by_visible_text('Enabled')
    time.sleep(1)
    
    # Klik Serach
    driver.find_element(By.ID,"searchBtn").click()
    time.sleep(3)

#==========================================================================================================

    # Klik Check Box By Search
    driver.find_element(By.NAME,"chkSelectRow[]").click()
    time.sleep(1)

    # Klik Delete
    driver.find_element(By.NAME,"btnDelete").click()
    time.sleep(1)
    
    # Klik Delete Confirm
    driver.find_element(By.ID,"dialogDeleteBtn").click()
    time.sleep(1)


finally:
    driver.close()
    driver.quit()
