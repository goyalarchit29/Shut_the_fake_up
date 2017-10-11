
link = 'http://www.fakenewsai.com/'
# address = raw_input()
address = 'http://www.fakingnews.firstpost.com/india/supreme-court-firecrackers-pil-diwali-23627'
# soup = BeautifulSoup(r.text,'html.parser')
# address = 'http://google.com'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def verifyLink(address):
	driver = webdriver.Chrome()
	driver.get(link)
	# assert "Python" in driver.title
	elem = driver.find_element_by_name("url")
	elem.clear()
	elem.send_keys(address)
	elem.send_keys(Keys.RETURN)
	# assert "No results found." not in driver.page_source
	time.sleep(2.5)
	ans = driver.find_element_by_xpath("/html/body")
	attributeValue = ans.get_attribute("style")
	driver.close()
	# green real
	if str(attributeValue) == "background-color: rgb(0, 153, 0);":
		return 1
	else :
		return 0

if __name__ == "__main__":
	aaddress = 'http://www.fakingnews.firstpost.com/india/supreme-court-firecrackers-pil-diwali-23627'
	print verifyLink(address)