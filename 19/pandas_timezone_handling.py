#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue" align="center">Pandas Time Series Analysis: Handling Time Zones</h1>

# **We live in a world with different timezones. If you are having morning coffee in new york at 9 AM it might be a time for dinner in Mumbai, India because it would be 6.30 PM there. Handling time zone could become necessity while doing time series analysis in Pandas**

# <img src="timezones_world_map.png" />

# **Read microsoft's intraday stock prize**

# In[149]:


import pandas as pd
df = pd.read_csv("msft.csv", header=1,index_col='Date Time',parse_dates=True)
df


# In[150]:


df.index


# <h3>Two types of datetimes in python</h3>
# <ol>
#     <li>Naive (no timezone awareness)</li>
#     <li>Timezone aware datetime</li>
# <ol>

# <h3 style="color:purple">Convert naive DatetimeIndex to timezone aware DatetimeIndex using tz_localize</h3>

# In[151]:


df.tz_localize(tz='US/Eastern')
df


# In[152]:


df.index = df.index.tz_localize(tz='US/Eastern')
df.index


# <h3 style="color:purple">Convert to Berlin time using tz_convert</h3>

# In[153]:


df = df.tz_convert('Europe/Berlin')
df


# In[154]:


df.index


# In[138]:


from pytz import all_timezones
print (all_timezones)


# <h3 style="color:purple">Convert to Mumbai time</h3>

# In[139]:


df.index = df.index.tz_convert('Asia/Calcutta') # tz database doesn't have any Mumbai timezone but calcutta and mumbai are both in same timezone so we will use that
df


# <h3 style="color:purple">Using timezones in date_range</h3>

# <h4 style="color:green">(1) timezone using pytz</h4>

# In[140]:


london = pd.date_range('3/6/2012 00:09:00', periods=10, freq='H',tz='Europe/London')
london


# <h4 style="color:green">(2) timezone using dateutil</h4>

# In[141]:


td = pd.date_range('3/6/2012 00:00', periods=10, freq='H',tz='dateutil/Europe/London')
td


# 
# <h3>Pandas documentation indicates that difference between pytz timezone and dateutil timezones is</h3>
# <ol>
#     <li>In pytz you can find a list of common (and less common) time zones using from pytz import common_timezones, all_timezones</li>
#     <li>dateutil uses the OS timezones so there isn’t a fixed list available. For common zones, the names are the same as pytz</li>
# <ol>

# <h3 style="color:purple">Airthmetic between different timezones</h3>

# In[155]:


rng = pd.date_range(start="2017-08-22 09:00:00",periods=10, freq='30min')
s = pd.Series(range(10),index=rng)
s


# In[156]:





# In[157]:


b = s.tz_localize(tz="Europe/Berlin")
b


# In[158]:


b.index


# In[159]:


m = s.tz_localize(tz="Asia/Calcutta")
m.index


# In[160]:


m


# **It will first convert individual timezones to UTC and then align datetimes to perform addition/subtraction etc. operations**

# In[161]:


b + m 


# **Date alignment is shown below**

# <img src="alignment.png" />
