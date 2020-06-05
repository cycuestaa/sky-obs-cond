#!/usr/bin/env python
# coding: utf-8

# In[13]:


import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime


# In[14]:


url= 'https://www.wunderground.com/history/daily/us/ca/santa-rosa/KSTS/date/'
query = input("Request day: yyyy-mm-dd")
page = requests.get(url+query)
print(page)
soup =  BeautifulSoup(page.content,'html.parser')
print(soup)


# In[6]:


table = soup.find_all('table')
raw_data = [row.text.splitlines() for row in table]
raw_data = raw_data[:-9]
for i in range(len(raw_data)):
 raw_data[i] = raw_data[i][2:len(raw_data[i]):3]
print(raw_data)
print(table)
type(raw_data)


# In[ ]:




