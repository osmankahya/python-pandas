

```python
import pandas as pd
df = pd.read_csv("fb.csv",parse_dates=['Date'],index_col='Date')
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
      <th>Price</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-15</th>
      <td>171.00</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>170.00</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>166.91</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>167.41</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>167.78</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>169.64</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>168.71</td>
    </tr>
    <tr>
      <th>2017-08-24</th>
      <td>167.74</td>
    </tr>
    <tr>
      <th>2017-08-25</th>
      <td>166.32</td>
    </tr>
    <tr>
      <th>2017-08-28</th>
      <td>167.24</td>
    </tr>
  </tbody>
</table>
</div>



<img src="shift_image.png" />

<h2 style="color:purple">Shift</h2>


```python
df.shift(1)
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
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-15</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>171.00</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>170.00</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>166.91</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>167.41</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>167.78</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>169.64</td>
    </tr>
    <tr>
      <th>2017-08-24</th>
      <td>168.71</td>
    </tr>
    <tr>
      <th>2017-08-25</th>
      <td>167.74</td>
    </tr>
    <tr>
      <th>2017-08-28</th>
      <td>166.32</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shift(-1)
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
      <th>Price</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-15</th>
      <td>170.00</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>166.91</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>167.41</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>167.78</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>169.64</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>168.71</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>167.74</td>
    </tr>
    <tr>
      <th>2017-08-24</th>
      <td>166.32</td>
    </tr>
    <tr>
      <th>2017-08-25</th>
      <td>167.24</td>
    </tr>
    <tr>
      <th>2017-08-28</th>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Prev Day Price'] = df['Price'].shift(1)
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
      <th>Price</th>
      <th>Prev Day Price</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-15</th>
      <td>171.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>170.00</td>
      <td>171.00</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>166.91</td>
      <td>170.00</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>167.41</td>
      <td>166.91</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>167.78</td>
      <td>167.41</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>169.64</td>
      <td>167.78</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>168.71</td>
      <td>169.64</td>
    </tr>
    <tr>
      <th>2017-08-24</th>
      <td>167.74</td>
      <td>168.71</td>
    </tr>
    <tr>
      <th>2017-08-25</th>
      <td>166.32</td>
      <td>167.74</td>
    </tr>
    <tr>
      <th>2017-08-28</th>
      <td>167.24</td>
      <td>166.32</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Price Change'] = df['Price'] - df['Prev Day Price']
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
      <th>Price</th>
      <th>Prev Day Price</th>
      <th>Price Change</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-15</th>
      <td>171.00</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>170.00</td>
      <td>171.00</td>
      <td>-1.00</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>166.91</td>
      <td>170.00</td>
      <td>-3.09</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>167.41</td>
      <td>166.91</td>
      <td>0.50</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>167.78</td>
      <td>167.41</td>
      <td>0.37</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>169.64</td>
      <td>167.78</td>
      <td>1.86</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>168.71</td>
      <td>169.64</td>
      <td>-0.93</td>
    </tr>
    <tr>
      <th>2017-08-24</th>
      <td>167.74</td>
      <td>168.71</td>
      <td>-0.97</td>
    </tr>
    <tr>
      <th>2017-08-25</th>
      <td>166.32</td>
      <td>167.74</td>
      <td>-1.42</td>
    </tr>
    <tr>
      <th>2017-08-28</th>
      <td>167.24</td>
      <td>166.32</td>
      <td>0.92</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['5 day return'] =  (df['Price'] - df['Price'].shift(5))*100/df['Price'].shift(5)
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
      <th>Price</th>
      <th>Prev Day Price</th>
      <th>Price Change</th>
      <th>5 day return</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-15</th>
      <td>171.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>170.00</td>
      <td>171.00</td>
      <td>-1.00</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>166.91</td>
      <td>170.00</td>
      <td>-3.09</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>167.41</td>
      <td>166.91</td>
      <td>0.50</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>167.78</td>
      <td>167.41</td>
      <td>0.37</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>169.64</td>
      <td>167.78</td>
      <td>1.86</td>
      <td>-0.795322</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>168.71</td>
      <td>169.64</td>
      <td>-0.93</td>
      <td>-0.758824</td>
    </tr>
    <tr>
      <th>2017-08-24</th>
      <td>167.74</td>
      <td>168.71</td>
      <td>-0.97</td>
      <td>0.497274</td>
    </tr>
    <tr>
      <th>2017-08-25</th>
      <td>166.32</td>
      <td>167.74</td>
      <td>-1.42</td>
      <td>-0.651096</td>
    </tr>
    <tr>
      <th>2017-08-28</th>
      <td>167.24</td>
      <td>166.32</td>
      <td>0.92</td>
      <td>-0.321850</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = df[['Price']]
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
      <th>Price</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-15</th>
      <td>171.00</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>170.00</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>166.91</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>167.41</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>167.78</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>169.64</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>168.71</td>
    </tr>
    <tr>
      <th>2017-08-24</th>
      <td>167.74</td>
    </tr>
    <tr>
      <th>2017-08-25</th>
      <td>166.32</td>
    </tr>
    <tr>
      <th>2017-08-28</th>
      <td>167.24</td>
    </tr>
  </tbody>
</table>
</div>



<h2 style="color:purple">tshift</h2>


```python
df.index
```




    DatetimeIndex(['2017-08-15', '2017-08-16', '2017-08-17', '2017-08-18',
                   '2017-08-21', '2017-08-22', '2017-08-23', '2017-08-24',
                   '2017-08-25', '2017-08-28'],
                  dtype='datetime64[ns]', name='Date', freq=None)




```python
df.index = pd.date_range(start='2017-08-15',periods=10, freq='B')
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
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-15</th>
      <td>171.00</td>
    </tr>
    <tr>
      <th>2017-08-16</th>
      <td>170.00</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>166.91</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>167.41</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>167.78</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>169.64</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>168.71</td>
    </tr>
    <tr>
      <th>2017-08-24</th>
      <td>167.74</td>
    </tr>
    <tr>
      <th>2017-08-25</th>
      <td>166.32</td>
    </tr>
    <tr>
      <th>2017-08-28</th>
      <td>167.24</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index
```




    DatetimeIndex(['2017-08-15', '2017-08-16', '2017-08-17', '2017-08-18',
                   '2017-08-21', '2017-08-22', '2017-08-23', '2017-08-24',
                   '2017-08-25', '2017-08-28'],
                  dtype='datetime64[ns]', freq='B')




```python
df.tshift(1)
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
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-16</th>
      <td>171.00</td>
    </tr>
    <tr>
      <th>2017-08-17</th>
      <td>170.00</td>
    </tr>
    <tr>
      <th>2017-08-18</th>
      <td>166.91</td>
    </tr>
    <tr>
      <th>2017-08-21</th>
      <td>167.41</td>
    </tr>
    <tr>
      <th>2017-08-22</th>
      <td>167.78</td>
    </tr>
    <tr>
      <th>2017-08-23</th>
      <td>169.64</td>
    </tr>
    <tr>
      <th>2017-08-24</th>
      <td>168.71</td>
    </tr>
    <tr>
      <th>2017-08-25</th>
      <td>167.74</td>
    </tr>
    <tr>
      <th>2017-08-28</th>
      <td>166.32</td>
    </tr>
    <tr>
      <th>2017-08-29</th>
      <td>167.24</td>
    </tr>
  </tbody>
</table>
</div>


