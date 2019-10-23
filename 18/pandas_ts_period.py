#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue" align="center">Pandas Time Series Analysis: Period and PeriodIndex</h1>

# <h3 style="color:purple">Yearly Period</h3>

# In[4]:


import pandas as pd
y = pd.Period('2019')
y


# In[5]:


y.start_time


# In[6]:


y.end_time


# In[73]:


y.is_leap_year


# <h3 style="color:purple">Monthly Period</h3>

# In[64]:


m = pd.Period('2017-12')
m


# In[2]:


m.start_time


# In[3]:


m.end_time


# In[4]:


m+1


# <h3 style="color:purple">Daily Period</h3>

# In[66]:


d = pd.Period('2016-02-28', freq='D')
d


# In[67]:


d.start_time


# In[68]:


d.end_time


# In[69]:


d+1


# <h3 style="color:purple">Hourly Period</h3>

# In[9]:


h = pd.Period('2017-08-15 23:00:00',freq='H')
h


# In[10]:


h+1


# <h4>Achieve same results using pandas offsets hour</h4>

# In[34]:


h+pd.offsets.Hour(1)


# <h3 style="color:purple">Quarterly Period</h3>

# In[11]:


q1= pd.Period('2017Q1', freq='Q-JAN')
q1


# In[12]:


q1.start_time


# In[13]:


q1.end_time


# <h4>Use asfreq to convert period to a different frequency</h4>

# In[46]:


q1.asfreq('M',how='start')


# In[47]:


q1.asfreq('M',how='end')


# <h3 style="color:purple">Weekly Period</h3>

# In[14]:


w = pd.Period('2017-07-05',freq='W')
w


# In[15]:


w-1


# In[16]:


w2 = pd.Period('2017-08-15',freq='W')
w2


# In[17]:


w2-w


# <h3 style="color:purple">PeriodIndex and period_range</h3>

# In[58]:


r = pd.period_range('2011', '2017', freq='q')
r


# In[59]:


r[0].start_time


# In[60]:


r[0].end_time


# **Walmart's fiscal year ends in Jan, below is how you generate walmart's fiscal quarters between 2011 and 2017**

# In[57]:


r = pd.period_range('2011', '2017', freq='q-jan')
r


# In[20]:


r[0].start_time


# In[21]:


r[0].end_time


# In[42]:


r = pd.PeriodIndex(start='2016-01', freq='3M', periods=10)
r


# In[43]:


import numpy as np
ps = pd.Series(np.random.randn(len(idx)), idx)
ps


# <h4>Partial Indexing</h4>

# In[44]:


ps['2016']


# In[45]:


ps['2016':'2017']


# <h4>Converting between representations</h4>

# In[50]:


pst = ps.to_timestamp()
pst


# In[51]:


pst.index


# In[54]:


ps = pst.to_period()
ps


# In[55]:


ps.index


# <h3 style="color:purple">Processing Wal Mart's Financials</h3>

# In[74]:


import pandas as pd
df = pd.read_csv("wmt.csv")
df


# In[25]:


df.set_index("Line Item",inplace=True)
df = df.T
df


# In[26]:


df.index = pd.PeriodIndex(df.index, freq="Q-JAN")
df


# In[27]:


df.index


# In[28]:


df.index[0].start_time


# <h4 style="color:green">Add start date end date columns to dataframe</h4>

# In[29]:


df["Start Date"]=df.index.map(lambda x: x.start_time)
df


# In[30]:


df["End Date"]=df.index.map(lambda x: x.end_time)
df

