#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv(r'C:\Users\okahya\Desktop\pandas github\1\nyc_weather.csv')
print(df)

# In[3]:


df['Temperature'].max()


# In[5]:


df['Humidity'][df['Events']=='Snow']


# In[10]:


df.fillna(0, inplace=True)
df['WindSpeedMPH'].mean()


# In[ ]:

print('asd')

