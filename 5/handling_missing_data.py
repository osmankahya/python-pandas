#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("weather_data.csv", parse_dates=["day"])
df.set_index('day',inplace=True)
df


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.temperature.plot.bar()


# In[4]:


new_df = df.fillna({
        'temperature': 0,
        'windspeed': 0,
        'event': 'no event'
    })
new_df


# In[11]:


new_df = df.fillna(0)
new_df


# In[19]:


new_df = df.fillna(method="ffill")
new_df


# In[22]:


new_df = df.interpolate(method="time")
new_df


# In[27]:


new_df = df.dropna(thresh=1) # (how="all") 
new_df


# In[17]:


dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
df

