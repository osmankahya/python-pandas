#!/usr/bin/env python
# coding: utf-8

# # <font color="purple"><h3 align="center">Dataframe and mysql database tutorial</h3></font>

# In[1]:


import pandas as pd
import sqlalchemy


# In[8]:


engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/application')


# Format of connection string is:
# 
# mysql+pymysql://username:password@host:port/database_name
# 
# Format of connection string for other databases
# 
# https://pandas.pydata.org/pandas-docs/stable/io.html#engine-connection-examples

# <img src="conn_string_format.JPG"/>

# <h3 style="color:purple">Read entire table in a dataframe using <span style="color:blue">read_sql_table</span></h3>

# In[9]:


df = pd.read_sql_table('customers',engine)
df


# **Read only selected columns**

# In[24]:


df = pd.read_sql_table('customers', engine, columns=["name"])
df


# <h3 style="color:purple">Join two tables and read them in a dataframe using <span style="color:blue">read_sql_query</span></h3>

# In[15]:


df = pd.read_sql_query("select id,name from customers",engine)
df


# In[18]:


query = '''
 SELECT customers.name, customers.phone_number, orders.name, orders.amount
 FROM customers INNER JOIN orders
 ON customers.id=orders.customer_id
'''
df = pd.read_sql_query(query,engine)
df


# <h3 style="color:purple"><span style="color:blue">read_sql</span> is a wrapper around read_sql_query and read_sql_table</h3>

# In[25]:


query = '''
 SELECT customers.name, customers.phone_number, orders.name, orders.amount
 FROM customers INNER JOIN orders
 ON customers.id=orders.customer_id
'''
pd.read_sql(query,engine)


# In[26]:


pd.read_sql("customers",engine)


# <h3 style="color:purple">Write to mysql database using <span style="color:blue">to_sql</span></h3>

# In[20]:


df = pd.read_csv("customers.csv")
df


# In[21]:


df.rename(columns={
    'Customer Name': 'name',
    'Customer Phone': 'phone_number'
}, inplace=True)
df


# In[22]:


df.to_sql(
    name='customers', # database table name
    con=engine,
    if_exists='append',
    index=False
)


# **to_sql has different parameters such as chunksize which allows to write data in chunks. This is useful when 
# size of dataframe is huge**
