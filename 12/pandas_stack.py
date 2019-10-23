#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue">Reshape dataframe using stack/unstack</h1>

# In[81]:


import pandas as pd
df = pd.read_excel("stocks.xlsx",header=[0,1])
df


# In[89]:


df.stack()


# In[90]:


df.stack(level=0)


# In[92]:


df_stacked=df.stack()
df_stacked


# In[93]:


df_stacked.unstack()


# <h1 style="color:blue">3 levels of column headers</h1>

# In[95]:


df2 = pd.read_excel("stocks_3_levels.xlsx",header=[0,1,2])
df2


# In[96]:


df2.stack()


# In[104]:


df2.stack(level=0)


# In[105]:


df2.stack(level=1)

