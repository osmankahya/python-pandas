
<h1 style="color:blue" align="center">Pandas Time Series Analysis: Period and PeriodIndex</h1>

<h3 style="color:purple">Yearly Period</h3>


```python
import pandas as pd
y = pd.Period('2019')
y
```




    Period('2019', 'A-DEC')




```python
y.start_time
```




    Timestamp('2019-01-01 00:00:00')




```python
y.end_time
```




    Timestamp('2019-12-31 23:59:59.999999999')




```python
y.is_leap_year
```




    True



<h3 style="color:purple">Monthly Period</h3>


```python
m = pd.Period('2017-12')
m
```




    Period('2017-12', 'M')




```python
m.start_time
```




    Timestamp('2017-12-01 00:00:00')




```python
m.end_time
```




    Timestamp('2017-12-31 23:59:59.999999999')




```python
m+1
```




    Period('2018-01', 'M')



<h3 style="color:purple">Daily Period</h3>


```python
d = pd.Period('2016-02-28', freq='D')
d
```




    Period('2016-02-28', 'D')




```python
d.start_time
```




    Timestamp('2016-02-28 00:00:00')




```python
d.end_time
```




    Timestamp('2016-02-28 23:59:59.999999999')




```python
d+1
```




    Period('2016-02-29', 'D')



<h3 style="color:purple">Hourly Period</h3>


```python
h = pd.Period('2017-08-15 23:00:00',freq='H')
h
```




    Period('2017-08-15 23:00', 'H')




```python
h+1
```




    Period('2017-08-16 00:00', 'H')



<h4>Achieve same results using pandas offsets hour</h4>


```python
h+pd.offsets.Hour(1)
```




    Period('2017-08-16 00:00', 'H')



<h3 style="color:purple">Quarterly Period</h3>


```python
q1= pd.Period('2017Q1', freq='Q-JAN')
q1
```




    Period('2017Q1', 'Q-JAN')




```python
q1.start_time
```




    Timestamp('2016-02-01 00:00:00')




```python
q1.end_time
```




    Timestamp('2016-04-30 23:59:59.999999999')



<h4>Use asfreq to convert period to a different frequency</h4>


```python
q1.asfreq('M',how='start')
```




    Period('2016-02', 'M')




```python
q1.asfreq('M',how='end')
```




    Period('2016-04', 'M')



<h3 style="color:purple">Weekly Period</h3>


```python
w = pd.Period('2017-07-05',freq='W')
w
```




    Period('2017-07-03/2017-07-09', 'W-SUN')




```python
w-1
```




    Period('2017-06-26/2017-07-02', 'W-SUN')




```python
w2 = pd.Period('2017-08-15',freq='W')
w2
```




    Period('2017-08-14/2017-08-20', 'W-SUN')




```python
w2-w
```




    6



<h3 style="color:purple">PeriodIndex and period_range</h3>


```python
r = pd.period_range('2011', '2017', freq='q')
r
```




    PeriodIndex(['2011Q1', '2011Q2', '2011Q3', '2011Q4', '2012Q1', '2012Q2',
                 '2012Q3', '2012Q4', '2013Q1', '2013Q2', '2013Q3', '2013Q4',
                 '2014Q1', '2014Q2', '2014Q3', '2014Q4', '2015Q1', '2015Q2',
                 '2015Q3', '2015Q4', '2016Q1', '2016Q2', '2016Q3', '2016Q4',
                 '2017Q1'],
                dtype='period[Q-DEC]', freq='Q-DEC')




```python
r[0].start_time
```




    Timestamp('2011-01-01 00:00:00')




```python
r[0].end_time
```




    Timestamp('2011-03-31 23:59:59.999999999')



**Walmart's fiscal year ends in Jan, below is how you generate walmart's fiscal quarters between 2011 and 2017**


```python
r = pd.period_range('2011', '2017', freq='q-jan')
r
```




    PeriodIndex(['2011Q4', '2012Q1', '2012Q2', '2012Q3', '2012Q4', '2013Q1',
                 '2013Q2', '2013Q3', '2013Q4', '2014Q1', '2014Q2', '2014Q3',
                 '2014Q4', '2015Q1', '2015Q2', '2015Q3', '2015Q4', '2016Q1',
                 '2016Q2', '2016Q3', '2016Q4', '2017Q1', '2017Q2', '2017Q3',
                 '2017Q4'],
                dtype='period[Q-JAN]', freq='Q-JAN')




