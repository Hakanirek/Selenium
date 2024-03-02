from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/experiments/cookie/")


def buyfromstore(money):

    item_affordable = []

    items = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    #print(items)
    items_money = []
    for item in items:
        if item is not None:
            split_text = item.text.split()
            if split_text:
                items_money.append(split_text[-1])

    for n in range(len(items_money)):
        number = int(''.join(items_money[n].split(",")))

        if money > number:
            item_affordable.append(number)

    #print(item_affordable)

    if len(item_affordable) > 0:
        max_value = max(item_affordable)

        index_of_item = item_affordable.index(max_value)

        buy = items[index_of_item]
        buy.click()






timeout = time.time() + 5

count_five_minute = time.time() + 5*60


while True:
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()


    if time.time() > timeout:
        money = int(driver.find_element(By.ID, value="money").text)
        buyfromstore(money)

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    if time.time() > count_five_minute:
        cookies_second = driver.find_element(By.ID, value="cps").text
        print(f"CPS : {cookies_second}")
        break



