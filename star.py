from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(url)
print(page)

soup = bs(page.text, 'html.parser')

startable = soup.find('table')

temp_list = []
table_rows = startable.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Name = []
Distance = []
Mass = []
Radius = []

for i in range(1, len(temp_list)):
    Name.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    
dfe = pd.DataFrame(list(zip(Name, Distance, Mass, Radius)), columns = ['Name', 'Distance', 'Mass', 'Radius'])
print(dfe)

dfe.to_csv('star.csv')