```python
r[0].start_time
```




    Timestamp('2010-11-01 00:00:00')




```python
r[0].end_time
```




    Timestamp('2011-01-31 23:59:59.999999999')




```python
r = pd.PeriodIndex(start='2016-01', freq='3M', periods=10)
r
```




    PeriodIndex(['2016-01', '2016-04', '2016-07', '2016-10', '2017-01', '2017-04',
                 '2017-07', '2017-10', '2018-01', '2018-04'],
                dtype='period[3M]', freq='3M')




```python
import numpy as np
ps = pd.Series(np.random.randn(len(idx)), idx)
ps
```




    2016-01   -0.895267
    2016-04    1.343498
    2016-07   -0.979625
    2016-10   -0.292720
    2017-01    0.275139
    2017-04    1.200450
    2017-07    1.890607
    2017-10    0.259646
    2018-01   -1.113016
    2018-04    1.669858
    Freq: 3M, dtype: float64



<h4>Partial Indexing</h4>


```python
ps['2016']
```




    2016-01   -0.895267
    2016-04    1.343498
    2016-07   -0.979625
    2016-10   -0.292720
    2017-01    0.275139
    Freq: 3M, dtype: float64




```python
ps['2016':'2017']
```




    2016-01   -0.895267
    2016-04    1.343498
    2016-07   -0.979625
    2016-10   -0.292720
    2017-01    0.275139
    2017-04    1.200450
    2017-07    1.890607
    2017-10    0.259646
    Freq: 3M, dtype: float64



<h4>Converting between representations</h4>


```python
pst = ps.to_timestamp()
pst
```




    2016-01-01   -0.895267
    2016-04-01    1.343498
    2016-07-01   -0.979625
    2016-10-01   -0.292720
    2017-01-01    0.275139
    2017-04-01    1.200450
    2017-07-01    1.890607
    2017-10-01    0.259646
    2018-01-01   -1.113016
    2018-04-01    1.669858
    Freq: QS-OCT, dtype: float64




```python
pst.index
```




    DatetimeIndex(['2016-01-01', '2016-04-01', '2016-07-01', '2016-10-01',
                   '2017-01-01', '2017-04-01', '2017-07-01', '2017-10-01',
                   '2018-01-01', '2018-04-01'],
                  dtype='datetime64[ns]', freq='QS-OCT')




```python
ps = pst.to_period()
ps
```




    2016Q1   -0.895267
    2016Q2    1.343498
    2016Q3   -0.979625
    2016Q4   -0.292720
    2017Q1    0.275139
    2017Q2    1.200450
    2017Q3    1.890607
    2017Q4    0.259646
    2018Q1   -1.113016
    2018Q2    1.669858
    Freq: Q-DEC, dtype: float64




```python
ps.index
```




    PeriodIndex(['2016Q1', '2016Q2', '2016Q3', '2016Q4', '2017Q1', '2017Q2',
                 '2017Q3', '2017Q4', '2018Q1', '2018Q2'],
                dtype='period[Q-DEC]', freq='Q-DEC')



<h3 style="color:purple">Processing Wal Mart's Financials</h3>


