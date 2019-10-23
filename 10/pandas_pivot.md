
<h1 style="color:blue">Pivot basics</h1>


```python
import pandas as pd
import numpy as np
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
      <th>date</th>
      <th>city</th>
      <th>temperature</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5/1/2017</td>
      <td>new york</td>
      <td>65</td>
      <td>56</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5/2/2017</td>
      <td>new york</td>
      <td>66</td>
      <td>58</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5/3/2017</td>
      <td>new york</td>
      <td>68</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5/1/2017</td>
      <td>mumbai</td>
      <td>75</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5/2/2017</td>
      <td>mumbai</td>
      <td>78</td>
      <td>83</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5/3/2017</td>
      <td>mumbai</td>
      <td>82</td>
      <td>85</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5/1/2017</td>
      <td>beijing</td>
      <td>80</td>
      <td>26</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5/2/2017</td>
      <td>beijing</td>
      <td>77</td>
      <td>30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5/3/2017</td>
      <td>beijing</td>
      <td>79</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.pivot(index='city',columns='date')
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
      <th></th>
      <th colspan="3" halign="left">temperature</th>
      <th colspan="3" halign="left">humidity</th>
    </tr>
    <tr>
      <th>date</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
    </tr>
    <tr>
      <th>city</th>
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
      <th>beijing</th>
      <td>80</td>
      <td>77</td>
      <td>79</td>
      <td>26</td>
      <td>30</td>
      <td>35</td>
    </tr>
    <tr>
      <th>mumbai</th>
      <td>75</td>
      <td>78</td>
      <td>82</td>
      <td>80</td>
      <td>83</td>
      <td>85</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>65</td>
      <td>66</td>
      <td>68</td>
      <td>56</td>
      <td>58</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.pivot(index='city',columns='date',values="humidity")
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
      <th>date</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>beijing</th>
      <td>26</td>
      <td>30</td>
      <td>35</td>
    </tr>
    <tr>
      <th>mumbai</th>
      <td>80</td>
      <td>83</td>
      <td>85</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>56</td>
      <td>58</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.pivot(index='date',columns='city')
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
      <th></th>
      <th colspan="3" halign="left">temperature</th>
      <th colspan="3" halign="left">humidity</th>
    </tr>
    <tr>
      <th>city</th>
      <th>beijing</th>
      <th>mumbai</th>
      <th>new york</th>
      <th>beijing</th>
      <th>mumbai</th>
      <th>new york</th>
    </tr>
    <tr>
      <th>date</th>
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
      <th>5/1/2017</th>
      <td>80</td>
      <td>75</td>
      <td>65</td>
      <td>26</td>
      <td>80</td>
      <td>56</td>
    </tr>
    <tr>
      <th>5/2/2017</th>
      <td>77</td>
      <td>78</td>
      <td>66</td>
      <td>30</td>
      <td>83</td>
      <td>58</td>
    </tr>
    <tr>
      <th>5/3/2017</th>
      <td>79</td>
      <td>82</td>
      <td>68</td>
      <td>35</td>
      <td>85</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.pivot(index='humidity',columns='city')
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
      <th></th>
      <th colspan="3" halign="left">date</th>
      <th colspan="3" halign="left">temperature</th>
    </tr>
    <tr>
      <th>city</th>
      <th>beijing</th>
      <th>mumbai</th>
      <th>new york</th>
      <th>beijing</th>
      <th>mumbai</th>
      <th>new york</th>
    </tr>
    <tr>
      <th>humidity</th>
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
      <th>26</th>
      <td>5/1/2017</td>
      <td>None</td>
      <td>None</td>
      <td>80.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>30</th>
      <td>5/2/2017</td>
      <td>None</td>
      <td>None</td>
      <td>77.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35</th>
      <td>5/3/2017</td>
      <td>None</td>
      <td>None</td>
      <td>79.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>56</th>
      <td>None</td>
      <td>None</td>
      <td>5/1/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>65.0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>None</td>
      <td>None</td>
      <td>5/2/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>60</th>
      <td>None</td>
      <td>None</td>
      <td>5/3/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>80</th>
      <td>None</td>
      <td>5/1/2017</td>
      <td>None</td>
      <td>NaN</td>
      <td>75.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>83</th>
      <td>None</td>
      <td>5/2/2017</td>
      <td>None</td>
      <td>NaN</td>
      <td>78.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>85</th>
      <td>None</td>
      <td>5/3/2017</td>
      <td>None</td>
      <td>NaN</td>
      <td>82.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



<h1 style="color:blue">Pivot Table</h1>


```python
df = pd.read_csv("weather2.csv")
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
      <th>date</th>
      <th>city</th>
      <th>temperature</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5/1/2017</td>
      <td>new york</td>
      <td>65</td>
      <td>56</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5/1/2017</td>
      <td>new york</td>
      <td>61</td>
      <td>54</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5/2/2017</td>
      <td>new york</td>
      <td>70</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5/2/2017</td>
      <td>new york</td>
      <td>72</td>
      <td>62</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5/1/2017</td>
      <td>mumbai</td>
      <td>75</td>
      <td>80</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5/1/2017</td>
      <td>mumbai</td>
      <td>78</td>
      <td>83</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5/2/2017</td>
      <td>mumbai</td>
      <td>82</td>
      <td>85</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5/2/2017</td>
      <td>mumbai</td>
      <td>80</td>
      <td>26</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.pivot_table(index="city",columns="date")
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
      <th></th>
      <th colspan="2" halign="left">humidity</th>
      <th colspan="2" halign="left">temperature</th>
    </tr>
    <tr>
      <th>date</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>mumbai</th>
      <td>81.5</td>
      <td>55.5</td>
      <td>76.5</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>55.0</td>
      <td>61.0</td>
      <td>63.0</td>
      <td>71.0</td>
    </tr>
  </tbody>
