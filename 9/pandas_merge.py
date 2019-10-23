#!/usr/bin/env python
# coding: utf-8

# # <font color="purple"><h3 align="center">Pandas Merge Tutorial</h3></font>

# ## <font color='blue'>Basic Merge Using a Dataframe Column</font>

# In[28]:


import pandas as pd
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
df1


# In[29]:


df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
df2


# In[30]:


df3 = pd.merge(df1, df2, on="city")
df3


# ## <font color='blue'>Type Of DataBase Joins</font>

# <img src="db_joins.jpg" height="800", width="800">

# In[31]:


df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35, 38],
})
df1


# In[32]:


df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "humidity": [65,68,71],
})
df2


# In[33]:


df3=pd.merge(df1,df2,on="city",how="inner")
df3


# In[34]:


df3=pd.merge(df1,df2,on="city",how="outer")
df3


# In[35]:


df3=pd.merge(df1,df2,on="city",how="left")
df3


# In[36]:


df3=pd.merge(df1,df2,on="city",how="right")
df3


# ## <font color='blue'>indicator flag</font>

# In[37]:


df3=pd.merge(df1,df2,on="city",how="outer",indicator=True)
df3


# ## <font color='blue'>suffixes</font>

# In[38]:


df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})
df1


# In[39]:


df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})
df2


# In[40]:


df3= pd.merge(df1,df2,on="city",how="outer", suffixes=('_first','_second'))
df3


# ## <font color='blue'>join</font>

# In[58]:


df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
df1.set_index('city',inplace=True)
df1


# In[59]:


df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
df2.set_index('city',inplace=True)
df2


# In[60]:


df1.join(df2,lsuffix='_l', rsuffix='_r')

