#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue" align="center">Pandas Time Series Analysis Tutorial: to_datetime</h1>

# In[14]:


import pandas as pd
dates = ['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05','20170105']
pd.to_datetime(dates)


# In[13]:


dt = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05','20170105']
pd.to_datetime(dt)


# <h3 style="color:purple">European style dates with day first</h3>

# In[7]:


pd.to_datetime('30-12-2016')


# In[8]:


pd.to_datetime('5-1-2016', dayfirst=True)


# <h3 style="color:purple">Custom date time format</h3>

# In[3]:


pd.to_datetime('2017$01$05', format='%Y$%m$%d')


# In[4]:


pd.to_datetime('2017#01#05', format='%Y#%m#%d')


# <h3 style="color:purple">Handling invalid dates</h3>

# In[5]:


pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='ignore')


# In[6]:


pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='coerce')


# <h3 style="color:purple">Epoch</h3>

# **Epoch or Unix time means number of seconds that have passed since Jan 1, 1970 00:00:00 UTC time**

# In[15]:


current_epoch = 1501324478
pd.to_datetime(current_epoch, unit='s')


# In[16]:


pd.to_datetime(current_epoch*1000, unit='ms')


# In[17]:


t = pd.to_datetime([current_epoch], unit='s')
t


# In[18]:


t.view('int64')

