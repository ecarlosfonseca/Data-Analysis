import pandas as pd
import numpy as np
from itertools import tee

import matplotlib.pyplot as plt



#filename = "vgsales.csv"
url = 'https://raw.githubusercontent.com/ecarlosfonseca/DataSets/master/vgsales.csv'

data = pd.read_csv(url, index_col=0, chunksize=99)

data1, data2 = tee(data)

"""
print(data.shape)
    (16598, 10)
print(data.columns) 
    Index(['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales',
        'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'],
        dtype='object')
print(data.dtypes)
    Name             object
    Platform         object
    Year            float64
    Genre            object
    Publisher        object
    NA_Sales        float64
    EU_Sales        float64
    JP_Sales        float64
    Other_Sales     float64
    Global_Sales    float64
print(data.isnull().sum())
    Name              0
    Platform          0
    Year            271
    Genre             0
    Publisher        58
    NA_Sales          0
    EU_Sales          0
    JP_Sales          0
    Other_Sales       0
    Global_Sales      0
    dtype: int64
print(data.head())
                             Name Platform  ...  Other_Sales Global_Sales
    Rank                                     ...                          
    1                   Wii Sports      Wii  ...         8.46        82.74
    2            Super Mario Bros.      NES  ...         0.77        40.24
    3               Mario Kart Wii      Wii  ...         3.31        35.82
    4            Wii Sports Resort      Wii  ...         2.96        33.00
    5     Pokemon Red/Pokemon Blue       GB  ...         1.00        31.37
"""

chunk_arr1 = []
for chunk in data1:
    data_chunk_filtered = chunk[['Name', 'EU_Sales', 'JP_Sales']]
    chunk_arr1.append(data_chunk_filtered)
df1 = pd.concat(chunk_arr1, axis=0)
df1 = df1.reset_index(drop=True).set_index('Name')

df1.plot()
plt.show()

chunk_arr2 = {}
for chunk in data2:
    chunk = chunk[['Year', 'EU_Sales', 'JP_Sales', 'NA_Sales']].dropna().reset_index(drop=True).set_index('Year')
    for year in chunk.index.unique():
        if year not in chunk_arr2:
            chunk_arr2[year] = {'EU_Sales': 0,
                                'JP_Sales': 0,
                                'NA_Sales': 0}

        chunk_arr2[year]['EU_Sales'] += chunk.at[year, 'EU_Sales'].sum()
        chunk_arr2[year]['JP_Sales'] += chunk.at[year, 'JP_Sales'].sum()
        chunk_arr2[year]['NA_Sales'] += chunk.at[year, 'NA_Sales'].sum()

df2 = pd.DataFrame.from_dict(chunk_arr2, orient='index').sort_index()
df2.index = df2.index.astype(np.int64)
df2.plot(kind='bar')
plt.show()



