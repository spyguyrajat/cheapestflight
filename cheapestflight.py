from selenium import webdriver
import time
#set range of dates for flight
for i in range(14,30):
	try:
		j = str(i)
		#get url from google.com/flights with specified conditions like the url above and replace it.
		url = "https://www.google.com/flights?hl=en#flt=BLR.IXR.2020-10-"+j+";c:INR;e:1;s:0;sd:1;t:f;tt:o"
		#print(url)
		driver = webdriver.Chrome()
		driver.get(url)
		time.sleep(5)
		print(i, driver.find_element_by_css_selector('.gws-flights-results__cheapest-price').text)
		driver.quit()

	except:
		continue
