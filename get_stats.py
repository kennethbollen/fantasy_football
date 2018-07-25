#py3!

from selenium import webdriver

#username and password
username = 'ukza17'
password = 'Antwerp11'

#save csv directory
save_location = '/Users/2024450/Documents/Stats/fpl/csv_files'

#store data
invol_data = []
dist_data = []
def_data = []
att_data = []
set_pieces_data = []
ex_data = []
metrics = [involv_data, dist_data, def_data, att_data, set_pieces_data, ex_data]
web_metrics = ['involvement', 'distribution', 'defending', 'goal-threat', 'set-pieces', 'expected']
	       
#using Google Chrome browser, requires Chrome Driver to be installed into PATH
driver = webdriver.Chrome('C:/Chrome_Driver/chromedriver.exe')

#access fantasy football scout members
driver.get('http://members.fantasyfootballscout.co.uk')

#input user name and password
driver.find_element(by='name', value='username').send_keys(username)
driver.find_element(by='name', value='password').send_keys(password)
driver.find_element(by='name', value='login').click()

for i in range(len(metrics)):
	driver.get('https://members.fantasyfootballscout.co.uk/team-stats/%s/' % web_metrics[i])
	table = driver.find_element_by_class_name('stats')
	body = table.find_element_by_tag_name('tbody')
	body_rows = body.find_elements_by_tag_name('tr')
	
	for row in body_rows:
		data = row.find_elements_by_tag_name('td')
		file_row = []
		for datum_text = datum.text
		file_row.append(datum_text)
	metrics[i].append(','.join(file_row))
	
	with open(save_location + '/%s.csv' % web_metrics[i], "w") as f:
		f.write('/n'.join(metrics[i]))
