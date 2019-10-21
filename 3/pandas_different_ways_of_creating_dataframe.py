#!/usr/bin/env python
# coding: utf-8

# # <font color="purple"><h3 align="center">Different Ways Of Creating Dataframe</h3></font>

# ## <font color="green">Using csv</h3></font>

# In[4]:


import pandas as pd

df = pd.read_csv("weather_data.csv")
df


# ## <font color="green">Using excel</h3></font>

# In[6]:


df=pd.read_excel("weather_data.xlsx","Sheet1")
df


# ## <font color="green">Using dictionary</h3></font>

# In[7]:


weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)
df


# ## <font color="green">Using tuples list</h3></font>

# In[8]:


weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
df


# ## <font color="green">Using list of dictionaries</h3></font>

# In[9]:


weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
    
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
df

