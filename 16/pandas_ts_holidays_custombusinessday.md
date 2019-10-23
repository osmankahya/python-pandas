
<h1 style="color:blue" align="center">Pandas Time Series Analysis Tutorial: Handling Holidays</h1>


```python
import pandas as pd
df = pd.read_csv("aapl_no_dates.csv")
df.head()
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
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>144.88</td>
      <td>145.30</td>
      <td>143.10</td>
      <td>143.50</td>
      <td>14277848</td>
    </tr>
    <tr>
      <th>1</th>
      <td>143.69</td>
      <td>144.79</td>
      <td>142.72</td>
      <td>144.09</td>
      <td>21569557</td>
    </tr>
    <tr>
      <th>2</th>
      <td>143.02</td>
      <td>143.50</td>
      <td>142.41</td>
      <td>142.73</td>
      <td>24128782</td>
    </tr>
    <tr>
      <th>3</th>
      <td>142.90</td>
      <td>144.75</td>
      <td>142.90</td>
      <td>144.18</td>
      <td>19201712</td>
    </tr>
    <tr>
      <th>4</th>
      <td>144.11</td>
      <td>145.95</td>
      <td>143.37</td>
      <td>145.06</td>
      <td>21090636</td>
    </tr>
  </tbody>
</table>
</div>




```python
rng = pd.date_range(start="7/1/2017", end="7/21/2017", freq='B')
rng
```




    DatetimeIndex(['2017-07-03', '2017-07-04', '2017-07-05', '2017-07-06',
                   '2017-07-07', '2017-07-10', '2017-07-11', '2017-07-12',
                   '2017-07-13', '2017-07-14', '2017-07-17', '2017-07-18',
                   '2017-07-19', '2017-07-20', '2017-07-21'],
                  dtype='datetime64[ns]', freq='B')



**Using 'B' frequency is not going to help because 4th July was holiday and 'B' is not taking that into account. 
It only accounts for weekends**

<h3 style="color:purple">Using CustomBusinessDay to generate US holidays calendar frequency</h3>


```python
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

us_cal = CustomBusinessDay(calendar=USFederalHolidayCalendar())

rng = pd.date_range(start="7/1/2017",end="7/23/2017", freq=us_cal)
rng
```




    DatetimeIndex(['2017-07-03', '2017-07-05', '2017-07-06', '2017-07-07',
                   '2017-07-10', '2017-07-11', '2017-07-12', '2017-07-13',
                   '2017-07-14', '2017-07-17', '2017-07-18', '2017-07-19',
                   '2017-07-20', '2017-07-21'],
                  dtype='datetime64[ns]', freq='C')




```python
df.set_index(rng,inplace=True)
df.head()
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
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-07-03</th>
      <td>144.88</td>
      <td>145.30</td>
      <td>143.10</td>
      <td>143.50</td>
      <td>14277848</td>
    </tr>
    <tr>
      <th>2017-07-05</th>
      <td>143.69</td>
      <td>144.79</td>
      <td>142.72</td>
      <td>144.09</td>
      <td>21569557</td>
    </tr>
    <tr>
      <th>2017-07-06</th>
      <td>143.02</td>
      <td>143.50</td>
      <td>142.41</td>
      <td>142.73</td>
      <td>24128782</td>
    </tr>
    <tr>
      <th>2017-07-07</th>
      <td>142.90</td>
      <td>144.75</td>
      <td>142.90</td>
      <td>144.18</td>
      <td>19201712</td>
    </tr>
    <tr>
      <th>2017-07-10</th>
      <td>144.11</td>
      <td>145.95</td>
      <td>143.37</td>
      <td>145.06</td>
      <td>21090636</td>
    </tr>
  </tbody>
</table>
</div>



**You can define your own calendar using AbstractHolidayCalendar as shown below. USFederalHolidayCalendar is the only calendar available in pandas library and it serves as an example for those who want to write their own custom calendars. Here is the link for USFederalHolidayCalendar implementation** https://github.com/pandas-dev/pandas/blob/master/pandas/tseries/holiday.py

<h3 style="color:purple">AbstractHolidayCalendar</h3>


```python
from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday
class myCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('My Birth Day', month=4, day=15),#, observance=nearest_workday),
    ]
    
my_bday = CustomBusinessDay(calendar=myCalendar())
pd.date_range('4/1/2017','4/30/2017',freq=my_bday)
```




    DatetimeIndex(['2017-04-03', '2017-04-04', '2017-04-05', '2017-04-06',
                   '2017-04-07', '2017-04-10', '2017-04-11', '2017-04-12',
                   '2017-04-13', '2017-04-14', '2017-04-17', '2017-04-18',
                   '2017-04-19', '2017-04-20', '2017-04-21', '2017-04-24',
                   '2017-04-25', '2017-04-26', '2017-04-27', '2017-04-28'],
                  dtype='datetime64[ns]', freq='C')



<h3 style="color:purple">CustomBusinessDay</h3>

**Weekend in egypt is Friday and Saturday. Sunday is just a normal weekday and you can handle this custom week schedule using
CystomBysinessDay with weekmask as shown below**


```python
egypt_weekdays = "Sun Mon Tue Wed Thu"

b = CustomBusinessDay(weekmask=egypt_weekdays)

pd.date_range(start="7/1/2017",periods=20,freq=b)
```




    DatetimeIndex(['2017-07-02', '2017-07-03', '2017-07-04', '2017-07-05',
                   '2017-07-06', '2017-07-09', '2017-07-10', '2017-07-11',
                   '2017-07-12', '2017-07-13', '2017-07-16', '2017-07-17',
                   '2017-07-18', '2017-07-19', '2017-07-20', '2017-07-23',
                   '2017-07-24', '2017-07-25', '2017-07-26', '2017-07-27'],
                  dtype='datetime64[ns]', freq='C')



**You can also add holidays to this custom business day frequency**


```python
b = CustomBusinessDay(holidays=['2017-07-04', '2017-07-10'], weekmask=egypt_weekdays)

pd.date_range(start="7/1/2017",periods=20,freq=b)
```




    DatetimeIndex(['2017-07-02', '2017-07-03', '2017-07-05', '2017-07-06',
                   '2017-07-09', '2017-07-11', '2017-07-12', '2017-07-13',
                   '2017-07-16', '2017-07-17', '2017-07-18', '2017-07-19',
                   '2017-07-20', '2017-07-23', '2017-07-24', '2017-07-25',
                   '2017-07-26', '2017-07-27', '2017-07-30', '2017-07-31'],
                  dtype='datetime64[ns]', freq='C')



**Mathematical operations on date object using custom business day**


```python
from datetime import datetime
dt = datetime(2017,7,9)
dt
```




    datetime.datetime(2017, 7, 9, 0, 0)




```python
dt + 1*b
```




    Timestamp('2017-07-11 00:00:00')


