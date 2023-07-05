import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_driver_path = r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

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

clicks_per_second = 100


def cookie_clicking():
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()


def get_cookie_count():
    cookie_count_str = driver.find_element(By.ID, "money").text.replace(",", "")
    return int(cookie_count_str)


def get_closest_item(cookie_count):
    closest_value = None
    for value in items_dict.values():
        if value <= cookie_count:
            if closest_value is None or value > closest_value:
                closest_value = value
    return closest_value


def buy_item(item):
    item_to_buy = driver.find_element(By.CSS_SELECTOR, f"#{item} > b")
    item_to_buy.click()


while True:
    for _ in range(clicks_per_second):
        cookie_clicking()
    cookie_count = get_cookie_count()
    print("Cookie count:", cookie_count)
    closest_value = get_closest_item(cookie_count)
    if closest_value is not None:
        keys = [key for key, value in items_dict.items() if value == closest_value]
        item_to_buy_key = keys[0]
        buy_item(item_to_buy_key)
        print("Buying item:", item_to_buy_key)
    time.sleep(1)
    print("This is after 1 second")
    clicks_per_second += 100
