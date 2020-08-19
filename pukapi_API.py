import pandas as pd
import requests
import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#  Getting all beers data from the API
url = 'https://api.punkapi.com/v2/beers'

parameters = {'page': 1, 'per_page': 80}
response = requests.get(url, params=parameters)
beers = response.json()
while response.json():
    parameters['page'] += 1
    response = requests.get(url, params=parameters)
    beers += response.json()

beers_df = pd.DataFrame(beers).reset_index(drop=True).set_index('id')

#beers_df.to_csv("Pukapi_beers.csv")
#beers_df = pd.read_csv('Pukapi_API/Pukapi_beers.csv')

#  EDA
beers_df['first_brewed'] = pd.to_datetime(beers_df['first_brewed'], infer_datetime_format=True)

analysis_dict = {'variables': list(beers_df.columns.values),
                 'count': list(beers_df.count().values),
                 'v_types': list(beers_df.dtypes.values),
                 'n_null': list(beers_df.isnull().sum().values),
                 'n_uniques': list(beers_df.nunique().values)}

analysis = pd.DataFrame(analysis_dict)
print(analysis)

corr_matrix = beers_df.corr()
lower_triangle_mask = np.triu(np.ones(corr_matrix.shape)).astype(np.bool)
cor_mat_lower = corr_matrix.mask(lower_triangle_mask)

sns.heatmap(cor_mat_lower,
            annot=True,
            cmap='RdBu_r')

plt.show()

