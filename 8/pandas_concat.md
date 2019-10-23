
# <font color="purple"><h3 align="center">Pandas Concatenate Tutorial</h3></font>

## <font color='blue'>Basic Concatenation</font>


```python
import pandas as pd

india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
india_weather
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>humidity</th>
      <th>temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mumbai</td>
      <td>80</td>
      <td>32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>delhi</td>
      <td>60</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>78</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>




```python
us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
us_weather
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>humidity</th>
      <th>temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>68</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>65</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>75</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.concat([india_weather, us_weather])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>humidity</th>
      <th>temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mumbai</td>
      <td>80</td>
      <td>32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>delhi</td>
      <td>60</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>78</td>
      <td>30</td>
    </tr>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>68</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>65</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>75</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>



## <font color='blue'>Ignore Index</font>


```python
df = pd.concat([india_weather, us_weather], ignore_index=True)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>humidity</th>
      <th>temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mumbai</td>
      <td>80</td>
      <td>32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>delhi</td>
      <td>60</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>78</td>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>new york</td>
      <td>68</td>
      <td>21</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chicago</td>
      <td>65</td>
      <td>14</td>
    </tr>
    <tr>
      <th>5</th>
      <td>orlando</td>
      <td>75</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>



## <font color='blue'>Concatenation And Keys</font>


```python
df = pd.concat([india_weather, us_weather], keys=["india", "us"])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>city</th>
      <th>humidity</th>
      <th>temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">india</th>
      <th>0</th>
      <td>mumbai</td>
      <td>80</td>
      <td>32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>delhi</td>
      <td>60</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>78</td>
      <td>30</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">us</th>
      <th>0</th>
      <td>new york</td>
      <td>68</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>65</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>75</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc["us"]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>humidity</th>
      <th>temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>68</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>65</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>75</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc["india"]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>humidity</th>
      <th>temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mumbai</td>
      <td>80</td>
      <td>32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>delhi</td>
      <td>60</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>78</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>



## <font color='blue'>Concatenation Using Index</font>


```python
temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
}, index=[0,1,2])
temperature_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mumbai</td>
      <td>32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>delhi</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>




```python
windspeed_df = pd.DataFrame({
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
}, index=[1,0])
windspeed_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>windspeed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>delhi</td>
      <td>7</td>
    </tr>
    <tr>
      <th>0</th>
      <td>mumbai</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.concat([temperature_df,windspeed_df],axis=1)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature</th>
      <th>city</th>
      <th>windspeed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mumbai</td>
      <td>32</td>
      <td>mumbai</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>delhi</td>
      <td>45</td>
      <td>delhi</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>30</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## <font color='blue'>Concatenate dataframe with series</font>


```python
s = pd.Series(["Humid","Dry","Rain"], name="event")
s
```




    0    Humid
    1      Dry
    2     Rain
    Name: event, dtype: object




```python
df = pd.concat([temperature_df,s],axis=1)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mumbai</td>
      <td>32</td>
      <td>Humid</td>
    </tr>
    <tr>
      <th>1</th>
      <td>delhi</td>
      <td>45</td>
      <td>Dry</td>
    </tr>
    <tr>
      <th>2</th>
      <td>banglore</td>
      <td>30</td>
      <td>Rain</td>
    </tr>
  </tbody>
</table>
</div>


