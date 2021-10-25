# Surfs_Up

In this project, I was tasked with analyzing weather trends in Oahu, Hawaii for the months of June and December in order to help provide a strong case for the viability of an icecream shop all year round. This analysis, makes use of the SQLite database, the sqlalchemy ORM for python and the pandas module to process weather data.

---

**Challenge-relevant code is located in the surf_challenge folder**

---

## Results

- Oahu's temperature range is incredibly tight. From a 56F minimum in December to an 83F maximum in June, there doesn't seem to be a day when ice cream is entirely out of the question.

- The mean temperature in Oahu remains in the low 70s for both December and June.

- The lower quartile of temperatures in December is just below 70F. This is still plenty warm enough to sell ice cream.

here is the data:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>june_temps</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1700.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>74.944118</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.257417</td>
    </tr>
    <tr>
      <th>min</th>
      <td>64.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>73.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>75.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>77.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>85.000000</td>
    </tr>
  </tbody>
</table>


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dec_temps</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1517.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>71.041529</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.745920</td>
    </tr>
    <tr>
      <th>min</th>
      <td>56.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>69.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>71.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>74.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>83.000000</td>
    </tr>
  </tbody>
</table>


---

## Summary

The data show that June and December in Oahu do not have meaningfully different temperatures for the most part. Perfect temperature persists pretty much all year round in Oahu seeing as the mean temperatures hover around the low 70s all year long. Apart from temperature I would probably add another measure for percipitation to see which months might be less optimal for icecream sales. 
