import requests
from requests_oauthlib import OAuth1
import argparse
import urllib.request,json
import datetime
import requests
import os
import pandas as pd

uauth = OAuth1('CQ0SBNGlDITRbkw2PM84Ug', '7RVaHKptMjqId0CaOSIS_5mnW84',
                  'WmOCoc8PHkdfsDOWv7vnVD2fiOTkstxO', '_yYDR4Kh2qq0tsup11JfS9xzxqU')

ua=OAuth1('WmOCoc8PHkdfsDOWv7vnVD2fiOTkstxO')

#requests.get('https://api.yelp.com/oauth2/token',auth=uauth).json()

#Getting bearer token
data = urllib.parse.urlencode({
'client_id' : '92p07_JjKyriZTQxAXRiKQ',
'client_secret': 'xJgWoUoy6Y3tGvykSYpi1EmndMnp0Z6TjNiUdhema3e2fyKnXFiOEbiVfhkvIiRA',
        'grant_type'  : 'client_credentials',
})
headers = {
     'content-type': 'application/x-www-form-urlencoded',
 }
response = requests.request('POST', 'https://api.yelp.com/oauth2/token', data=data, headers=headers)
bearer_token = response.json()['access_token']

#Token
headers = {
       'Authorization': 'Bearer %s' % bearer_token
}

print('Enter City Name and category separated by space')
parser = argparse.ArgumentParser()
parser.add_argument("city", help="City Name",
                    type=str)
parser.add_argument("category", help="category - Hotels, Restaurants or attractions",
                    type=str)


args = parser.parse_args()
searchh=args.category.lower()
v=['hotels','restaurants','attractions']
if(searchh not in v):
    parser.error('Category must be hotels,restaurants or attractions')

cityy=args.city
categoryy=args.category


requestdata=[]
offset=40
data=[]
dataid=[]
businessdata=[]
#Getting data using request api
term=categoryy
location=cityy
print('Fetching your search term data and business data from the API.....')
for i in range(1,9):
    requestdata.append(requests.get('https://api.yelp.com/v2/search?term='+term+'&location='+location+'&limit=40&offset='+str(offset),auth=uauth,headers=headers).json())
    offset=offset+40

#All the data is stored in single lists (equal to number of times loop is run) - Now putting each element in a list   
for i in range(len(requestdata)):
    for j in range(len(requestdata[i]['businesses'])):
           data.append(requestdata[i]['businesses'][j])

#The data we have is sufficient but this does not have all parameters pertaining to a restaurant or hotel etc.
#We need to get the id of the business and send it to the business request api to get complete data of business
for i in range(len(data)):
    dataid.append(data[i]['id'])

#Here, we fetch the the json file for each business (it has all the parameters)
for i in range(len(dataid)):
    businessdata.append(requests.get('https://api.yelp.com/v3/businesses/'+dataid[i],headers=headers).json())


#Appending search term to json object
for i in range(len(businessdata)):
    businessdata[i]['term']=term

print('Storing the data we got from Yelp API in the appropriate folders.....')
#Storing the data in the appropriate folder
import json
import os
foldername=term
directory='Yelp Data'

