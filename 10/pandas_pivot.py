#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue">Pivot basics</h1>

# In[38]:


import pandas as pd
import numpy as np
df = pd.read_csv("weather.csv")
df


# In[39]:


df.pivot(index='city',columns='date')


# In[40]:


df.pivot(index='city',columns='date',values="humidity")


# In[41]:


df.pivot(index='date',columns='city')


# In[42]:


df.pivot(index='humidity',columns='city')


# <h1 style="color:blue">Pivot Table</h1>

# In[49]:


df = pd.read_csv("weather2.csv")
df


# In[51]:


df.pivot_table(index="city",columns="date")


# <h2 style="color:brown">Margins</h2>

# In[45]:


df.pivot_table(index="city",columns="date", margins=True,aggfunc=np.sum)


# <h2 style="color:brown">Grouper</h2>

# In[46]:


df = pd.read_csv("weather3.csv")
df


# In[47]:


df['date'] = pd.to_datetime(df['date'])


# In[48]:


df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')

