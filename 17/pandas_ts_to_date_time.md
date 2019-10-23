
<h1 style="color:blue" align="center">Pandas Time Series Analysis Tutorial: to_datetime</h1>


```python
import pandas as pd
dates = ['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05','20170105']
pd.to_datetime(dates)
```




    DatetimeIndex(['2017-01-05', '2017-01-05', '2017-01-05', '2017-01-05',
                   '2017-01-05', '2017-01-05'],
                  dtype='datetime64[ns]', freq=None)




```python
dt = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05','20170105']
pd.to_datetime(dt)
```




    DatetimeIndex(['2017-01-05 14:30:00', '2017-01-05 14:30:00',
                   '2016-01-05 00:00:00', '2017-01-05 00:00:00',
                   '2017-01-05 00:00:00', '2017-01-05 00:00:00'],
                  dtype='datetime64[ns]', freq=None)



<h3 style="color:purple">European style dates with day first</h3>


```python
pd.to_datetime('30-12-2016')
```




    Timestamp('2016-12-30 00:00:00')




```python
pd.to_datetime('5-1-2016', dayfirst=True)
```




    Timestamp('2016-01-05 00:00:00')



<h3 style="color:purple">Custom date time format</h3>


```python
pd.to_datetime('2017$01$05', format='%Y$%m$%d')
```




    Timestamp('2017-01-05 00:00:00')




```python
pd.to_datetime('2017#01#05', format='%Y#%m#%d')
```




    Timestamp('2017-01-05 00:00:00')



<h3 style="color:purple">Handling invalid dates</h3>


```python
pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='ignore')
```




    array(['2017-01-05', 'Jan 6, 2017', 'abc'], dtype=object)




```python
pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='coerce')
```




    DatetimeIndex(['2017-01-05', '2017-01-06', 'NaT'], dtype='datetime64[ns]', freq=None)



<h3 style="color:purple">Epoch</h3>

**Epoch or Unix time means number of seconds that have passed since Jan 1, 1970 00:00:00 UTC time**


```python
current_epoch = 1501324478
pd.to_datetime(current_epoch, unit='s')
```




    Timestamp('2017-07-29 10:34:38')




```python
pd.to_datetime(current_epoch*1000, unit='ms')
```




    Timestamp('2017-07-29 10:34:38')




```python
t = pd.to_datetime([current_epoch], unit='s')
t
```




    DatetimeIndex(['2017-07-29 10:34:38'], dtype='datetime64[ns]', freq=None)




```python
t.view('int64')
```




    array([1501324478000000000], dtype=int64)