for i in range(len(businessdata)):
    if 'location' in businessdata[i].keys():
        if not os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])):
            os.makedirs(directory+'\\'+str(businessdata[i]['location']['country']))
            if not os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])):
                os.makedirs(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state']))
                if not os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])):
                    os.makedirs(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city']))
                    if not os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term)):
                        os.makedirs(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term))
                        with open(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term)+'\\'+businessdata[i]['id']+'.json', 'w') as outfile:
                            json.dump(businessdata[i], outfile)
        elif os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])):
            if not os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])):
                os.makedirs(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state']))
                if not os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])):
                    os.makedirs(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city']))
                    if not os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term)):
                        os.makedirs(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term))
                        with open(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term)+'\\'+businessdata[i]['id']+'.json', 'w') as outfile:
                            json.dump(businessdata[i], outfile)
            elif os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])):
                if not os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])):
                    os.makedirs(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city']))
                    if not os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term)):
                        os.makedirs(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term))
                        with open(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term)+'\\'+businessdata[i]['id']+'.json', 'w') as outfile:
                            json.dump(businessdata[i], outfile)
                elif os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])):
                    if not os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term)):
                        os.makedirs(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term))
                        with open(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term)+'\\'+businessdata[i]['id']+'.json', 'w') as outfile:
                            json.dump(businessdata[i], outfile)
                    elif os.path.exists(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term)):
                         with open(directory+'\\'+str(businessdata[i]['location']['country'])+'\\'+str(businessdata[i]['location']['state'])+'\\'+str(businessdata[i]['location']['city'])+'\\'+str(term)+'\\'+businessdata[i]['id']+'.json', 'w') as outfile:
                            json.dump(businessdata[i], outfile)

print('Now we are going to get the population data in the city from where we fetched Yelp data - This is a different API')
#Request to get population data for cities based on the city data gathered
h={
    'X-FullContact-APIKey': '67d9b059fd8d95ae'
    }
city=[]
for i in range(len(businessdata)):
    city.append(businessdata[i]['location']['city']) 
   
cityunique=[]
cityunique=list(set(city))

#Population data request
print('Fetching the population data from FullContact API')
popdata=[]
for i in range(len(cityunique)):
    popdata.append(requests.get('http://api.fullcontact.com/v2/address/locationEnrichment.json?place='+cityunique[i],headers=h).json())

populationdata=[]
for i in range(len(popdata)):
    if 'locations' in popdata[i].keys():
            for j in range(len(popdata[i]['locations'])):
                if 'city' in popdata[i]['locations'][j].keys() and 'name' in popdata[i]['locations'][j]['state'].keys():
                    populationdata.append(popdata[i]['locations'][j])

print('Storing the population data for each cities in the respective folders')
populationdirectory='Population Data'
for i in range(len(populationdata)):
    if not os.path.exists(populationdirectory+'\\'+str(populationdata[i]['country']['code'])):
        os.makedirs(populationdirectory+'\\'+str(populationdata[i]['country']['code']))
        with open(populationdirectory+'\\'+str(populationdata[i]['country']['code'])+'\\'+str(populationdata[i]['city'])+'-'+str(populationdata[i]['state']['name'])+'-'+populationdata[i]['country']['code']+'.json', 'w') as outfile:
            json.dump(populationdata[i], outfile)
    elif os.path.exists(populationdirectory+'\\'+str(populationdata[i]['country']['code'])):
        with open(populationdirectory+'\\'+str(populationdata[i]['country']['code'])+'\\'+str(populationdata[i]['city'])+'-'+str(populationdata[i]['state']['name'])+'-'+populationdata[i]['country']['code']+'.json', 'w') as outfile:
            json.dump(populationdata[i], outfile)


print('Now, writing the Yelp data we have to a CSV file')
#Writing data to a csv
import os
import json
#import sys
#from imp import reload
#reload(sys)
#sys.setdefaultencoding('UTF-8')

mrow=[]
mrow.append('id,name,review_count,price,is_closed,latitude,longitude,city,state,zip_code,country,rating,phone,place_category\n')
path='Yelp Data'
datapath = [os.path.join(root, name)
            for root, dirs, files in os.walk(path)
            for name in files
            if name.endswith((".json", ".jsons"))]

data=[]
for js in datapath:
    with open(js) as json_file:
        data.append(json.load(json_file))
