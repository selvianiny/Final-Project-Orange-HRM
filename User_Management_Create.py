from datetime import date, datetime
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select



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

    driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/saveSystemUser')

    #Select Dropdown User Role
    userrole=driver.find_element(By.NAME,"systemUser[userType]")
    ur=Select(userrole)
    ur.select_by_visible_text('Admin')
    time.sleep(1)

    # isi Employee Name
    driver.find_element(By.NAME,"systemUser[employeeName][empName]").send_keys("Admin A")
    time.sleep(1)

    # isi Username
    driver.find_element(By.NAME,"systemUser[userName]").send_keys("Selviany")
    time.sleep(1)

    # isi Status
    status=driver.find_element(By.NAME,"systemUser[status]")
    st=Select(status)

    st.select_by_visible_text('Enabled')
    time.sleep(1)

    # isi Password
    driver.find_element(By.NAME,"systemUser[password]").send_keys("Selviany123")
    time.sleep(1)

    # isi Confirm Password
    driver.find_element(By.NAME,"systemUser[confirmPassword]").send_keys("Selviany123")
    time.sleep(1)

    # Klik Save
    driver.find_element(By.ID,"btnSave").click()
    time.sleep(1)

finally:
    driver.close()
    driver.quit()
