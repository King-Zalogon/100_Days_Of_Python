from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

wikipedia_url = 'https://en.wikipedia.org/wiki/Main_Page'
signup_url = 'http://secure-retreat-92358.herokuapp.com/'

# Keep Chrome browser running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get(wikipedia_url)

article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount > a:nth-child(1)')
# print(article_count.text)
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

search = driver.find_element(By.NAME, value='search')
search.send_keys('Python')
# button = driver.find_element(By.CLASS_NAME, value='cdx-search-input__end-button')
# button.click()
search.send_keys(Keys.ENTER)

driver.get(signup_url)
first_name = driver.find_element(By.NAME, value='fName')
first_name.send_keys('John')
last_name = driver.find_element(By.NAME, value='lName')
last_name.send_keys('Doe')
email = driver.find_element(By.NAME, value='email')
email.send_keys('notrealmail@notmail.com')
button = driver.find_element(By.CLASS_NAME, value='btn-block')
button.click()

# THE END #
# driver.quit()