</table>
</div>



<h2 style="color:brown">Margins</h2>


```python
df.pivot_table(index="city",columns="date", margins=True,aggfunc=np.sum)
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
      <th></th>
      <th colspan="4" halign="left">humidity</th>
      <th colspan="4" halign="left">temperature</th>
    </tr>
    <tr>
      <th>date</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
      <th>All</th>
      <th>5/1/2017</th>
      <th>5/2/2017</th>
      <th>5/3/2017</th>
      <th>All</th>
    </tr>
    <tr>
      <th>city</th>
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
      <th>beijing</th>
      <td>26.0</td>
      <td>30.0</td>
      <td>35.0</td>
      <td>91.0</td>
      <td>80.0</td>
      <td>77.0</td>
      <td>79.0</td>
      <td>236.0</td>
    </tr>
    <tr>
      <th>mumbai</th>
      <td>80.0</td>
      <td>83.0</td>
      <td>85.0</td>
      <td>248.0</td>
      <td>75.0</td>
      <td>78.0</td>
      <td>82.0</td>
      <td>235.0</td>
    </tr>
    <tr>
      <th>new york</th>
      <td>110.0</td>
      <td>122.0</td>
      <td>60.0</td>
      <td>292.0</td>
      <td>126.0</td>
      <td>142.0</td>
      <td>68.0</td>
      <td>336.0</td>
    </tr>
    <tr>
      <th>All</th>
      <td>216.0</td>
      <td>235.0</td>
      <td>180.0</td>
      <td>631.0</td>
      <td>281.0</td>
      <td>297.0</td>
      <td>229.0</td>
      <td>807.0</td>
    </tr>
  </tbody>
</table>
</div>



<h2 style="color:brown">Grouper</h2>


```python
df = pd.read_csv("weather3.csv")
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
      <th>date</th>
      <th>city</th>
      <th>temperature</th>
      <th>humidity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5/1/2017</td>
      <td>new york</td>
      <td>65</td>
      <td>56</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5/2/2017</td>
      <td>new york</td>
      <td>61</td>
      <td>54</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5/3/2017</td>
      <td>new york</td>
      <td>70</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12/1/2017</td>
      <td>new york</td>
      <td>30</td>
      <td>50</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12/2/2017</td>
      <td>new york</td>
      <td>28</td>
      <td>52</td>
    </tr>
    <tr>
      <th>5</th>
      <td>12/3/2017</td>
      <td>new york</td>
      <td>25</td>
      <td>51</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['date'] = pd.to_datetime(df['date'])
```


```python
df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city')
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
      <th></th>
      <th>humidity</th>
      <th>temperature</th>
    </tr>
    <tr>
      <th>city</th>
      <th>new york</th>
      <th>new york</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-05-31</th>
      <td>56.666667</td>
      <td>65.333333</td>
    </tr>
    <tr>
      <th>2017-12-31</th>
      <td>51.000000</td>
      <td>27.666667</td>
    </tr>
  </tbody>
</table>
</div>


