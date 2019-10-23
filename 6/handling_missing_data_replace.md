
## <font color="maroon"><h4 align="center">Handling Missing Data - replace method</font>


```python
import pandas as pd
import numpy as np
df = pd.read_csv("weather_data.csv")
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32</td>
      <td>6</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>-99999</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28</td>
      <td>-99999</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>-99999</td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2017</td>
      <td>32</td>
      <td>-99999</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2017</td>
      <td>31</td>
      <td>2</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/6/2017</td>
      <td>34</td>
      <td>5</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



**Replacing single value**


```python
new_df = df.replace(-99999, value=np.NaN)
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2017</td>
      <td>31.0</td>
      <td>2.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/6/2017</td>
      <td>34.0</td>
      <td>5.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



**Replacing list with single value**


```python
new_df = df.replace(to_replace=[-99999,-88888], value=0)
new_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
    <tr>
      <th>day</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-01</th>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>0.0</td>
      <td>7.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>28.0</td>
      <td>0.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>2017-01-06</th>
      <td>0.0</td>
      <td>7.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2017-01-07</th>
      <td>32.0</td>
      <td>0.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>2017-01-08</th>
      <td>31.0</td>
      <td>2.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2017-01-09</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2017-01-10</th>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>2017-01-11</th>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



**Replacing per column**


```python
new_df = df.replace({
        'temperature': -99999,
        'windspeed': -99999,
        'event': '0'
    }, np.nan)
new_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2017</td>
      <td>31.0</td>
      <td>2.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/6/2017</td>
      <td>34.0</td>
      <td>5.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



**Replacing by using mapping**


```python
new_df = df.replace({
        -99999: np.nan,
        'no event': 'Sunny',
    })
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2017</td>
      <td>31.0</td>
      <td>2.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/6/2017</td>
      <td>34.0</td>
      <td>5.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



**Regex**


```python
# when windspeed is 6 mph, 7 mph etc. & temperature is 32 F, 28 F etc.
new_df = df.replace({'temperature': '[A-Za-z]', 'windspeed': '[a-z]'},'', regex=True) 
new_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>day</th>
      <th>temperature</th>
      <th>windspeed</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>32</td>
      <td>6</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2017</td>
      <td>-99999</td>
      <td>7</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2017</td>
      <td>28</td>
      <td>-99999</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2017</td>
      <td>-99999</td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2017</td>
      <td>32</td>
      <td>-99999</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2017</td>
      <td>31</td>
      <td>2</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/6/2017</td>
      <td>34</td>
      <td>5</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



**Replacing list with another list**


```python
df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
      <th>student</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>exceptional</td>
      <td>rob</td>
    </tr>
    <tr>
      <th>1</th>
      <td>average</td>
      <td>maya</td>
    </tr>
    <tr>
      <th>2</th>
      <td>good</td>
      <td>parthiv</td>
    </tr>
    <tr>
      <th>3</th>
      <td>poor</td>
      <td>tom</td>
    </tr>
    <tr>
      <th>4</th>
      <td>average</td>
      <td>julian</td>
    </tr>
    <tr>
      <th>5</th>
      <td>exceptional</td>
      <td>erica</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>score</th>
      <th>student</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>rob</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>maya</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>parthiv</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>tom</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>julian</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>erica</td>
    </tr>
  </tbody>
</table>
</div>


