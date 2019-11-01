from copy import deepcopy
import requests
from bs4 import BeautifulSoup as bs

#taken all the pages from 1980 to 2019 (change the value of 1980 to take more pages)
pages = []
a = "http://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?class=2;id="
b = ";type=year"
for i in range (1980,2020):
    pages.append(a+str(i)+b)

temp = [0]*40   #1980 to 2019 (for year wise run scored) 

hashmap = {} 
for year in range (1980,2020):
    data = requests.get(pages[year-1980])
    soup = bs(data.text,'html.parser')
    table = soup.find('table', attrs={'class':'engineTable'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for i in rows:
        row_data = i.find_all('td')
        x = row_data[0].prettify()
        x = x.split('\n')
        #print(x)
        name = x[2].strip()
        name+=" "
        name+= x[4].strip()
        #getting runs scored
        x = row_data[4].prettify()
        x = x.split('\n')
        #print(x)
        runs = int(x[2].strip())
        if(name in hashmap):
            l = hashmap[name]
            l[year-1980] = runs
            hashmap[name]=l
        else:
            l = list(temp)
            l[year-1980] = runs
            hashmap[name]=l

#for key,value in hashmap.items():
#    print(key,value,sep=' : ')

#Cummulative sum
mycopy = deepcopy(hashmap)
for key,value in mycopy.items():
    for i in range (1,40):
        value[i]+=value[i-1]

#printing names of all the players with their scores till today
for key,value in mycopy.items():
    print(key,value[39],sep = ' : ')

#printing runs by virat kohli till 2014
mycopy['V Kohli (INDIA)'][2014-1980]
#printing runs by Sachin Tendulkar till 1995
mycopy['SR Tendulkar (INDIA)'][1995-1980]



