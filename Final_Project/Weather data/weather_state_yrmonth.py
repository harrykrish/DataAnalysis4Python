import pandas as pd
wdf=pd.read_csv('Weather_monthly.csv')
#wsdf=pd.read_csv('weather_station.csv')
cols = pd.read_csv('weatherstation.csv', nrows=1).columns
wsdf = pd.read_csv('weatherstation.csv', usecols=cols)
#print(len(wsdf))
wsdf=wsdf[['WBAN','Name','State']]
#wsdf.head(5)
#len(wsdf)
wsdf=wsdf.drop_duplicates()
wdf=wdf.merge(wsdf, left_on=['WBAN'], right_on=['WBAN'], how='outer')
wdf=wdf[['YearMonth','Name','State','AvgTemp']]
wdf=wdf.drop_duplicates()
wdf.to_csv('weather_state_yrmonth.csv')
