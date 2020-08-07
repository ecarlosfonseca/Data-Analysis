import pandas as pd
import numpy as np
import seaborn as sns
from itertools import tee

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl

url = 'https://raw.githubusercontent.com/ecarlosfonseca/DataSets/master/trade-indicators-for-portugal-1.csv'

data = pd.read_csv(url, usecols=[2, 3, 5], skiprows=2, names=['year', 'kpi', 'value'],
                   dtype={0: 'int64', 4: object, 6: float}, index_col=0, chunksize=100)

data1, data2 = tee(data)


def filter_indicator(df, indicator):
    return df.loc[df['kpi'] == indicator, :]


chunk_arr = []
for chunk in data1:
    data_chunk_filtered = filter_indicator(chunk, 'Agricultural raw materials exports (% of merchandise exports)')
    chunk_arr.append(data_chunk_filtered)

df1 = pd.concat(chunk_arr, axis=0)

df1.plot()
plt.show()


chunk_arr2 = []
for chunk in data2:
    chunk_arr2.append(chunk)
df2 = pd.concat(chunk_arr2, axis=0)
df2 = df2.reset_index()

df2 = df2.pivot(index='year', columns='kpi')['value']
print(df2.head())
df2.plot()
plt.show()

corr_matrix = df2.corr()
lower_triangle_mask = np.triu(np.ones(corr_matrix.shape)).astype(np.bool)
cor_mat_lower = corr_matrix.mask(lower_triangle_mask)

sns.heatmap(cor_mat_lower,
            annot=False,
            cmap='RdBu_r')

plt.show()


