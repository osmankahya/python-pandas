#!/usr/bin/env python
# coding: utf-8

# # <font color="purple"><h3 align="center">DataFrame Basics Tutorial</h3></font>

# ## **Dataframe is most commonly used object in pandas. It is a table like datastructure containing rows and columns similar to excel spreadsheet**

# In[5]:


import pandas as pd
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)
df = pd.read_csv("weather_data.csv")
df


# In[6]:


df.shape # rows, columns = df.shape


# ## <font color='blue'>Rows</font>

# In[5]:


df.head() # df.head(3)


# In[6]:


df.tail() # df.tail(2)


# In[7]:


df[1:3]


# ## <font color='blue'>Columns</font>

# In[8]:


df.columns


# In[9]:


df['day'] # or df.day


# In[10]:


type(df['day'])


# In[2]:


df[['day','temperature']]


# ## <font color='blue'>Operations On DataFrame</font>

# In[ ]:





# In[12]:


df['temperature'].max()


# In[13]:


df[df['temperature']>32]


# In[14]:


df['day'][df['temperature'] == df['temperature'].max()] # Kinda doing SQL in pandas


# In[15]:


df[df['temperature'] == df['temperature'].max()] # Kinda doing SQL in pandas


# In[16]:


df['temperature'].std()


# In[17]:


df['event'].max() # But mean() won't work since data type is string


# In[18]:


df.describe()


# **Google pandas series operations to find out list of all operations**
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html

# ## <font color='blue'>set_index</font>

# In[19]:


df.set_index('day')


# In[20]:


df.set_index('day', inplace=True)


# In[21]:


df


# In[22]:


df.index


# In[23]:


df.loc['1/2/2017']


# In[24]:


df.reset_index(inplace=True)
df.head()


# In[25]:


df.set_index('event',inplace=True) # this is kind of building a hash map using event as a key
df


# In[26]:


df.loc['Snow']

