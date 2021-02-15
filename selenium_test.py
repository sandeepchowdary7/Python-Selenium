import selenium
from selenium.webdriver.common.keys import Keys

driver = selenium.webdriver.Chrome('chromedriver')
driver.get("https://www.yelp.com/search")
print(driver.title)
search_bar = driver.find_element_by_name("find_desc")
search_bar1 = driver.find_element_by_name("find_loc")
search_bar.clear()
search_bar1.clear()
search_bar.send_keys("Plumbers")
search_bar1.send_keys("Atlanta, GA")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()