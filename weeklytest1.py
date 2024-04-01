#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Extract question title and body
question_title = soup.find('h1', class_='fs-headline1').text.strip()
question_body = soup.find('div', class_='s-prose js-post-body').text.strip()

# Print question title and body
#print("Question Title:", question_title)
#print("Question Body:", question_body)

# Extract and print answers
answer_divs = soup.find_all('div', class_='answercell post-layout--right')
for i, answer_div in enumerate(answer_divs, start=1):
    answer_body = answer_div.find('div', class_='s-prose js-post-body').text.strip()
    code_blocks = answer_div.find_all('code', class_='lang-py s-code-block')
    print(f"Answer {i}:", answer_body)
    print("Code Blocks:")
    for code_block in code_blocks:
        print(code_block.text.strip())


# In[ ]:




