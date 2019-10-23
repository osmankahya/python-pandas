#!/usr/bin/env python
# coding: utf-8

# ## <font color="maroon"><h4 align="center">Handling Missing Data - replace method</font>

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv("weather_data.csv")
df


# **Replacing single value**

# In[2]:


new_df = df.replace(-99999, value=np.NaN)
new_df


# **Replacing list with single value**

# In[41]:


new_df = df.replace(to_replace=[-99999,-88888], value=0)
new_df


# **Replacing per column**

# In[5]:


new_df = df.replace({
        'temperature': -99999,
        'windspeed': -99999,
        'event': '0'
    }, np.nan)
new_df


# **Replacing by using mapping**

# In[3]:


new_df = df.replace({
        -99999: np.nan,
        'no event': 'Sunny',
    })
new_df


# **Regex**

# In[84]:


# when windspeed is 6 mph, 7 mph etc. & temperature is 32 F, 28 F etc.
new_df = df.replace({'temperature': '[A-Za-z]', 'windspeed': '[a-z]'},'', regex=True) 
new_df


# **Replacing list with another list**

# In[42]:


df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
df


# In[43]:


df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])

