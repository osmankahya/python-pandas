#!/usr/bin/env python
# coding: utf-8

# In[98]:


import pandas as pd
df = pd.read_csv("fb.csv",parse_dates=['Date'],index_col='Date')
df


# <img src="shift_image.png" />

# <h2 style="color:purple">Shift</h2>

# In[115]:


df.shift(1)


# In[100]:


df.shift(-1)


# In[101]:


df['Prev Day Price'] = df['Price'].shift(1)
df


# In[102]:


df['Price Change'] = df['Price'] - df['Prev Day Price']
df


# In[103]:


df['5 day return'] =  (df['Price'] - df['Price'].shift(5))*100/df['Price'].shift(5)
df


# In[104]:


df = df[['Price']]
df


# <h2 style="color:purple">tshift</h2>

# In[105]:


df.index


# In[106]:


df.index = pd.date_range(start='2017-08-15',periods=10, freq='B')
df


# In[107]:


df.index


# In[110]:


df.tshift(1)

