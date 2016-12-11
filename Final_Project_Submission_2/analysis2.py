import argparse
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
parser = argparse.ArgumentParser()
parser.add_argument("--c",dest="city", type=str,
                    help="input a city name")
parser.add_argument("--n",dest="country", type=str,
                    help="input a country name")
parser.add_argument("--v",help="input a city name  using --c and county code using --n")
args = parser.parse_args()
cityname = args.city
countrycode = args.country
if(len(countrycode)!=2):
    parser.error('Enter correct country code my friend!! I already told you!(Two characters AU, US etc)')

testdf=pd.read_csv("Other Files\\RestaurantTiming.csv")
dfpr=pd.read_csv("Other Files\\ProcessedData.csv",encoding='utf-8')
days = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}

testdf['day_of_week'] = testdf['day'].apply(lambda x: days[x])


citylive=cityname
countrylive=countrycode
today=datetime.date.today().strftime('%A')
dfpr2=dfpr[(dfpr['city_x']== citylive)& (dfpr['country']== countrylive)&(dfpr['place_category']== 'restaurants')]
timee=datetime.datetime.now()
hr=timee.hour
minute=timee.minute
if(len(dfpr2)>0):
    #Separating hour and minute, preprocessing the data to make it the right format to split
    testdf['start']=testdf['start'].astype(str)
    testdf['start'] = testdf['start'].apply(lambda x: x.zfill(4))
    testdf['end']=testdf['end'].astype(str)
    testdf['end']=testdf['end'].apply(lambda x: x.zfill(4))
    testdf['start_hour'] = testdf['start'].str[:-2].astype(int)
    testdf['start_min'] = testdf['start'].str[2:]
    testdf['end_hour'] = testdf['end'].str[:-2].astype(int)
    testdf['end_min'] = testdf['end'].str[2:]
    uniqueids=dfpr2['id'].unique()
    df_data=pd.DataFrame()
    for i in range(len(uniqueids)):
        t=testdf[(testdf['id']==uniqueids[i]) & (testdf['day_of_week']==today)]
        df_data=df_data.append(t,ignore_index=True)
    #Logic to check if restaurant is open
    timesdata=pd.DataFrame()
    tem=df_data[(df_data['start_hour']<hr)&(df_data['end_hour']>hr)]
    #else:
    t=df_data[(df_data['start_hour']==df_data['end_hour'])&(df_data['start_min']==df_data['end_min'])]
    q=df_data[(df_data['end_hour']<df_data['start_hour'])&(df_data['end_hour']==0)&(hr>df_data['start_hour'])]
    r=df_data[(df_data['end_hour']<df_data['start_hour'])&(df_data['overnight']==True)&((hr>df_data['start_hour'])|((hr<df_data['end_hour'])))]
    timesdata = pd.concat([tem, t,q,r], axis=0)
    rest=list(timesdata['id'].unique())

    #Restaurant data open during specified time of user request
    reqdata=pd.DataFrame()
    for i in range(len(rest)):
        t=dfpr2[(dfpr2['id']==rest[i])]
        reqdata=reqdata.append(t,ignore_index=True)

    reqdata2=reqdata.sort_values(['rating', 'review_count'], ascending=False)
    reqdata3=reqdata2[0:10]
    reqdata2=reqdata2.ix[:,'id':]
    reqdata2.to_csv(r"Output Files\Analysis 2\CSV Files\restaurants-open.csv",index=False)
    fig = plt.figure() # Create matplotlib figure
    
    ax = fig.add_subplot(111) # Create matplotlib axes
    ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

    width = 0.4

    reqdata3['rating'].plot(kind='bar', color='red', ax=ax, width=width, position=1)
    reqdata3['Price Rating'].plot(kind='bar', color='blue', ax=ax2, width=width, position=0)

    ax.set_ylabel('Restaurant Rating',fontsize=20)
    ax2.set_ylabel('Price Rating',fontsize=20)
    ax2.set_ylabel('Price Rating',fontsize=20)
    ax.set_xlabel('Restaurant Name',fontsize=20)
    ax.set_xticklabels(reqdata3['name'],fontsize=10,rotation=25 )
    ax.set_yticklabels(reqdata3['rating'],fontsize=20 )
    ax2.set_yticklabels(reqdata3['rating'],fontsize=20 )
    fig.suptitle("Restaurants open at "+str(timee.strftime("%Y-%m-%d %H:%M:%S " )+str('in ')+str(citylive)),fontsize=23)
    #fig.tight_layout()
    #plt.subplots_adjust(bottom=0.15)
    plt.savefig(r'Output Files\Analysis 2\Plot\Restaurants-Open.jpg')
    plt.show()
else:
    print('Im sorry The restaurant data is not available for this city')
