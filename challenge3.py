from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://secure-retreat-92358.herokuapp.com/")

# Input fname
fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Hakan")
time.sleep(2)

# Input lname
lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("İrek")
time.sleep(2)

# Input email
email = driver.find_element(By.NAME, value="email")
email.send_keys("hakan134134@gmail.com")
time.sleep(2)

# Button
button = driver.find_element(By.CLASS_NAME, value="btn-block")
button.click()

time.sleep(2)

#driver.quit()

