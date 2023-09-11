import time

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://orteil.dashnet.org/cookieclicker/'

# Keep Chrome browser running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get(url)

time.sleep(3.0)
dismiss = driver.find_element(By.CLASS_NAME, value='cc_btn_accept_all')
dismiss.click()

time.sleep(1.0)
language = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
language.click()

time.sleep(2.0)

button = driver.find_element(By.XPATH, value='//*[@id="bigCookie"]')

while True:
    if round(time.time()) % 5 == 0:
        time.sleep(2)
    button.click()
