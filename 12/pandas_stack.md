
<h1 style="color:blue">Reshape dataframe using stack/unstack</h1>


```python
import pandas as pd
df = pd.read_excel("stocks.xlsx",header=[0,1])
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
    <tr>
      <th></th>
      <th colspan="3" halign="left">Price</th>
      <th colspan="3" halign="left">Price to earnings ratio (P/E)</th>
    </tr>
    <tr>
      <th>Company</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-06-05</th>
      <td>155</td>
      <td>955</td>
      <td>66</td>
      <td>37.10</td>
      <td>32.0</td>
      <td>30.31</td>
    </tr>
    <tr>
      <th>2017-06-06</th>
      <td>150</td>
      <td>987</td>
      <td>69</td>
      <td>36.98</td>
      <td>31.3</td>
      <td>30.56</td>
    </tr>
    <tr>
      <th>2017-06-07</th>
      <td>153</td>
      <td>963</td>
      <td>62</td>
      <td>36.78</td>
      <td>31.7</td>
      <td>30.46</td>
    </tr>
    <tr>
      <th>2017-06-08</th>
      <td>155</td>
      <td>1000</td>
      <td>61</td>
      <td>36.11</td>
      <td>31.2</td>
      <td>30.11</td>
    </tr>
    <tr>
      <th>2017-06-09</th>
      <td>156</td>
      <td>1012</td>
      <td>66</td>
      <td>37.07</td>
      <td>30.0</td>
      <td>31.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.stack()
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
      <th></th>
      <th>Price</th>
      <th>Price to earnings ratio (P/E)</th>
    </tr>
    <tr>
      <th></th>
      <th>Company</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">2017-06-05</th>
      <th>Facebook</th>
      <td>155</td>
      <td>37.10</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>955</td>
      <td>32.00</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>66</td>
      <td>30.31</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2017-06-06</th>
      <th>Facebook</th>
      <td>150</td>
      <td>36.98</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>987</td>
      <td>31.30</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>69</td>
      <td>30.56</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2017-06-07</th>
      <th>Facebook</th>
      <td>153</td>
      <td>36.78</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>963</td>
      <td>31.70</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>62</td>
      <td>30.46</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2017-06-08</th>
      <th>Facebook</th>
      <td>155</td>
      <td>36.11</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>1000</td>
      <td>31.20</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>61</td>
      <td>30.11</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2017-06-09</th>
      <th>Facebook</th>
      <td>156</td>
      <td>37.07</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>1012</td>
      <td>30.00</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>66</td>
      <td>31.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.stack(level=0)
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
      <th>Company</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">2017-06-05</th>
      <th>Price</th>
      <td>155.00</td>
      <td>955.0</td>
      <td>66.00</td>
    </tr>
    <tr>
      <th>Price to earnings ratio (P/E)</th>
      <td>37.10</td>
      <td>32.0</td>
      <td>30.31</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2017-06-06</th>
      <th>Price</th>
      <td>150.00</td>
      <td>987.0</td>
      <td>69.00</td>
    </tr>
    <tr>
      <th>Price to earnings ratio (P/E)</th>
      <td>36.98</td>
      <td>31.3</td>
      <td>30.56</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2017-06-07</th>
      <th>Price</th>
      <td>153.00</td>
      <td>963.0</td>
      <td>62.00</td>
    </tr>
    <tr>
      <th>Price to earnings ratio (P/E)</th>
      <td>36.78</td>
      <td>31.7</td>
      <td>30.46</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2017-06-08</th>
      <th>Price</th>
      <td>155.00</td>
      <td>1000.0</td>
      <td>61.00</td>
    </tr>
    <tr>
      <th>Price to earnings ratio (P/E)</th>
      <td>36.11</td>
      <td>31.2</td>
      <td>30.11</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2017-06-09</th>
      <th>Price</th>
      <td>156.00</td>
      <td>1012.0</td>
      <td>66.00</td>
    </tr>
    <tr>
      <th>Price to earnings ratio (P/E)</th>
      <td>37.07</td>
      <td>30.0</td>
      <td>31.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_stacked=df.stack()
df_stacked
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
      <th></th>
      <th>Price</th>
      <th>Price to earnings ratio (P/E)</th>
    </tr>
    <tr>
      <th></th>
      <th>Company</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">2017-06-05</th>
      <th>Facebook</th>
      <td>155</td>
      <td>37.10</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>955</td>
      <td>32.00</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>66</td>
      <td>30.31</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2017-06-06</th>
      <th>Facebook</th>
      <td>150</td>
      <td>36.98</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>987</td>
      <td>31.30</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>69</td>
      <td>30.56</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2017-06-07</th>
      <th>Facebook</th>
      <td>153</td>
      <td>36.78</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>963</td>
      <td>31.70</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>62</td>
      <td>30.46</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2017-06-08</th>
      <th>Facebook</th>
      <td>155</td>
      <td>36.11</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>1000</td>
      <td>31.20</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>61</td>
      <td>30.11</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">2017-06-09</th>
      <th>Facebook</th>
      <td>156</td>
      <td>37.07</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>1012</td>
      <td>30.00</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>66</td>
      <td>31.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_stacked.unstack()
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
      <th colspan="3" halign="left">Price</th>
      <th colspan="3" halign="left">Price to earnings ratio (P/E)</th>
    </tr>
    <tr>
      <th>Company</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-06-05</th>
      <td>155</td>
      <td>955</td>
      <td>66</td>
      <td>37.10</td>
      <td>32.0</td>
      <td>30.31</td>
    </tr>
    <tr>
      <th>2017-06-06</th>
      <td>150</td>
      <td>987</td>
      <td>69</td>
      <td>36.98</td>
      <td>31.3</td>
      <td>30.56</td>
    </tr>
    <tr>
      <th>2017-06-07</th>
      <td>153</td>
      <td>963</td>
      <td>62</td>
      <td>36.78</td>
      <td>31.7</td>
      <td>30.46</td>
    </tr>
    <tr>
      <th>2017-06-08</th>
      <td>155</td>
      <td>1000</td>
      <td>61</td>
      <td>36.11</td>
      <td>31.2</td>
      <td>30.11</td>
    </tr>
    <tr>
      <th>2017-06-09</th>
      <td>156</td>
      <td>1012</td>
      <td>66</td>
      <td>37.07</td>
      <td>30.0</td>
      <td>31.00</td>
    </tr>
  </tbody>
</table>
</div>



<h1 style="color:blue">3 levels of column headers</h1>


```python
df2 = pd.read_excel("stocks_3_levels.xlsx",header=[0,1,2])
df2
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
      <th colspan="6" halign="left">Price Ratios</th>
      <th colspan="6" halign="left">Income Statement</th>
    </tr>
    <tr>
      <th></th>
      <th colspan="3" halign="left">Price</th>
      <th colspan="3" halign="left">Price to earnings ratio (P/E)</th>
      <th colspan="3" halign="left">Net Sales</th>
      <th colspan="3" halign="left">Net Profit</th>
    </tr>
    <tr>
      <th>Company</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Q1 2016</th>
      <td>155</td>
      <td>955</td>
      <td>66</td>
      <td>37.10</td>
      <td>32.0</td>
      <td>30.31</td>
      <td>2.6</td>
      <td>20</td>
      <td>18.70</td>
      <td>0.80</td>
      <td>5.43</td>
      <td>4.56</td>
    </tr>
    <tr>
      <th>Q2 2016</th>
      <td>150</td>
      <td>987</td>
      <td>69</td>
      <td>36.98</td>
      <td>31.3</td>
      <td>30.56</td>
      <td>3.1</td>
      <td>22</td>
      <td>21.30</td>
      <td>0.97</td>
      <td>5.89</td>
      <td>5.10</td>
    </tr>
    <tr>
      <th>Q3 2016</th>
      <td>153</td>
      <td>963</td>
      <td>62</td>
      <td>36.78</td>
      <td>31.7</td>
      <td>30.46</td>
      <td>4.3</td>
      <td>24</td>
      <td>21.45</td>
      <td>1.20</td>
      <td>6.10</td>
      <td>5.43</td>
    </tr>
    <tr>
      <th>Q4 2016</th>
      <td>155</td>
      <td>1000</td>
      <td>61</td>
      <td>36.11</td>
      <td>31.2</td>
      <td>30.11</td>
      <td>6.7</td>
      <td>26</td>
      <td>21.88</td>
      <td>1.67</td>
      <td>6.50</td>
      <td>5.89</td>
    </tr>
    <tr>
      <th>Q1 2017</th>
      <td>156</td>
      <td>1012</td>
      <td>66</td>
      <td>37.07</td>
      <td>30.0</td>
      <td>31.00</td>
      <td>8.1</td>
      <td>31</td>
      <td>22.34</td>
      <td>2.03</td>
      <td>6.40</td>
      <td>6.09</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.stack()
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
      <th></th>
      <th colspan="2" halign="left">Income Statement</th>
      <th colspan="2" halign="left">Price Ratios</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>Net Profit</th>
      <th>Net Sales</th>
      <th>Price</th>
      <th>Price to earnings ratio (P/E)</th>
    </tr>
    <tr>
      <th></th>
      <th>Company</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">Q1 2016</th>
      <th>Facebook</th>
      <td>0.80</td>
      <td>2.60</td>
      <td>155</td>
      <td>37.10</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>5.43</td>
      <td>20.00</td>
      <td>955</td>
      <td>32.00</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>4.56</td>
      <td>18.70</td>
      <td>66</td>
      <td>30.31</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Q2 2016</th>
      <th>Facebook</th>
      <td>0.97</td>
      <td>3.10</td>
      <td>150</td>
      <td>36.98</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>5.89</td>
      <td>22.00</td>
      <td>987</td>
      <td>31.30</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>5.10</td>
      <td>21.30</td>
      <td>69</td>
      <td>30.56</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Q3 2016</th>
      <th>Facebook</th>
      <td>1.20</td>
      <td>4.30</td>
      <td>153</td>
      <td>36.78</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>6.10</td>
      <td>24.00</td>
      <td>963</td>
      <td>31.70</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>5.43</td>
      <td>21.45</td>
      <td>62</td>
      <td>30.46</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Q4 2016</th>
      <th>Facebook</th>
      <td>1.67</td>
      <td>6.70</td>
      <td>155</td>
      <td>36.11</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>6.50</td>
      <td>26.00</td>
      <td>1000</td>
      <td>31.20</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>5.89</td>
      <td>21.88</td>
      <td>61</td>
      <td>30.11</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Q1 2017</th>
      <th>Facebook</th>
      <td>2.03</td>
      <td>8.10</td>
      <td>156</td>
      <td>37.07</td>
    </tr>
    <tr>
      <th>Google</th>
      <td>6.40</td>
      <td>31.00</td>
      <td>1012</td>
      <td>30.00</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>6.09</td>
      <td>22.34</td>
      <td>66</td>
      <td>31.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.stack(level=0)
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
      <th></th>
      <th colspan="3" halign="left">Net Profit</th>
      <th colspan="3" halign="left">Net Sales</th>
      <th colspan="3" halign="left">Price</th>
      <th colspan="3" halign="left">Price to earnings ratio (P/E)</th>
    </tr>
    <tr>
      <th></th>
      <th>Company</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Q1 2016</th>
      <th>Income Statement</th>
      <td>0.80</td>
      <td>5.43</td>
      <td>4.56</td>
      <td>2.6</td>
      <td>20.0</td>
      <td>18.70</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Price Ratios</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>155.0</td>
      <td>955.0</td>
      <td>66.0</td>
      <td>37.10</td>
      <td>32.0</td>
      <td>30.31</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Q2 2016</th>
      <th>Income Statement</th>
      <td>0.97</td>
      <td>5.89</td>
      <td>5.10</td>
      <td>3.1</td>
      <td>22.0</td>
      <td>21.30</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Price Ratios</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>150.0</td>
      <td>987.0</td>
      <td>69.0</td>
      <td>36.98</td>
      <td>31.3</td>
      <td>30.56</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Q3 2016</th>
      <th>Income Statement</th>
      <td>1.20</td>
      <td>6.10</td>
      <td>5.43</td>
      <td>4.3</td>
      <td>24.0</td>
      <td>21.45</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Price Ratios</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>153.0</td>
      <td>963.0</td>
      <td>62.0</td>
      <td>36.78</td>
      <td>31.7</td>
      <td>30.46</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Q4 2016</th>
      <th>Income Statement</th>
      <td>1.67</td>
      <td>6.50</td>
      <td>5.89</td>
      <td>6.7</td>
      <td>26.0</td>
      <td>21.88</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Price Ratios</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>155.0</td>
      <td>1000.0</td>
      <td>61.0</td>
      <td>36.11</td>
      <td>31.2</td>
      <td>30.11</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Q1 2017</th>
      <th>Income Statement</th>
      <td>2.03</td>
      <td>6.40</td>
      <td>6.09</td>
      <td>8.1</td>
      <td>31.0</td>
      <td>22.34</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Price Ratios</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>156.0</td>
      <td>1012.0</td>
      <td>66.0</td>
      <td>37.07</td>
      <td>30.0</td>
      <td>31.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.stack(level=1)
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
      <th></th>
      <th colspan="3" halign="left">Income Statement</th>
      <th colspan="3" halign="left">Price Ratios</th>
    </tr>
    <tr>
      <th></th>
      <th>Company</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
      <th>Facebook</th>
      <th>Google</th>
      <th>Microsoft</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Q1 2016</th>
      <th>Net Profit</th>
      <td>0.80</td>
      <td>5.43</td>
      <td>4.56</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Net Sales</th>
      <td>2.60</td>
      <td>20.00</td>
      <td>18.70</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Price</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>155.00</td>
      <td>955.0</td>
      <td>66.00</td>
    </tr>
    <tr>
      <th>Price to earnings ratio (P/E)</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37.10</td>
      <td>32.0</td>
      <td>30.31</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Q2 2016</th>
      <th>Net Profit</th>
      <td>0.97</td>
      <td>5.89</td>
      <td>5.10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Net Sales</th>
      <td>3.10</td>
      <td>22.00</td>
      <td>21.30</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Price</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>150.00</td>
      <td>987.0</td>
      <td>69.00</td>
    </tr>
    <tr>
      <th>Price to earnings ratio (P/E)</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.98</td>
      <td>31.3</td>
      <td>30.56</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Q3 2016</th>
      <th>Net Profit</th>
      <td>1.20</td>
      <td>6.10</td>
      <td>5.43</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Net Sales</th>
      <td>4.30</td>
      <td>24.00</td>
      <td>21.45</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Price</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>153.00</td>
      <td>963.0</td>
      <td>62.00</td>
    </tr>
    <tr>
      <th>Price to earnings ratio (P/E)</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.78</td>
      <td>31.7</td>
      <td>30.46</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Q4 2016</th>
      <th>Net Profit</th>
      <td>1.67</td>
      <td>6.50</td>
      <td>5.89</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Net Sales</th>
      <td>6.70</td>
      <td>26.00</td>
      <td>21.88</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Price</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>155.00</td>
      <td>1000.0</td>
      <td>61.00</td>
    </tr>
    <tr>
      <th>Price to earnings ratio (P/E)</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>36.11</td>
      <td>31.2</td>
      <td>30.11</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Q1 2017</th>
      <th>Net Profit</th>
      <td>2.03</td>
      <td>6.40</td>
      <td>6.09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Net Sales</th>
      <td>8.10</td>
      <td>31.00</td>
      <td>22.34</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Price</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>156.00</td>
      <td>1012.0</td>
      <td>66.00</td>
    </tr>
    <tr>
      <th>Price to earnings ratio (P/E)</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37.07</td>
      <td>30.0</td>
      <td>31.00</td>
    </tr>
  </tbody>
</table>
</div>


