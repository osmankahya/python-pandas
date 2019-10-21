

```python
import pandas as pd
df = pd.read_csv('nyc_weather.cs  v')
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
      <th>EST</th>
      <th>Temperature</th>
      <th>DewPoint</th>
      <th>Humidity</th>
      <th>Sea Level PressureIn</th>
      <th>VisibilityMiles</th>
      <th>WindSpeedMPH</th>
      <th>PrecipitationIn</th>
      <th>CloudCover</th>
      <th>Events</th>
      <th>WindDirDegrees</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2016</td>
      <td>38</td>
      <td>23</td>
      <td>52</td>
      <td>30.03</td>
      <td>10</td>
      <td>8.0</td>
      <td>0</td>
      <td>5</td>
      <td>NaN</td>
      <td>281</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/2/2016</td>
      <td>36</td>
      <td>18</td>
      <td>46</td>
      <td>30.02</td>
      <td>10</td>
      <td>7.0</td>
      <td>0</td>
      <td>3</td>
      <td>NaN</td>
      <td>275</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/3/2016</td>
      <td>40</td>
      <td>21</td>
      <td>47</td>
      <td>29.86</td>
      <td>10</td>
      <td>8.0</td>
      <td>0</td>
      <td>1</td>
      <td>NaN</td>
      <td>277</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/4/2016</td>
      <td>25</td>
      <td>9</td>
      <td>44</td>
      <td>30.05</td>
      <td>10</td>
      <td>9.0</td>
      <td>0</td>
      <td>3</td>
      <td>NaN</td>
      <td>345</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/5/2016</td>
      <td>20</td>
      <td>-3</td>
      <td>41</td>
      <td>30.57</td>
      <td>10</td>
      <td>5.0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>333</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/6/2016</td>
      <td>33</td>
      <td>4</td>
      <td>35</td>
      <td>30.50</td>
      <td>10</td>
      <td>4.0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>259</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/7/2016</td>
      <td>39</td>
      <td>11</td>
      <td>33</td>
      <td>30.28</td>
      <td>10</td>
      <td>2.0</td>
      <td>0</td>
      <td>3</td>
      <td>NaN</td>
      <td>293</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/8/2016</td>
      <td>39</td>
      <td>29</td>
      <td>64</td>
      <td>30.20</td>
      <td>10</td>
      <td>4.0</td>
      <td>0</td>
      <td>8</td>
      <td>NaN</td>
      <td>79</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/9/2016</td>
      <td>44</td>
      <td>38</td>
      <td>77</td>
      <td>30.16</td>
      <td>9</td>
      <td>8.0</td>
      <td>T</td>
      <td>8</td>
      <td>Rain</td>
      <td>76</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1/10/2016</td>
      <td>50</td>
      <td>46</td>
      <td>71</td>
      <td>29.59</td>
      <td>4</td>
      <td>NaN</td>
      <td>1.8</td>
      <td>7</td>
      <td>Rain</td>
      <td>109</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1/11/2016</td>
      <td>33</td>
      <td>8</td>
      <td>37</td>
      <td>29.92</td>
      <td>10</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>NaN</td>
      <td>289</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1/12/2016</td>
      <td>35</td>
      <td>15</td>
      <td>53</td>
      <td>29.85</td>
      <td>10</td>
      <td>6.0</td>
      <td>T</td>
      <td>4</td>
      <td>NaN</td>
      <td>235</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1/13/2016</td>
      <td>26</td>
      <td>4</td>
      <td>42</td>
      <td>29.94</td>
      <td>10</td>
      <td>10.0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>284</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1/14/2016</td>
      <td>30</td>
      <td>12</td>
      <td>47</td>
      <td>29.95</td>
      <td>10</td>
      <td>5.0</td>
      <td>T</td>
      <td>7</td>
      <td>NaN</td>
      <td>266</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1/15/2016</td>
      <td>43</td>
      <td>31</td>
      <td>62</td>
      <td>29.82</td>
      <td>9</td>
      <td>5.0</td>
      <td>T</td>
      <td>2</td>
      <td>NaN</td>
      <td>101</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1/16/2016</td>
      <td>47</td>
      <td>37</td>
      <td>70</td>
      <td>29.52</td>
      <td>8</td>
      <td>7.0</td>
      <td>0.24</td>
      <td>7</td>
      <td>Rain</td>
      <td>340</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1/17/2016</td>
      <td>36</td>
      <td>23</td>
      <td>66</td>
      <td>29.78</td>
      <td>8</td>
      <td>6.0</td>
      <td>0.05</td>
      <td>6</td>
      <td>Fog-Snow</td>
      <td>345</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1/18/2016</td>
      <td>25</td>
      <td>6</td>
      <td>53</td>
      <td>29.83</td>
      <td>9</td>
      <td>12.0</td>
      <td>T</td>
      <td>2</td>
      <td>Snow</td>
      <td>293</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1/19/2016</td>
      <td>22</td>
      <td>3</td>
      <td>42</td>
      <td>30.03</td>
      <td>10</td>
      <td>11.0</td>
      <td>0</td>
      <td>1</td>
      <td>NaN</td>
      <td>293</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1/20/2016</td>
      <td>32</td>
      <td>15</td>
      <td>49</td>
      <td>30.13</td>
      <td>10</td>
      <td>6.0</td>
      <td>0</td>
      <td>2</td>
      <td>NaN</td>
      <td>302</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1/21/2016</td>
      <td>31</td>
      <td>11</td>
      <td>45</td>
      <td>30.15</td>
      <td>10</td>
      <td>6.0</td>
      <td>0</td>
      <td>1</td>
      <td>NaN</td>
      <td>312</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1/22/2016</td>
      <td>26</td>
      <td>6</td>
      <td>41</td>
      <td>30.21</td>
      <td>9</td>
      <td>NaN</td>
      <td>0.01</td>
      <td>3</td>
      <td>Snow</td>
      <td>34</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1/23/2016</td>
      <td>26</td>
      <td>21</td>
      <td>78</td>
      <td>29.77</td>
      <td>1</td>
      <td>16.0</td>
      <td>2.31</td>
      <td>8</td>
      <td>Fog-Snow</td>
      <td>42</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1/24/2016</td>
      <td>28</td>
      <td>11</td>
      <td>53</td>
      <td>29.92</td>
      <td>8</td>
      <td>6.0</td>
      <td>T</td>
      <td>3</td>
      <td>Snow</td>
      <td>327</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1/25/2016</td>
      <td>34</td>
      <td>18</td>
      <td>54</td>
      <td>30.25</td>
      <td>10</td>
      <td>3.0</td>
      <td>0</td>
      <td>2</td>
      <td>NaN</td>
      <td>286</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1/26/2016</td>
      <td>43</td>
      <td>29</td>
      <td>56</td>
      <td>30.03</td>
      <td>10</td>
      <td>7.0</td>
      <td>0</td>
      <td>2</td>
      <td>NaN</td>
      <td>244</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1/27/2016</td>
      <td>41</td>
      <td>22</td>
      <td>45</td>
      <td>30.03</td>
      <td>10</td>
      <td>7.0</td>
      <td>T</td>
      <td>3</td>
      <td>Rain</td>
      <td>311</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1/28/2016</td>
      <td>37</td>
      <td>20</td>
      <td>51</td>
      <td>29.90</td>
      <td>10</td>
      <td>5.0</td>
      <td>0</td>
      <td>1</td>
      <td>NaN</td>
      <td>234</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1/29/2016</td>
      <td>36</td>
      <td>21</td>
      <td>50</td>
      <td>29.58</td>
      <td>10</td>
      <td>8.0</td>
      <td>0</td>
      <td>4</td>
      <td>NaN</td>
      <td>298</td>
    </tr>
    <tr>
      <th>29</th>
      <td>1/30/2016</td>
      <td>34</td>
      <td>16</td>
      <td>46</td>
      <td>30.01</td>
      <td>10</td>
      <td>7.0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>257</td>
    </tr>
    <tr>
      <th>30</th>
      <td>1/31/2016</td>
      <td>46</td>
      <td>28</td>
      <td>52</td>
      <td>29.90</td>
      <td>10</td>
      <td>5.0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>241</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Temperature'].max()
```




    50




```python
df['Humidity'][df['Events']=='Snow']
```




    17    53
    21    41
    23    53
    Name: Humidity, dtype: int64




```python
df.fillna(0, inplace=True)
df['WindSpeedMPH'].mean()

```




    6.225806451612903




```python

```


```python

```
