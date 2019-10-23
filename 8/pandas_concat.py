#!/usr/bin/env python
# coding: utf-8

# # <font color="purple"><h3 align="center">Pandas Concatenate Tutorial</h3></font>

# ## <font color='blue'>Basic Concatenation</font>

# In[1]:


import pandas as pd

india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
india_weather


# In[2]:


us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
us_weather


# In[3]:


df = pd.concat([india_weather, us_weather])
df


# ## <font color='blue'>Ignore Index</font>

# In[4]:


df = pd.concat([india_weather, us_weather], ignore_index=True)
df


# ## <font color='blue'>Concatenation And Keys</font>

# In[26]:


df = pd.concat([india_weather, us_weather], keys=["india", "us"])
df


# In[27]:


df.loc["us"]


# In[28]:


df.loc["india"]


# ## <font color='blue'>Concatenation Using Index</font>

# In[16]:


temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
}, index=[0,1,2])
temperature_df


# In[17]:


windspeed_df = pd.DataFrame({
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
}, index=[1,0])
windspeed_df


# In[24]:


df = pd.concat([temperature_df,windspeed_df],axis=1)
df


# ## <font color='blue'>Concatenate dataframe with series</font>

# In[20]:


s = pd.Series(["Humid","Dry","Rain"], name="event")
s


# In[23]:


df = pd.concat([temperature_df,s],axis=1)
df

