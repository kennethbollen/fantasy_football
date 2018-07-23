#py3!

from selenium import webdriver

#PATH used to access google chrome
path = 'C:/Chrome_Driver/chromedriver.exe'

#username and password
username = ''
password = ''


#using Google Chrome browser, requires Chrome Driver to be installed into PATH
driver = webdriver.Chrome(path)

#access fantasy football scout members access page
driver.get('https://members.fantasyfootballscout.co.uk/')

#input user name and password
driver.find_element(by='name', value='username').send_keys(username)
driver.find_element(by='name', value='password').send_keys(password)
driver.find_element(by='name', value='login').click()
