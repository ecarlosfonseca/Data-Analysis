import pandas as pd
import requests
import json


url = 'https://api.punkapi.com/v2/beers'

# Getting all beers
parameters = {'page': 1, 'per_page': 80}
response = requests.get(url, params=parameters)
beers = response.json()
while response.json():
    parameters['page'] += 1
    response = requests.get(url, params=parameters)
    beers += response.json()

beers_df = pd.DataFrame(beers).reset_index(drop=True).set_index('id')

# beers_df.to_csv("Pukapi_beers.csv")
# beers_df = pd.read_csv('Pukapi_beers.csv')

analysis_dict = {'variables': list(beers_df.columns.values),
                 'count': list(beers_df.count().values),
                 'v_types': list(beers_df.dtypes.values),
                 'n_null': list(beers_df.isnull().sum().values),
                 'n_uniques': list(beers_df.nunique().values)}

analysis = pd.DataFrame(analysis_dict)
print(analysis)

