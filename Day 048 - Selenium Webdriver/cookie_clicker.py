import time

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://orteil.dashnet.org/experiments/cookie/ '

# Keep Chrome browser running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get(url)

time.sleep(2.0)

button = driver.find_element(By.ID, value='cookie')
for i in range(15):
    button.click()

store = driver.find_elements(By.XPATH, value='/html/body/div[4]/div[5]/div/div/b/text()[2]')
print(type(store))
print(len(store))
items = []
# for item in store:
#     name_cost_text = item.text.split('\n')
#     print(name_cost_text)
#     name = name_cost_text[0].split(' - ')[0]
#     print(name)
#     cost = name_cost_text[0].split(' - ')[1]
#     print(int(cost))





# while True:
#     if round(time.time()) % 5 == 0:

    # button.click()
