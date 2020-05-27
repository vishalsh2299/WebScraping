import pandas as pd
import requests
from bs4 import  BeautifulSoup

page  = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XrgeNmgzbIU')
soup = BeautifulSoup(page.content, 'html.parser') # beautiful soup provides structured data
#print(soup.find_all('a'))
# using this we get the source code we can find different things like we find anchor tag 'a' above
week = soup.find(id='seven-day-forecast-body') # copy id from the inspect of the div that we want
#print(week) # it will show the contents of the div whose id we selected

items = week.find_all(class_ = 'forecast-tombstone') # we used _ with class as we have class as keyword
#print(items[0])
# we choosed this class as it contains most of the info that we want


# now below are the info that we need from the website print them and check
items[0].find(class_ ='period-name').get_text() # we are getting these id's from the html
items[0].find(class_ = 'short-desc').get_text()
items[0].find(class_ = 'temp').get_text()

# now we will get all period names // we saw one from the items list above
period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_ = 'short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

#print(period_names)
#print(short_descriptions)
#print(temperatures)

# we used pandas. it will provide the data in a table the format //not exactly
weather_stuff = pd.DataFrame(
    {
        'period' : period_names, # storing list of period_names with key period
        'short_descriptions' : short_descriptions,
        'temperatures' : temperatures,

    })

#print(weather_stuff)

weather_stuff.to_csv('weather.csv') # it will create the csv file
# we created csv file from the data taken from online