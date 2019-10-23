#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue" align="center">Pandas Time Series Tutorial: DateTimeIndex</h1>

# In[5]:


import pandas as pd
df = pd.read_csv("aapl.csv",parse_dates=["Date"], index_col="Date")
df.head(2)


# In[6]:


df.index


# <h3 style="color:purple">What is DatetimeIndex? Benefits of it</h3>

# <h4> (1) Partial Date Index: Select Specific Months Data</h4>

# In[7]:


df['2017-06-30']


# In[19]:


df["2017-01"]


# In[8]:


df['2017-06'].head() 


# <h4>Average price of aapl's stock in June, 2017</h4>

# In[9]:


df['2017-06'].Close.mean()


# In[10]:


df['2017'].head(2) 


# <h4>(2) Select Date Range</h4>

# In[11]:


df['2017-01-08':'2017-01-03']


# In[12]:


df['2017-01']


# <h3 style="color:purple">Resampling</h3>

# In[13]:


df['Close'].resample('M').mean().head()


# In[14]:


df['2016-07']


# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
df['Close'].plot()


# In[16]:


df['Close'].resample('M').mean().plot(kind='bar')

