
## <font color="purple"><h4 align="center">Read/Write CSV and Excel Files in Pandas</font>

### <font color="blue">Read CSV</color>


```python
import pandas as pd

df = pd.read_csv("stock_data.csv")
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
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("stock_data.csv", skiprows=1)
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
      <th>GOOGL</th>
      <th>27.82</th>
      <th>87</th>
      <th>845</th>
      <th>larry page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("stock_data.csv", header=1) # skiprows and header are kind of same
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
      <th>GOOGL</th>
      <th>27.82</th>
      <th>87</th>
      <th>845</th>
      <th>larry page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>2</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("stock_data.csv", header=None, names = ["ticker","eps","revenue","people"])
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
      <th>ticker</th>
      <th>eps</th>
      <th>revenue</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>tickers</th>
      <td>eps</td>
      <td>revenue</td>
      <td>price</td>
      <td>people</td>
    </tr>
    <tr>
      <th>GOOGL</th>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>WMT</th>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>RIL</th>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>TATA</th>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("stock_data.csv",  nrows=2)
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
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("stock_data.csv", na_values=["n.a.", "not available"])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845.0</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1.00</td>
      <td>85</td>
      <td>64.0</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>NaN</td>
      <td>50</td>
      <td>1023.0</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.60</td>
      <td>-1</td>
      <td>NaN</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("stock_data.csv",  na_values={
        'eps': ['not available'],
        'revenue': [-1],
        'people': ['not available','n.a.']
    })
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87.0</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484.0</td>
      <td>65</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1.00</td>
      <td>85.0</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>NaN</td>
      <td>50.0</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.60</td>
      <td>NaN</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>



### <font color="blue">Write to CSV</color>


```python
df.to_csv("new.csv", index=False)
```


```python
df.columns
```




    Index(['tickers', 'eps', 'revenue', 'price', 'people'], dtype='object')




```python
df.to_csv("new.csv",header=False)
```


```python
df.to_csv("new.csv", columns=["tickers","price"], index=False)
```

### <font color="blue">Read Excel</color>


```python
df = pd.read_excel("stock_data.xlsx","Sheet1")
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>n.a.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>n.a.</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>




```python
def convert_people_cell(cell):
    if cell=="n.a.":
        return 'Sam Walton'
    return cell

def convert_price_cell(cell):
    if cell=="n.a.":
        return 50
    return cell
    
df = pd.read_excel("stock_data.xlsx","Sheet1", converters= {
        'people': convert_people_cell,
        'price': convert_price_cell
    })
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tickers</th>
      <th>eps</th>
      <th>revenue</th>
      <th>price</th>
      <th>people</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GOOGL</td>
      <td>27.82</td>
      <td>87</td>
      <td>845</td>
      <td>larry page</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WMT</td>
      <td>4.61</td>
      <td>484</td>
      <td>65</td>
      <td>Sam Walton</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSFT</td>
      <td>-1</td>
      <td>85</td>
      <td>64</td>
      <td>bill gates</td>
    </tr>
    <tr>
      <th>3</th>
      <td>RIL</td>
      <td>not available</td>
      <td>50</td>
      <td>1023</td>
      <td>mukesh ambani</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TATA</td>
      <td>5.6</td>
      <td>-1</td>
      <td>50</td>
      <td>ratan tata</td>
    </tr>
  </tbody>
</table>
</div>



### <font color="blue">Write to Excel</color>


```python
df.to_excel("new.xlsx", sheet_name="stocks", index=False, startrow=2, startcol=1)
```

**Write two dataframes to two separate sheets in excel**


```python
df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})
```


```python
with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")
```
