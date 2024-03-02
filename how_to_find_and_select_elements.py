from selenium import webdriver
from selenium.webdriver.common.by import By

# https://www.selenium.dev/documentation/webdriver/elements/locators/
# https://selenium-python.readthedocs.io/api.html#locate-elements-by
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
""" 
# Amazon price tracker
driver.get("https://www.amazon.com/dp/B08PHT7JKG/ref=sbl_dpx_kitchen-electric-cookware_B01NBKTPTS_0")

# for find the elements we can use find_element function.
# With that we can use By class to find the particular elements
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# These are will return selenium object
# print(price_dollar)
# print(price_cents)

# For reach the value use **(text)**
print(price_dollar.text)
print(price_cents.text)
"""
# ***************************finding the element by name**************************************
driver.get("https://www.python.org")

# finding the element by name
search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar)# it will be a selenium element
# For getting the specific attributes value use get_attribute()
# print(search_bar.get_attribute("placeholder"))

# ***************************finding the element by id**************************************
# finding the element by id
submit_button = driver.find_element(By.ID, value="submit")
# print(submit_button.size)


# ****************************finding the element by Css Selector**************************************
# finding the element by css selector

# When a particular tag has no id, name, or class.
# We can use css selector to reach the element
docs_links = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

# print(docs_links.text)


# **************************** finding the element by Xpath **************************************
# https://www.w3schools.com/xml/xpath_intro.asp
# Xpath: is a way to located the specific html element. By a path structure

bug_link = driver.find_element(By.XPATH, value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")

# print(bug_link.get_attribute("href"))

# **************************** finding the more elements  **************************************
# using the fins_elements() method for finding to all the tags which we want



driver.quit()  # close the all tabs
