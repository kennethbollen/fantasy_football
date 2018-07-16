#py3

import bs4
import requests
import pandas as pd

teams = []
odds = []
decimal_odds = []
ranking = []

#function used to convert string fraction odds into decimals (source: https://stackoverflow.com/questions/1806278/convert-fraction-to-float)

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

url = 'https://www.betvictor.com/en-gb/sports/football/eng-premier-league-outright/coupons/100/54920110/0/4432/0/PE/0/0/0/0/1'
r = requests.get(url)
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'lxml')

#web scrap teams 
for link in soup.find_all('span', {'class': 'outcome_description outcome-bet-button-desc'}):
    teams.append(link.text)

#web scrap odds and convert into decimal betting odds
for link in soup.find_all('span', {'class': 'price outcome-bet-button-price'}):
    odds.append(link.text)

for i in odds:
    decimal_odds.append(1 + convert_to_float(i))
    
#setup prem league ranking 
for i in range(1, 21):
    number.append(i)
    
#create dataframe for teams and odds
df = pd.DataFrame({'teams': teams, 'odds': decimal_odds,}, index= ranking)

#calculate the implied probability based on the betting odds 
df['implied_probability'] = round((1 / df['odds']) * 100, 2)


