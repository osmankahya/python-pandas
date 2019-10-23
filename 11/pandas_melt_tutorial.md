
# <font color="purple"><h3 align="center">Reshape pandas dataframe using melt</h3></font>


```python
import pandas as pd
df = pd.read_csv("weather.csv")
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
      <th>day</th>
      <th>chicago</th>
      <th>chennai</th>
      <th>berlin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>32</td>
      <td>75</td>
      <td>41</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tuesday</td>
      <td>30</td>
      <td>77</td>
      <td>43</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wednesday</td>
      <td>28</td>
      <td>75</td>
      <td>45</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Thursday</td>
      <td>22</td>
      <td>82</td>
      <td>38</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Friday</td>
      <td>30</td>
      <td>83</td>
      <td>30</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Saturday</td>
      <td>20</td>
      <td>81</td>
      <td>45</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Sunday</td>
      <td>25</td>
      <td>77</td>
      <td>47</td>
    </tr>
  </tbody>
</table>
</div>




```python
melted = pd.melt(df, id_vars=["day"], var_name='city', value_name='temperature')
melted
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
      <th>day</th>
      <th>city</th>
      <th>temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Monday</td>
      <td>chicago</td>
      <td>32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tuesday</td>
      <td>chicago</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wednesday</td>
      <td>chicago</td>
      <td>28</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Thursday</td>
      <td>chicago</td>
      <td>22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Friday</td>
      <td>chicago</td>
      <td>30</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Saturday</td>
      <td>chicago</td>
      <td>20</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Sunday</td>
      <td>chicago</td>
      <td>25</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Monday</td>
      <td>chennai</td>
      <td>75</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Tuesday</td>
      <td>chennai</td>
      <td>77</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Wednesday</td>
      <td>chennai</td>
      <td>75</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Thursday</td>
      <td>chennai</td>
      <td>82</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Friday</td>
      <td>chennai</td>
      <td>83</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Saturday</td>
      <td>chennai</td>
      <td>81</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Sunday</td>
      <td>chennai</td>
      <td>77</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Monday</td>
      <td>berlin</td>
      <td>41</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Tuesday</td>
      <td>berlin</td>
      <td>43</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Wednesday</td>
      <td>berlin</td>
      <td>45</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Thursday</td>
      <td>berlin</td>
      <td>38</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Friday</td>
      <td>berlin</td>
      <td>30</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Saturday</td>
      <td>berlin</td>
      <td>45</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Sunday</td>
      <td>berlin</td>
      <td>47</td>
    </tr>
  </tbody>
</table>
</div>


