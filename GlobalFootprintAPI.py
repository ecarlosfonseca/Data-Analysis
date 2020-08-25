import requests
from requests.auth import HTTPBasicAuth

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

base_url = 'http://api.footprintnetwork.org/v1/'

# Making a get request for all years in the df
response = requests.get(base_url + 'years',
                        auth=HTTPBasicAuth('CarlosFonseca', 'XXXXX'))

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
                            auth=HTTPBasicAuth('CarlosFonseca', 'XXXXX'))

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

brazil_land_type_df = countries_df.loc[countries_df['countryName'] == 'Brazil', ['year', 'cropLand', 'grazingLand', 'forestLand']].set_index('year')
ax1 = sns.lineplot(data=brazil_land_type_df, ci=None, legend='brief')
ax1.set_title('Brazil ground types areas evolution over the years')
ax1.set_ylabel('Areas (gha)')
ax1.set_xlabel('Years')
plt.show()

fishingGround_df = countries_df.loc[(countries_df['year'] == 2016) & (countries_df['record'] == 'AreaTotHA'), ['countryName', 'fishingGround']].nlargest(40, 'fishingGround')
ax2 = sns.barplot(x='fishingGround', y='countryName', data=fishingGround_df)
ax2.set_title('2016 world top40 fishing ground')
ax2.set_xlabel('Fishing Ground (gha)')
plt.show()

portugal_area_df = countries_df.loc[(countries_df['countryName'] == 'Portugal') & (countries_df['year'] == 2016) & (countries_df['record'] == 'AreaTotHA'), ['cropLand', 'grazingLand', 'forestLand']].T
ax3 = portugal_area_df.plot.pie(y=160552, title='Portugal 2016 ground types area', legend=False)
ax3.set_ylabel('')
plt.show()