for i in range(len(data)):
    if data[i].get("price",'none')!='none':
        mrow.append(str(data[i]['id'])+','+str(data[i]['name'].replace(',',';'))+','+str(data[i]['review_count'])+','+str(data[i]['price'])+','+str(data[i]['is_closed'])+','+str(data[i]['coordinates']['latitude'])+','+str(data[i]['coordinates']['longitude'])+','+str(data[i]['location']['city'])+','+str(data[i]['location']['state'])+','+str(data[i]['location']['zip_code'])+','+str(data[i]['location']['country'])+','+str(data[i]['rating'])+','+str(data[i]['phone'])+','+str(data[i]['term'])+'\n')
    else:
        mrow.append(str(data[i]['id'])+','+str(data[i]['name'].replace(',',';'))+','+str(data[i]['review_count'])+','+str('N/A')+','+str(data[i]['is_closed'])+','+str(data[i]['coordinates']['latitude'])+','+str(data[i]['coordinates']['longitude'])+','+str(data[i]['location']['city'])+','+str(data[i]['location']['state'])+','+str(data[i]['location']['zip_code'])+','+str(data[i]['location']['country'])+','+str(data[i]['rating'])+','+str(data[i]['phone'])+','+str(data[i]['term'])+'\n')

import csv
#import unicode_literals
with open('Other Files\\YelpData.csv', 'w',encoding='utf-8') as csv_file:
    for a in mrow:
        csv_file.write(a)

print('Now that Yelp data is in a CSV, we are writing the population data to a CSV')
#Population data - Write to csv
rowdata=[]
rowdata.append('city,population,state_code,state_name,country_code,country_name\n')
path='Population Data'
datapathpop = [os.path.join(root, name)
            for root, dirs, files in os.walk(path)
            for name in files
            if name.endswith((".json", ".jsons"))]

datapopulation=[]
for js in datapathpop:
    with open(js) as json_file:
        datapopulation.append(json.load(json_file))

for i in range(len(datapopulation)):
    if datapopulation[i]['state'].get("code",'none')!='none':
        rowdata.append(str(datapopulation[i]['city'])+','+str(datapopulation[i]['population'])+','+str(datapopulation[i]['state']['code'])+','+str(datapopulation[i]['state']['name'])+','+str(datapopulation[i]['country']['code'])+','+str(datapopulation[i]['country']['name'])+'\n')
    else:
        rowdata.append(str(datapopulation[i]['city'])+','+str(datapopulation[i]['population'])+','+str('N/A')+','+str(datapopulation[i]['state']['name'])+','+str(datapopulation[i]['country']['code'])+','+str(datapopulation[i]['country']['name'])+'\n')

#import unicode_literals
with open('Other Files\\PopulationData.csv', 'w',encoding='utf-8') as csv_file:
    for a in rowdata:
        csv_file.write(a)

print('Unfortunately, for Australia, our data does not have state abbreviations..')
print('Now, country data with abbreviations')
#Joining Australia Abbreviation Codes
#joining population and australia data
df1=pd.read_csv("Other Files\\PopulationData.csv")
df2=pd.read_csv("Other Files\\states_australia.csv")
#print(df1.head())
#print(df2.head())
df3=pd.merge(df1,df2,how='left', left_on=['state_name'],right_on=['State'])
##df3[(df3['state_code'].isnull())]['state_code']
#df3[(df3['state_code'].isnull())]['Abbreviation']
df3.state_code.fillna(df3.Abbreviation, inplace=True)
print('Writing the joined data to a CSV')
df3.to_csv("Other Files\\CountryJoinedData.csv")

