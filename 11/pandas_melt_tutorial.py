#!/usr/bin/env python
# coding: utf-8

# # <font color="purple"><h3 align="center">Reshape pandas dataframe using melt</h3></font>

# In[2]:


import pandas as pd
df = pd.read_csv("weather.csv")
df


# In[3]:


melted = pd.melt(df, id_vars=["day"], var_name='city', value_name='temperature')
melted

