
<h1 style="color:blue" align="center">Crosstab Tutorial</h1>


```python
import pandas as pd
df = pd.read_excel("survey.xls")
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
      <th>Name</th>
      <th>Nationality</th>
      <th>Sex</th>
      <th>Age</th>
      <th>Handedness</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kathy</td>
      <td>USA</td>
      <td>Female</td>
      <td>23</td>
      <td>Right</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Linda</td>
      <td>USA</td>
      <td>Female</td>
      <td>18</td>
      <td>Right</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Peter</td>
      <td>USA</td>
      <td>Male</td>
      <td>19</td>
      <td>Right</td>
    </tr>
    <tr>
      <th>3</th>
      <td>John</td>
      <td>USA</td>
      <td>Male</td>
      <td>22</td>
      <td>Left</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Fatima</td>
      <td>Bangadesh</td>
      <td>Female</td>
      <td>31</td>
      <td>Left</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Kadir</td>
      <td>Bangadesh</td>
      <td>Male</td>
      <td>25</td>
      <td>Left</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dhaval</td>
      <td>India</td>
      <td>Male</td>
      <td>35</td>
      <td>Left</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Sudhir</td>
      <td>India</td>
      <td>Male</td>
      <td>31</td>
      <td>Left</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Parvir</td>
      <td>India</td>
      <td>Male</td>
      <td>37</td>
      <td>Right</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Yan</td>
      <td>China</td>
      <td>Female</td>
      <td>52</td>
      <td>Right</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Juan</td>
      <td>China</td>
      <td>Female</td>
      <td>58</td>
      <td>Left</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Liang</td>
      <td>China</td>
      <td>Male</td>
      <td>43</td>
      <td>Left</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.crosstab(df.Nationality,df.Handedness)
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
      <th>Handedness</th>
      <th>Left</th>
      <th>Right</th>
    </tr>
    <tr>
      <th>Nationality</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bangadesh</th>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>China</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>India</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>USA</th>
      <td>1</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.crosstab(df.Sex,df.Handedness)
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
      <th>Handedness</th>
      <th>Left</th>
      <th>Right</th>
    </tr>
    <tr>
      <th>Sex</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>5</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



<h2 style="color:purple">Margins</h2>


```python
pd.crosstab(df.Sex,df.Handedness, margins=True)
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
      <th>Handedness</th>
      <th>Left</th>
      <th>Right</th>
      <th>All</th>
    </tr>
    <tr>
      <th>Sex</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>2</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>5</td>
      <td>2</td>
      <td>7</td>
    </tr>
    <tr>
      <th>All</th>
      <td>7</td>
      <td>5</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



<h2 style="color:purple">Multi Index Column and Rows</h2>


```python
pd.crosstab(df.Sex, [df.Handedness,df.Nationality], margins=True)
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
    <tr>
      <th>Handedness</th>
      <th colspan="4" halign="left">Left</th>
      <th colspan="3" halign="left">Right</th>
      <th>All</th>
    </tr>
    <tr>
      <th>Nationality</th>
      <th>Bangadesh</th>
      <th>China</th>
      <th>India</th>
      <th>USA</th>
      <th>China</th>
      <th>India</th>
      <th>USA</th>
      <th></th>
    </tr>
    <tr>
      <th>Sex</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>All</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.crosstab([df.Nationality, df.Sex], [df.Handedness], margins=True)
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
      <th>Handedness</th>
      <th>Left</th>
      <th>Right</th>
      <th>All</th>
    </tr>
    <tr>
      <th>Nationality</th>
      <th>Sex</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Bangadesh</th>
      <th>Female</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">China</th>
      <th>Female</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>India</th>
      <th>Male</th>
      <td>2</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">USA</th>
      <th>Female</th>
      <td>0</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>All</th>
      <th></th>
      <td>7</td>
      <td>5</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



<h2 style="color:purple">Normalize</h2>


```python
pd.crosstab(df.Sex, df.Handedness, normalize='index')
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
      <th>Handedness</th>
      <th>Left</th>
      <th>Right</th>
    </tr>
    <tr>
      <th>Sex</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>0.400000</td>
      <td>0.600000</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>0.714286</td>
      <td>0.285714</td>
    </tr>
  </tbody>
</table>
</div>



<h2 style="color:purple">Aggfunc and Values</h2>


```python
import numpy as np
pd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.average)
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
      <th>Handedness</th>
      <th>Left</th>
      <th>Right</th>
    </tr>
    <tr>
      <th>Sex</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>44.5</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>31.2</td>
      <td>28.0</td>
    </tr>
  </tbody>
</table>
</div>


