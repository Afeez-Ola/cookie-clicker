import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

closest_value = None


def cookie_clicking(cookie):
    cookie.click()


cookie = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "cookie"))
)
clicks_per_second = 100

items_dict = {
    "buyCursor": 15,
    "buyGrandma": 100,
    "buyFactory": 500,
    "buyMine": 2000,
    "buyShipment": 7000,
    "buyAlchemy": 50000,
    "buyPortal": 1000000,
    "buyTime": 123456789
}
items = [item for item in items_dict.keys()]


def closest_item():
    global closest_value
    for value in items_dict.values():
        if value <= cookie_count:
            if closest_value is None or value > closest_value:
                closest_value = value
    if closest_value is not None:
        for key, value in items_dict.items():
            if value == closest_value:
                return closest_value


# for price in items_dict.values():
#     print(price)

while True:
    for _ in range(clicks_per_second):
        cookie_clicking(cookie)
        cookie_count = int((driver.find_element(By.ID, "money")).text.replace(",", ""))
    print(cookie_count)
    keys = [key for key, val in items_dict.items() if val == closest_item()]
    item_to_buy = (driver.find_element(By.CSS_SELECTOR, f"#{keys[0]} > b"))
    item_to_buy.click()
    print(keys[0])
    time.sleep(5)
    print("this is after 5 seconds")
    clicks_per_second = clicks_per_second + 50
