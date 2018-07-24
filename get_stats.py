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

#using Google Chrome browser, requires Chrome Driver to be installed into PATH
driver = webdriver.Chrome('C:/Chrome_Driver/chromedriver.exe')

#access fantasy football scout members
driver.get('http://members.fantasyfootballscout.co.uk')

#input user name and password
driver.find_element(by='name', value='username').send_keys(username)
driver.find_element(by='name', value='password').send_keys(password)
driver.find_element(by='name', value='login').click()

#get involvement data
driver.get('https://members.fantasyfootballscout.co.uk/team-stats/involvement/')
table = driver.find_element_by_class_name('stats')
body = table.find_element_by_tag_name('tbody')
body_rows = body.find_elements_by_tag_name('tr')

for row in body_rows:
    data = row.find_elements_by_tag_name('td')
    file_row = []
    for datum in data:
        datum_text = datum.text
        file_row.append(datum_text)
    involv_data.append(','.join(file_row))

#write involvement data into csv
with open(save_location + '/involvement_data.csv', 'wb') as f:
	wr = csv.writer(f, dialect='excel')
	wr.writerows(involv_data)

#get distribution data
driver.get('https://members.fantasyfootballscout.co.uk/team-stats/distribution/')
table = driver.find_element_by_class_name('stats')
body = table.find_element_by_tag_name('tbody')
body_rows = body.find_elements_by_tag_name('tr')

for row in body_rows:
    data = row.find_elements_by_tag_name('td')
    file_row = []
    for datum in data:
        datum_text = datum.text
        file_row.append(datum_text)
    dist_data.append(','.join(file_row))

#write distribution data into csv
with open(save_location + '/dist_data.csv', 'wb') as f:
	wr = csv.writer(f, dialect='excel')
	wr.writerows(dist_data)

#get defending data
driver.get('https://members.fantasyfootballscout.co.uk/team-stats/defending/')
table = driver.find_element_by_class_name('stats')
body = table.find_element_by_tag_name('tbody')
body_rows = body.find_elements_by_tag_name('tr')

for row in body_rows:
    data = row.find_elements_by_tag_name('td')
    file_row = []
    for datum in data:
        datum_text = datum.text
        file_row.append(datum_text)
    def_data.append(','.join(file_row))

#write defence data into csv
with open(save_location + '/defence_data.csv', 'wb') as f:
	wr = csv.writer(f, dialect='excel')
	wr.writerows(def_data)

#get attacking data
driver.get('https://members.fantasyfootballscout.co.uk/team-stats/goal-threat/')
table = driver.find_element_by_class_name('stats')
body = table.find_element_by_tag_name('tbody')
body_rows = body.find_elements_by_tag_name('tr')

for row in body_rows:
    data = row.find_elements_by_tag_name('td')
    file_row = []
    for datum in data:
        datum_text = datum.text
        file_row.append(datum_text)
    attack_data.append(','.join(file_row))

#write attacking data into csv
with open(save_location + '/attacking_data.csv', 'wb') as f:
	wr = csv.writer(f, dialect='excel')
	wr.writerows(attack_data)
	
#get set pieces data
driver.get('https://members.fantasyfootballscout.co.uk/team-stats/set-pieces/')
table = driver.find_element_by_class_name('stats')
body = table.find_element_by_tag_name('tbody')
body_rows = body.find_elements_by_tag_name('tr')

for row in body_rows:
    data = row.find_elements_by_tag_name('td')
    file_row = []
    for datum in data:
        datum_text = datum.text
        file_row.append(datum_text)
    set_pieces_data.append(','.join(file_row))

#write set pieces data into csv
with open(save_location + '/set_pieces_data.csv', 'wb') as f:
	wr = csv.writer(f, dialect='excel')
	wr.writerows(set_pieces_data)
	
#get expected data
driver.get('https://members.fantasyfootballscout.co.uk/team-stats/set-pieces/')
table = driver.find_element_by_class_name('stats')
body = table.find_element_by_tag_name('tbody')
body_rows = body.find_elements_by_tag_name('tr')

for row in body_rows:
    data = row.find_elements_by_tag_name('td')
    file_row = []
    for datum in data:
        datum_text = datum.text
        file_row.append(datum_text)
    ex_data.append(','.join(file_row))

#write expected data into csv
with open(save_location + '/expected_data.csv', 'wb') as f:
	wr = csv.writer(f, dialect='excel')
	wr.writerows(ex_data)

