#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests

from bs4 import BeautifulSoup

import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}


url="https://www.imdb.com/chart/top/"

response=requests.get(url,headers=headers)

soup=BeautifulSoup(response.content,'html.parser')

soup.select('h3',class_='ipc-title__text')
movies=[]

for i in soup.select('h3',class_='ipc-title__text'):
    movies.append(i.text)

movies_250=[]
for i in movies:
    try:
        var=int(i.split('.')[0])
        movies_250.append(i)
    except:
        continue
print(*movies_250, sep='\n')


# In[6]:


import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch page: {response.status_code}")
    exit()

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the state data
table = soup.find('table', class_='wikitable')

# Initialize lists to store state names and populations
states = []
populations = []

# Extract column headers to determine the index of the population column
header_row = table.find('tr')
headers = [header.text.strip() for header in header_row.find_all('th')]
population_index = None
for i, header in enumerate(headers):
    if 'Population' in header:
        population_index = i
        break

if population_index is None:
    print("Population column not found.")
    exit()

# Extract data from the table rows
rows = table.find_all('tr')[1:]  # Exclude header row
for row in rows:
    # Extract data from table cells
    cells = row.find_all('td')
    if len(cells) >= population_index + 1:  # Ensure the population column exists
        state = cells[0].text.strip()
        population = cells[population_index].text.strip()

        # Append data to respective lists
        states.append(state)
        populations.append(population)
    else:
        print(" ")

# Print the extracted data
for state, population in zip(states, populations):
    print(f"State: {state}, Population: {population}")


# In[ ]:




