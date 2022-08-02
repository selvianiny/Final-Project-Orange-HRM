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
    driver.find_element(By.NAME,"txtUsername").send_keys("Admin") # isi Username
    time.sleep(1)
    driver.find_element(By.NAME,"txtPassword").send_keys("admin123") # isi password
    time.sleep(1)
    driver.find_element(By.ID, "btnLogin").click()
    time.sleep(1)

finally:
    driver.close()
    driver.quit()
