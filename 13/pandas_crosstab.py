#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue" align="center">Crosstab Tutorial</h1>

# In[16]:


import pandas as pd
df = pd.read_excel("survey.xls")
df


# In[17]:


pd.crosstab(df.Nationality,df.Handedness)


# In[18]:


pd.crosstab(df.Sex,df.Handedness)


# <h2 style="color:purple">Margins</h2>

# In[19]:


pd.crosstab(df.Sex,df.Handedness, margins=True)


# <h2 style="color:purple">Multi Index Column and Rows</h2>

# In[20]:


pd.crosstab(df.Sex, [df.Handedness,df.Nationality], margins=True)


# In[21]:


pd.crosstab([df.Nationality, df.Sex], [df.Handedness], margins=True)


# <h2 style="color:purple">Normalize</h2>

# In[22]:


pd.crosstab(df.Sex, df.Handedness, normalize='index')


# <h2 style="color:purple">Aggfunc and Values</h2>

# In[23]:


import numpy as np
pd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.average)

