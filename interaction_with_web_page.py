from selenium import webdriver
from selenium.webdriver.common.by import By

# Keys class contain a lot of constant like enter, shift
from selenium.webdriver.common.keys import Keys  #

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# for click on it
# article_count.click()


# ****************************** finding elements by their text ********************
# we can use By.LINK_TEXT for a button or a text for clicking
all_portal = driver.find_element(By.LINK_TEXT, value="View source")
all_portal.click()

# ******************************** Typing in a search bar *******************
search = driver.find_element(By.NAME, value="search")  # this method will find the location of the search bar
search.send_keys("Python")  # this method will type into the search bar

# This will find the enter from Keys class end put into the send_keys method
search.send_keys(Keys.ENTER)


driver.quit()
