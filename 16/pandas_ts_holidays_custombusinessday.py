#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:blue" align="center">Pandas Time Series Analysis Tutorial: Handling Holidays</h1>

# In[45]:


import pandas as pd
df = pd.read_csv("aapl_no_dates.csv")
df.head()


# In[46]:


rng = pd.date_range(start="7/1/2017", end="7/21/2017", freq='B')
rng


# **Using 'B' frequency is not going to help because 4th July was holiday and 'B' is not taking that into account. 
# It only accounts for weekends**

# <h3 style="color:purple">Using CustomBusinessDay to generate US holidays calendar frequency</h3>

# In[38]:


from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

us_cal = CustomBusinessDay(calendar=USFederalHolidayCalendar())

rng = pd.date_range(start="7/1/2017",end="7/23/2017", freq=us_cal)
rng


# In[39]:


df.set_index(rng,inplace=True)
df.head()


# **You can define your own calendar using AbstractHolidayCalendar as shown below. USFederalHolidayCalendar is the only calendar available in pandas library and it serves as an example for those who want to write their own custom calendars. Here is the link for USFederalHolidayCalendar implementation** https://github.com/pandas-dev/pandas/blob/master/pandas/tseries/holiday.py

# <h3 style="color:purple">AbstractHolidayCalendar</h3>

# In[48]:


from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday
class myCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('My Birth Day', month=4, day=15),#, observance=nearest_workday),
    ]
    
my_bday = CustomBusinessDay(calendar=myCalendar())
pd.date_range('4/1/2017','4/30/2017',freq=my_bday)


# <h3 style="color:purple">CustomBusinessDay</h3>

# **Weekend in egypt is Friday and Saturday. Sunday is just a normal weekday and you can handle this custom week schedule using
# CystomBysinessDay with weekmask as shown below**

# In[41]:


egypt_weekdays = "Sun Mon Tue Wed Thu"

b = CustomBusinessDay(weekmask=egypt_weekdays)

pd.date_range(start="7/1/2017",periods=20,freq=b)


# **You can also add holidays to this custom business day frequency**

# In[42]:


b = CustomBusinessDay(holidays=['2017-07-04', '2017-07-10'], weekmask=egypt_weekdays)

pd.date_range(start="7/1/2017",periods=20,freq=b)


# **Mathematical operations on date object using custom business day**

# In[43]:


from datetime import datetime
dt = datetime(2017,7,9)
dt


# In[44]:


dt + 1*b

