#!/usr/bin/env python
# coding: utf-8

# ## <font color="maroon"><h4 align="center">Pandas Group By</font>

# **In this tutorial we are going to look at weather data from various cities and see how group by can be used to run some analytics.** 

# In[1]:


import pandas as pd
df = pd.read_csv("weather_by_cities.csv")
df


# ### For this dataset, get following answers,
# #### 1. What was the maximum temperature in each of these 3 cities?
# #### 2. What was the average windspeed in each of these 3 cities?
# 

# In[2]:


g = df.groupby("city")
g


# **DataFrameGroupBy object looks something like below,**

# <img src="group_by_cities.png">

# In[3]:


for city, data in g:
    print("city:",city)
    print("\n")
    print("data:",data)    


# **This is similar to SQL,**
# 
# **SELECT * from weather_data GROUP BY city**

# In[4]:


g.get_group('mumbai')


# In[5]:


g.max()


# In[6]:


g.mean()


# **This method of splitting your dataset in smaller groups and then applying an operation 
# (such as min or max) to get aggregate result is called Split-Apply-Combine. It is illustrated in a diagram below**

# <img src="split_apply_combine.png">

# In[7]:


g.min()


# In[8]:


g.describe()


# In[9]:


g.size()


# In[10]:


g.count()


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
g.plot()


# <h4>Group data using custom function: Let's say you want to group your data using custom function. Here the requirement is to create three groups<h4>
# <ol>
#     <li>Days when temperature was between 80 and 90</li>
#     <li>Days when it was between 50 and 60</li>
#     <li>Days when it was anything else</li>
# </ol>

# For this you need to write custom grouping function and pass that to groupby

# In[21]:


def grouper(df, idx, col):
    if 80 <= df[col].loc[idx] <= 90:
        return '80-90'
    elif 50 <= df[col].loc[idx] <= 60:
        return '50-60'
    else:
        return 'others'


# In[22]:


g = df.groupby(lambda x: grouper(df, x, 'temperature'))
g


# In[24]:


for key, d in g:
    print("Group by Key: {}\n".format(key))
    print(d)

