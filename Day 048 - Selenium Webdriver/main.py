from selenium import webdriver
from selenium.webdriver.common.by import By

item_url = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/"
python_url = 'https://www.python.org/'

# Keep Chrome browser running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

# Getting the price of an Amazon iten
# driver.get(item_url)
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# item_price = float(f"{price_dollar}.{price_cents}")
# print(item_price)

# Python.org search bar
driver.get(python_url)

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
#
# # XPath (XML Path Language)
# bug_link = driver.find_element(By.XPATH, value='/html/body/div/footer/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# events = driver.find_elements(By.CLASS_NAME, value='event-widget li')
# events_dict = {}
# key_number = 0
# for event in events:
#     date_and_name = event.text.split("\n")
#     date = date_and_name[0]
#     name = date_and_name[1]
#     events_dict[key_number]={'time':date, 'name':name}
#     key_number += 1

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events = {n: {'time': event_times[n].text, 'name': event_names[n].text} for n in range(0, len(event_times))}

print(events)

# To close a single active tab
# driver.close()

# To quit the entire browser
driver.quit()
