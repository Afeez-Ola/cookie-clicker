from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_driver_path = r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

login_link = driver.find_element(By.CSS_SELECTOR,
                                 'body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis')
login_link.click()
email_field = driver.find_element(By.NAME, "session_key")
password_field = driver.find_element(By.NAME, "session_password")
email_address = "afeezbolajiola@gmail.com"
password = "Morenigbade1$"

email_field.send_keys(email_address)
password_field.send_keys(password)

login_button = driver.find_element(By.CSS_SELECTOR, '#organic-div > form > div.login__form_action_container > button')
login_button.click()

time.sleep(15)

wait_time = 20

# Wait for the elements to be present
wait = WebDriverWait(driver, wait_time)
jobs_link = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container__link")))
print(len(jobs_link))
for i in range(len(jobs_link)):
    print(len(jobs_link))
    print(jobs_link[i].text)
    job = jobs_link[i]
    ActionChains(driver).move_to_element(job).click().perform()
    time.sleep(2)
    try:
        easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        easy_apply.click()
        try:
            submit_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Submit application"]')
            submit_button.click()
        except NoSuchElementException:
            cancel = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            cancel.click()
            time.sleep(2)
            discard = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard.click()
    except NoSuchElementException:
        if i < len(jobs_link) - 1:
            job = jobs_link[i + 1]