```python
import pandas as pd
df = pd.read_csv("wmt.csv")
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
      <th>Line Item</th>
      <th>2017Q1</th>
      <th>2017Q2</th>
      <th>2017Q3</th>
      <th>2017Q4</th>
      <th>2018Q1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Revenue</td>
      <td>115904</td>
      <td>120854</td>
      <td>118179</td>
      <td>130936</td>
      <td>117542</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Expenses</td>
      <td>86544</td>
      <td>89485</td>
      <td>87484</td>
      <td>97743</td>
      <td>87688</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Profit</td>
      <td>29360</td>
      <td>31369</td>
      <td>30695</td>
      <td>33193</td>
      <td>29854</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.set_index("Line Item",inplace=True)
df = df.T
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
      <th>Line Item</th>
      <th>Revenue</th>
      <th>Expenses</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017Q1</th>
      <td>115904</td>
      <td>86544</td>
      <td>29360</td>
    </tr>
    <tr>
      <th>2017Q2</th>
      <td>120854</td>
      <td>89485</td>
      <td>31369</td>
    </tr>
    <tr>
      <th>2017Q3</th>
      <td>118179</td>
      <td>87484</td>
      <td>30695</td>
    </tr>
    <tr>
      <th>2017Q4</th>
      <td>130936</td>
      <td>97743</td>
      <td>33193</td>
    </tr>
    <tr>
      <th>2018Q1</th>
      <td>117542</td>
      <td>87688</td>
      <td>29854</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index = pd.PeriodIndex(df.index, freq="Q-JAN")
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
      <th>Line Item</th>
      <th>Revenue</th>
      <th>Expenses</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017Q1</th>
      <td>115904</td>
      <td>86544</td>
      <td>29360</td>
    </tr>
    <tr>
      <th>2017Q2</th>
      <td>120854</td>
      <td>89485</td>
      <td>31369</td>
    </tr>
    <tr>
      <th>2017Q3</th>
      <td>118179</td>
      <td>87484</td>
      <td>30695</td>
    </tr>
    <tr>
      <th>2017Q4</th>
      <td>130936</td>
      <td>97743</td>
      <td>33193</td>
    </tr>
    <tr>
      <th>2018Q1</th>
      <td>117542</td>
      <td>87688</td>
      <td>29854</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index
```




    PeriodIndex(['2017Q1', '2017Q2', '2017Q3', '2017Q4', '2018Q1'], dtype='period[Q-JAN]', freq='Q-JAN')




```python
df.index[0].start_time
```




    Timestamp('2016-02-01 00:00:00')



<h4 style="color:green">Add start date end date columns to dataframe</h4>


```python
df["Start Date"]=df.index.map(lambda x: x.start_time)
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
      <th>Line Item</th>
      <th>Revenue</th>
      <th>Expenses</th>
      <th>Profit</th>
      <th>Start Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017Q1</th>
      <td>115904</td>
      <td>86544</td>
      <td>29360</td>
      <td>2016-02-01</td>
    </tr>
    <tr>
      <th>2017Q2</th>
      <td>120854</td>
      <td>89485</td>
      <td>31369</td>
      <td>2016-05-01</td>
    </tr>
    <tr>
      <th>2017Q3</th>
      <td>118179</td>
      <td>87484</td>
      <td>30695</td>
      <td>2016-08-01</td>
    </tr>
    <tr>
      <th>2017Q4</th>
      <td>130936</td>
      <td>97743</td>
      <td>33193</td>
      <td>2016-11-01</td>
    </tr>
    <tr>
      <th>2018Q1</th>
      <td>117542</td>
      <td>87688</td>
      <td>29854</td>
      <td>2017-02-01</td>
    </tr>
  </tbody>
</table>
</div>




```python
df["End Date"]=df.index.map(lambda x: x.end_time)
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
      <th>Line Item</th>
      <th>Revenue</th>
      <th>Expenses</th>
      <th>Profit</th>
      <th>Start Date</th>
      <th>End Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017Q1</th>
      <td>115904</td>
      <td>86544</td>
      <td>29360</td>
      <td>2016-02-01</td>
      <td>2016-04-30</td>
    </tr>
    <tr>
      <th>2017Q2</th>
      <td>120854</td>
      <td>89485</td>
      <td>31369</td>
      <td>2016-05-01</td>
      <td>2016-07-31</td>
    </tr>
    <tr>
      <th>2017Q3</th>
      <td>118179</td>
      <td>87484</td>
      <td>30695</td>
      <td>2016-08-01</td>
      <td>2016-10-31</td>
    </tr>
    <tr>
      <th>2017Q4</th>
      <td>130936</td>
      <td>97743</td>
      <td>33193</td>
      <td>2016-11-01</td>
      <td>2017-01-31</td>
    </tr>
    <tr>
      <th>2018Q1</th>
      <td>117542</td>
      <td>87688</td>
      <td>29854</td>
      <td>2017-02-01</td>
      <td>2017-04-30</td>
    </tr>
  </tbody>
</table>
</div>