print('Now we have the Yelp Data and population data.Its the time to join both')
import pandas as pd
yelpdata=pd.read_csv("Other Files\\YelpData.csv")
countrydata=pd.read_csv("Other Files\\CountryJoinedData.csv")
#concatenating column to form keys to join
yelpdata['JoinColumn']=yelpdata['city']+yelpdata['state']+yelpdata['country']
countrydata['JoinColumn']=countrydata['city']+countrydata['state_code']+countrydata['country_code']
print('Filtering only US and AU since i need to join on keys(keys here are formed by concatenating three columns(since in US same city name in multiple states))')
yelpdataw=yelpdata[(yelpdata['country']=='AU') | (yelpdata['country']=='US') ]
tempor=pd.merge(yelpdataw,countrydata,how='left', left_on=['JoinColumn'],right_on=['JoinColumn'])
print('For other countries, using the city and country code as keys')
yelpdataww=yelpdata[(yelpdata['country']!= 'US')& (yelpdata['country']!= 'AU')]
yelpdataww['JoinColumn']=yelpdataww['city']+yelpdataww['country']
countrydata2=countrydata
countrydata2['JoinColumn']=countrydata2['city']+countrydata2['country_code']
tempor2=pd.merge(yelpdataww,countrydata2,how='left', left_on=['JoinColumn'],right_on=['JoinColumn'])
print('Appending all the dataframes.......')
newdataframe=tempor.append(tempor2)
processed=newdataframe[['id','name','review_count','price','is_closed','latitude','longitude','city_x','state','zip_code','country','rating','phone','place_category','population']]
processed['Price Rating']=processed['price'].str.len()
print('The processed data has been written to a CSV')
processed.to_csv("Other Files\\ProcessedData.csv", encoding='utf-8')

# Timings data
#Timings data
import os
import json
#import sys
#from imp import reload
#reload(sys)
#sys.setdefaultencoding('UTF-8')

print('Restaurant timings data are in dictionaries... Data is there for each day of the week')
print('Hence, I am writing this to a separate CSV from which I can get timing data by joining files based on id')
path='Yelp Data'
datapath = [os.path.join(root, name)
            for root, dirs, files in os.walk(path)
            for name in files
            if name.endswith((".json", ".jsons"))]

datatiming=[]
for js in datapath:
    with open(js) as json_file:
        datatiming.append(json.load(json_file))

rowtiming=[]
rowtiming.append('id,city,county,day,start,end,overnight\n')
for i in range(len(datatiming)):
    idval=datatiming[i]['id']
    city=datatiming[i]['location']['city']
    country=datatiming[i]['location']['country']
    if 'hours' in datatiming[i].keys():
            for j in range(len(datatiming[i]['hours'][0]['open'])):
                    day=datatiming[i]['hours'][0]['open'][j]['day']
                    start=datatiming[i]['hours'][0]['open'][j]['start']
                    end=datatiming[i]['hours'][0]['open'][j]['end']
                    overnight=datatiming[i]['hours'][0]['open'][j]['is_overnight']
                    rowtiming.append(str(idval)+','+str(city)+','+str(country)+','+str(day)+','+str(start)+','+str(end)+','+str(overnight)+'\n')

with open('Other Files\\RestaurantTiming.csv', 'w',encoding='utf-8') as csv_file:
    for a in rowtiming:
        csv_file.write(a)

print('Similarly, each business is associated with multiple categories. Saving the category data to a CSV')
#categories data write
import os
import json
path='Yelp Data'
datapath = [os.path.join(root, name)
            for root, dirs, files in os.walk(path)
            for name in files
            if name.endswith((".json", ".jsons"))]

datacategory=[]
for js in datapath:
    with open(js) as json_file:
        datacategory.append(json.load(json_file))

#Writing to csv
rowcategory=[]
rowcategory.append('id,title,alias\n')
for i in range(len(datacategory)):
    idval=datacategory[i]['id']
    if 'categories' in datacategory[i].keys():
            for j in range(len(datacategory[i]['categories'])):
                    title=datacategory[i]['categories'][j]['title'].replace(',','')
                    alias=datacategory[i]['categories'][j]['alias'].replace(',','')
                    rowcategory.append(str(idval)+','+str(title)+','+str(alias)+'\n')

with open('Other Files\\RestaurantCategory.csv', 'w',encoding='utf-8') as csv_file:
    for a in rowcategory:
        csv_file.write(a)


                    

