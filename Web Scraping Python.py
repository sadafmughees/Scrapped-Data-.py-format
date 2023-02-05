#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install beautifulsoup4


# In[2]:


pip install requests


# In[3]:


import requests
import bs4

url=("https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api")
response=requests.get(url)
print(type(response))
print(response.text)


# In[9]:


url=requests.get("https://ieg.worldbankgroup.org/data")


# In[10]:


url.content


# In[11]:


url.status_code


# In[12]:


url.encoding


# In[13]:


url.headers


# In[14]:


url.headers['Date']


# In[15]:


from bs4 import BeautifulSoup


# In[16]:


soup=BeautifulSoup(url.content,'html.parser')


# In[17]:


soup.title


# In[18]:


for para in soup.find_all('p'):
    print(para.text)


# In[ ]:


for table in soup.find_all('div', id='')
    for rows in table.find_all('tr')
        print(rows.text)

