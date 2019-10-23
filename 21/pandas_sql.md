
# <font color="purple"><h3 align="center">Dataframe and mysql database tutorial</h3></font>


```python
import pandas as pd
import sqlalchemy
```


```python
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/application')
```

Format of connection string is:

mysql+pymysql://username:password@host:port/database_name

Format of connection string for other databases

https://pandas.pydata.org/pandas-docs/stable/io.html#engine-connection-examples

<img src="conn_string_format.JPG"/>

<h3 style="color:purple">Read entire table in a dataframe using <span style="color:blue">read_sql_table</span></h3>


```python
df = pd.read_sql_table('customers',engine)
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>phone_number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Donald</td>
      <td>7326784567</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bill</td>
      <td>6573489999</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Modi</td>
      <td>4567895646</td>
    </tr>
  </tbody>
</table>
</div>



**Read only selected columns**


```python
df = pd.read_sql_table('customers', engine, columns=["name"])
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Donald</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bill</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Modi</td>
    </tr>
  </tbody>
</table>
</div>



<h3 style="color:purple">Join two tables and read them in a dataframe using <span style="color:blue">read_sql_query</span></h3>


```python
df = pd.read_sql_query("select id,name from customers",engine)
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Donald</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bill</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Modi</td>
    </tr>
  </tbody>
</table>
</div>




```python
query = '''
 SELECT customers.name, customers.phone_number, orders.name, orders.amount
 FROM customers INNER JOIN orders
 ON customers.id=orders.customer_id
'''
df = pd.read_sql_query(query,engine)
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>phone_number</th>
      <th>name</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Donald</td>
      <td>7326784567</td>
      <td>Google Pixel</td>
      <td>950.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bill</td>
      <td>6573489999</td>
      <td>Yoga Mat</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Modi</td>
      <td>4567895646</td>
      <td>Fossil Watch</td>
      <td>120.0</td>
    </tr>
  </tbody>
</table>
</div>



<h3 style="color:purple"><span style="color:blue">read_sql</span> is a wrapper around read_sql_query and read_sql_table</h3>


```python
query = '''
 SELECT customers.name, customers.phone_number, orders.name, orders.amount
 FROM customers INNER JOIN orders
 ON customers.id=orders.customer_id
'''
pd.read_sql(query,engine)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>phone_number</th>
      <th>name</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bill</td>
      <td>6573489999</td>
      <td>Yoga Mat</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Donald</td>
      <td>7326784567</td>
      <td>Google Pixel</td>
      <td>950.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Modi</td>
      <td>4567895646</td>
      <td>Fossil Watch</td>
      <td>120.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_sql("customers",engine)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>phone_number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Donald</td>
      <td>7326784567</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bill</td>
      <td>6573489999</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Modi</td>
      <td>4567895646</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10</td>
      <td>rafael nadal</td>
      <td>4567895647</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11</td>
      <td>maria sharapova</td>
      <td>434534545</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12</td>
      <td>vladimir putin</td>
      <td>89345345</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13</td>
      <td>kim un jong</td>
      <td>123434456</td>
    </tr>
    <tr>
      <th>7</th>
      <td>14</td>
      <td>jeff bezos</td>
      <td>934534543</td>
    </tr>
    <tr>
      <th>8</th>
      <td>15</td>
      <td>rahul gandhi</td>
      <td>44324222</td>
    </tr>
  </tbody>
</table>
</div>



<h3 style="color:purple">Write to mysql database using <span style="color:blue">to_sql</span></h3>


```python
df = pd.read_csv("customers.csv")
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Customer Name</th>
      <th>Customer Phone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>rafael nadal</td>
      <td>4567895647</td>
    </tr>
    <tr>
      <th>1</th>
      <td>maria sharapova</td>
      <td>434534545</td>
    </tr>
    <tr>
      <th>2</th>
      <td>vladimir putin</td>
      <td>89345345</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kim un jong</td>
      <td>123434456</td>
    </tr>
    <tr>
      <th>4</th>
      <td>jeff bezos</td>
      <td>934534543</td>
    </tr>
    <tr>
      <th>5</th>
      <td>rahul gandhi</td>
      <td>44324222</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.rename(columns={
    'Customer Name': 'name',
    'Customer Phone': 'phone_number'
}, inplace=True)
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>phone_number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>rafael nadal</td>
      <td>4567895647</td>
    </tr>
    <tr>
      <th>1</th>
      <td>maria sharapova</td>
      <td>434534545</td>
    </tr>
    <tr>
      <th>2</th>
      <td>vladimir putin</td>
      <td>89345345</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kim un jong</td>
      <td>123434456</td>
    </tr>
    <tr>
      <th>4</th>
      <td>jeff bezos</td>
      <td>934534543</td>
    </tr>
    <tr>
      <th>5</th>
      <td>rahul gandhi</td>
      <td>44324222</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_sql(
    name='customers', # database table name
    con=engine,
    if_exists='append',
    index=False
)
```

**to_sql has different parameters such as chunksize which allows to write data in chunks. This is useful when 
size of dataframe is huge**
