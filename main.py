# selenium automated the web scrapping
# Like create a robot
from selenium import webdriver

# Keep  Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# For giving the website
driver.get("https://www.amazon.com")

# driver.close()  # close a single tab
driver.quit()  # close the all tabs
