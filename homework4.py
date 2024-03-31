#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft"


response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")


table = soup.find("table", class_="wikitable")


data = []
for row in table.find_all("tr")[1:]: 
    columns = row.find_all("td")
    if len(columns) >= 4:  
        aircraft_type = columns[0].text.strip()
        origin = columns[1].text.strip()
        in_service = columns[2].text.strip()
        notes = columns[3].text.strip()
        data.append({"Aircraft Type": aircraft_type, "Origin": origin, "In Service": in_service, "Notes": notes})

for entry in data:
    print(entry)


# In[ ]:




