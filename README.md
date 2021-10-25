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

<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>june_temps</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>1700.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>74.944118</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>3.257417</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>64.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>73.000000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>75.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>77.000000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>85.000000</td>\n    </tr>\n  </tbody>\n</table>


<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>dec_temps</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>1517.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>71.041529</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>3.745920</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>56.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>69.000000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>71.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>74.000000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>83.000000</td>\n    </tr>\n  </tbody>\n</table>


---

## Summary

The data show that June and December in Oahu do not have meaningfully different temperatures for the most part. Perfect temperature persists pretty much all year round in Oahu seeing as the mean temperatures hover around the low 70s all year long. Apart from temperature I would probably add another measure for percipitation to see which months might be less optimal for icecream sales. 