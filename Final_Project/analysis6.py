import requests
import geopandas as gpd
from requests_oauthlib import OAuth1
import argparse
import datetime
import requests
import os
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--c",dest="category", type=str,
                    help="input a category")
parser.add_argument("--v",help="input a country codeusing --c")


args = parser.parse_args()
searchh=args.category.lower()
v=['hotels','restaurants','attractions']
if(searchh not in v):
    parser.error('Category must be hotels,restaurants or attractions')

print(searchh)



data_dff=pd.read_csv(r"Other Files\ProcessedData.csv")
data_dff=data_df[(data_df['place_category']== searchh)]
data_country_group=data_dff.groupby('country',as_index=False)['place_category'].count()
data_country_group.to_csv(r'country_distribution.csv')

df = gpd.read_file(r'Other Files\countries.geojson')

fig, ax = plt.subplots()
ax.set_aspect('equal')
data_country_group['country']=data_country_group['country'].str.replace('AU','Australia')
data_country_group['country']=data_country_group['country'].str.replace('US','United States of America')
data_country_group['country']=data_country_group['country'].str.replace('GB','united Kingdom')
data_country_group['country']=data_country_group['country'].str.replace('FR','France')
data_country_group['country']=data_country_group['country'].str.replace('CA','Canada')
data_country_group['country']=data_country_group['country'].str.replace('NZ','New Zealand')
df=df.merge(data_country_group, left_on=['name'], right_on=['country'], how='inner')


ay=df.plot(ax=ax,column='place_category',  k=5, colormap='OrRd')

print(df)
#ax = plot_dataframe(df, column='imdbRating',  colormap='OrRd', legend=False)
plt.title('Country wise distribution of '+str(searchh),y=1.05)

plt.savefig(r'Output Files\Analysis 6\Plot\country_distribution_category.jpg')
