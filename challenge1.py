from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

# take the upcoming events from https://www.python.org/

events_date_tags = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li time")
events_date = [tag.text for tag in events_date_tags]
# print(events_date)

events_topic_tags = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events_topic = [tag.text for tag in events_topic_tags]
# print(events_topic)

events = {}

for i in range(len(events_topic)):
    events[i] = {"time": events_date[i],
                 "name": events_topic[i]}

print(events)

driver.quit()
