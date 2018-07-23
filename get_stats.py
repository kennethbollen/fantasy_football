#py3!

from selenium import webdriver

#PATH used to access google chrome
path = 'C:/Chrome_Driver/chromedriver.exe'

#username and password
username = ''
password = ''


#using Google Chrome browser, requires Chrome Driver to be installed into PATH
driver = webdriver.Chrome(path)

#access fantasy football scout
driver.get('https://fantasyfootballscout.co.uk/')

#input user name and password
driver.find_element(by='name', value='log').send_keys(username)
driver.find_element(by='name', value='pwd').send_keys(password)
driver.find_element(by='name', value='wp-submit').click()

#enter members area
driver.get('http://members.fantasyfootballscout.co.uk')

#get defending data
driver.get('https://members.fantasyfootballscout.co.uk/team-stats/defending/')
body = table.find_element_by_tag_name('tbody')
body_rows = body.find_elements_by_tag_name('tr')
for row in body_rows:
	data = row.find_elements_by_tag_name('td')
	for datum in data:
		print(datum.text)
