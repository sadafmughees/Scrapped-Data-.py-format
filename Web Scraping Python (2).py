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


# In[4]:


url=requests.get("https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api")


# In[5]:


url.content


# In[6]:


url.status_code


# In[7]:


url.encoding


# In[8]:


url.headers


# In[9]:


url.headers['Date']


# In[10]:


from bs4 import BeautifulSoup


# In[11]:


soup=BeautifulSoup(url.content,'html.parser')


# In[12]:


soup.title


# In[13]:


for para in soup.find_all('p'):
    print(para.text)


# In[14]:


url1 = 'url.csv'


# In[15]:


url1


# In[16]:


import pandas as pd


# In[17]:


soup.select('body')


# In[18]:


import pandas as pd


# In[19]:


import requests


# In[ ]:





# In[20]:


url = ("https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api")


# In[21]:


response = requests.get(url).content


# In[22]:


url = "https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api"


# In[23]:


import bs4


# In[24]:


for para in soup.find("p"):
    print(para)


# In[25]:


for para in soup.find_all("p"):
    print(para)


# In[26]:


for para in soup.find_all("p"):
    print(para.text)


# In[27]:


for links in soup.find_all("a"):
    link = links.get('href')
    print(link)


# In[ ]:




