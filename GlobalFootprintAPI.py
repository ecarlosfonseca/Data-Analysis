import requests
from requests.auth import HTTPBasicAuth

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

base_url = 'http://api.footprintnetwork.org/v1/'

# Making a get request for all years in the df
response = requests.get(base_url + 'years',
                        auth=HTTPBasicAuth('CarlosFonseca', 'XXXX'))

# Making df with years
years_df = pd.DataFrame(response.json()).set_index('id').drop(columns=['version'])

# Making df with all countries for 1st year
response = requests.get(base_url + 'data/all/' + str(years_df.values[0][0]),
                        auth=HTTPBasicAuth('CarlosFonseca', 'XXXXX'))

countries_df = pd.DataFrame(response.json()).set_index('id')

# Getting all remaining years values and adding them to the df
for year in years_df.values:
    print(str(year[0]))
    response = requests.get(base_url + 'data/all/' + str(year[0]),
                            auth=HTTPBasicAuth('CarlosFonseca', '168O0I4p30qa2sgMkAbu20rLv1Hjqu557G6hhtdf6445bO8a9j9M'))

    print(response)
    aux_df = pd.DataFrame(response.json()).set_index('id')
    countries_df = pd.concat([countries_df, aux_df], axis=0, ignore_index=True)

print(countries_df.shape)

#countries_df.to_csv("footprintnetwork.csv")
#countries_df = pd.read_csv('GlobalfootprintAPI/footprintnetwork.csv').drop(columns=['Unnamed: 0', 'version'])

print(countries_df.head())
analysis_dict = {'variables': list(countries_df.columns.values),
                 'count': list(countries_df.count().values),
                 'v_types': list(countries_df.dtypes.values),
                 'n_null': list(countries_df.isnull().sum().values),
                 'n_uniques': list(countries_df.nunique().values)}

analysis = pd.DataFrame(analysis_dict)
print(analysis)

portugal_land_type_df = countries_df[countries_df['countryName'] == 'Brazil'].\
    drop(columns=['countryCode', 'countryName', 'shortName', 'isoa2', 'record', 'fishingGround', 'builtupLand',
                  'carbon', 'value', 'score']).set_index('year')

sns.lineplot(data=portugal_land_type_df, ci=None, legend='brief')
plt.show()


