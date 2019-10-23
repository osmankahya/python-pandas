
# <font color="purple"><h3 align="center">Pandas Merge Tutorial</h3></font>

## <font color='blue'>Basic Merge Using a Dataframe Column</font>


```python
import pandas as pd
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
df1
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
      <td>new york</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
df2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>chicago</td>
      <td>65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>new york</td>
      <td>68</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3 = pd.merge(df1, df2, on="city")
df3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>21</td>
      <td>68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14</td>
      <td>65</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>35</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>



## <font color='blue'>Type Of DataBase Joins</font>

<img src="db_joins.jpg" height="800", width="800">


```python
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35, 38],
})
df1
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
      <td>new york</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>35</td>
    </tr>
    <tr>
      <th>3</th>
      <td>baltimore</td>
      <td>38</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "humidity": [65,68,71],
})
df2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>chicago</td>
      <td>65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>new york</td>
      <td>68</td>
    </tr>
    <tr>
      <th>2</th>
      <td>san diego</td>
      <td>71</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3=pd.merge(df1,df2,on="city",how="inner")
df3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>21</td>
      <td>68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14</td>
      <td>65</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3=pd.merge(df1,df2,on="city",how="outer")
df3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>21.0</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14.0</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>35.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>baltimore</td>
      <td>38.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>san diego</td>
      <td>NaN</td>
      <td>71.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3=pd.merge(df1,df2,on="city",how="left")
df3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>21</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>35</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>baltimore</td>
      <td>38</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3=pd.merge(df1,df2,on="city",how="right")
df3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>21.0</td>
      <td>68</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14.0</td>
      <td>65</td>
    </tr>
    <tr>
      <th>2</th>
      <td>san diego</td>
      <td>NaN</td>
      <td>71</td>
    </tr>
  </tbody>
</table>
</div>



## <font color='blue'>indicator flag</font>


```python
df3=pd.merge(df1,df2,on="city",how="outer",indicator=True)
df3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>temperature</th>
      <th>humidity</th>
      <th>_merge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>21.0</td>
      <td>68.0</td>
      <td>both</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>14.0</td>
      <td>65.0</td>
      <td>both</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>35.0</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>3</th>
      <td>baltimore</td>
      <td>38.0</td>
      <td>NaN</td>
      <td>left_only</td>
    </tr>
    <tr>
      <th>4</th>
      <td>san diego</td>
      <td>NaN</td>
      <td>71.0</td>
      <td>right_only</td>
    </tr>
  </tbody>
</table>
</div>



## <font color='blue'>suffixes</font>


```python
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})
df1
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
      <td>65</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>68</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>71</td>
      <td>35</td>
    </tr>
    <tr>
      <th>3</th>
      <td>baltimore</td>
      <td>75</td>
      <td>38</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})
df2
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
      <td>chicago</td>
      <td>65</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>new york</td>
      <td>68</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>san diego</td>
      <td>71</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3= pd.merge(df1,df2,on="city",how="outer", suffixes=('_first','_second'))
df3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>humidity_first</th>
      <th>temperature_first</th>
      <th>humidity_second</th>
      <th>temperature_second</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>new york</td>
      <td>65.0</td>
      <td>21.0</td>
      <td>68.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chicago</td>
      <td>68.0</td>
      <td>14.0</td>
      <td>65.0</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>orlando</td>
      <td>71.0</td>
      <td>35.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>baltimore</td>
      <td>75.0</td>
      <td>38.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>san diego</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>71.0</td>
      <td>35.0</td>
    </tr>
  </tbody>
</table>
</div>



## <font color='blue'>join</font>


```python
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
df1.set_index('city',inplace=True)
df1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>new york</th>
      <td>21</td>
    </tr>
    <tr>
      <th>chicago</th>
      <td>14</td>
    </tr>
    <tr>
      <th>orlando</th>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
df2.set_index('city',inplace=True)
df2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>humidity</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>chicago</th>
      <td>65</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>68</td>
    </tr>
    <tr>
      <th>orlando</th>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.join(df2,lsuffix='_l', rsuffix='_r')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>humidity</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>new york</th>
      <td>21</td>
      <td>68</td>
    </tr>
    <tr>
      <th>chicago</th>
      <td>14</td>
      <td>65</td>
    </tr>
    <tr>
      <th>orlando</th>
      <td>35</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>


