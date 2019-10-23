#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue;" align="center">Pandas Time Series Analysis Tutorial: date_range</h1>

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("aapl_no_dates.csv")
df.head()


# In[20]:


rng = pd.date_range(start="6/1/2016",end="6/30/2016",freq='B')
rng


# In[5]:


df.set_index(rng, inplace=True)
df.head()


# <h3 style="color:purple">Finding missing dates from datetimeindex</h3>

# In[28]:


daily_index = pd.date_range(start="6/1/2016",end="6/30/2016",freq='D')
daily_index


# In[31]:


daily_index.difference(df.index)


# <h3 style="color:purple">Benefits of having DatetimeIndex</h3>

# In[30]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.plot()


# In[7]:


df["2016-06-01":"2016-06-10"].Close.mean()


# <h3 style="color:purple">asfreq</h3>

# In[8]:


df.index


# In[9]:


df.asfreq('D',method='pad')


# In[10]:


df.asfreq('W',method='pad')


# In[11]:


df.asfreq('H',method='pad')


# <h3 style="color:purple"> generating DatetimeIndex with periods argument</h3>

# In[12]:


rng = pd.date_range('1/1/2011', periods=72, freq='H')
rng


# In[13]:


import numpy as np
ts = pd.Series(np.random.randint(0,10,len(rng)), index=rng)
ts.head(20)

