import requests
from requests_oauthlib import OAuth1
import argparse
import urllib.request,json
import datetime
import requests
import os
import csv


parser = argparse.ArgumentParser()
parser.add_argument("searchterm", type=str,nargs='+',
                    help="Enter the two queries to be compared")
args = parser.parse_args()
query = args.searchterm
print(query)
path='C:\\Users\\harikrishna\\Documents\\Tweets'
jj = [os.path.join(root, name)
             for root, dirs, files in os.walk(path)
             for name in files
             if name.endswith((".json", ".jsons"))]

filedata=[]
for js in jj:
    with open(os.path.join(path, js)) as json_file:
        filedata.append(json.load(json_file))


#All states with place name
location={}
count=1
state={}
for i in range(len(filedata)):
    if(('location') in filedata[i]['user']):
        if(filedata[i]['user']['location']!=''):
            loc=filedata[i]['user']['location']
            
            if(loc not in location.keys()):
                location[filedata[i]['user']['location']]=1
            else:
                location[filedata[i]['user']['location']]+=1

#State wise distribution
location={}
count=1
state={}
for i in range(len(filedata)):
    if(('location') in filedata[i]['user']):
        if(filedata[i]['user']['location']!=''):
            loc=filedata[i]['user']['location']
            if(', ' in loc):
                if type(loc) == str:
                    loc=loc.split(", ",1)[1]            
                    if(len(loc)==2 or len(loc)==3):
                        if(loc not in state.keys()):
                            state[loc]=1
                        else:
                            state[loc]+=1
print(state)
import csv
with open('C:\\Users\harikrishna\\Desktop\\county22.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["city", "tweet"])
    for key, value in state.items():
        writer.writerow([key, value])  

#Time wise tweet generation (all tweets)
import time
import month
import datetime
from datetime import datetime
import calendar
import pytz
timewise={'morning':0,'afternoon':0,'evening':0,'night':0}
for i in range(len(filedata)):
    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(filedata[i]['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
    dt2 = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
    hour2=dt2.hour
    if(filedata[i]['created_at']!=''):
                if(hour2>=0 and hour2<12):
                    if('morning' not in timewise.keys()):
                        timewise['morning']=1
                    else:
                        timewise['morning']+=1
                elif(hour2>=12 and hour2<16):
                    if('afternoon' not in timewise.keys()):
                        timewise['afternoon']=1
                    else:
                        timewise['afternoon']+=1
                elif(hour2>=16 and hour2<21):
                    if('evening' not in timewise.keys()):
                        timewise['evening']=1
                    else:
                        timewise['evening']+=1            
                elif(hour2>=21 and hour2<=23):
                    if('night' not in timewise.keys()):
                        timewise['night']=1
                    else:
                        timewise['night']+=1
print(timewise)
import csv
with open('C:\\Users\harikrishna\\Desktop\\timewise.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Time of Day", "Number of Tweets"])
    for key, value in timewise.items():
        writer.writerow([key, value])
       
#Maximum retweeted tweet for each query term
separatei=query
mydictt2={}
for i in range(len(separatei)):
    q=separatei[i]
    for i in range(len(filedata)):
        if(filedata[i]['query']==q):
            if(q in mydictt2.keys()):
                
                if(filedata[i]['retweet_count']>mydictt2[q]['maxcount']):
                    mydictt2[q]['maxcount']=filedata[i]['retweet_count']
                    mydictt2[q]['text']=filedata[i]['text']
            else:
                mydictt2[q]={}
                mydictt2[q]['maxcount']=filedata[i]['retweet_count']
                mydictt2[q]['text']=filedata[i]['text']

import csv
re=[]
for key,value in mydictt2.items():
       # print(key)
        a=key
        f=value
        for key,values in f.items():
            b=key
            c=f[key]
            j=[a,b,c]
            re.append(j)
            #print(hh)
            
            
with open('C:\\Users\harikrishna\\Desktop\\retweet.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["name", "category","value"])            
    for i in range(len(re)):
        writer.writerow([re[i][0],re[i][1],re[i][2]])


#Maximum friends for each query search term
separate=query
userss={}
for i in range(len(separate)):
    q=separate[i]
    for i in range(len(filedata)):
        if(filedata[i]['query']==q):
            if(q in userss.keys()):
                userss[q]['friendscount']+=filedata[i]['user']['friends_count']
            else:
                
                userss[q]={}
                userss[q]['friendscount']=filedata[i]['user']['friends_count']

print(userss)
users2=[]
for key,value in userss.items():
        print(key)
        a=key
        f=value
        for key,values in f.items():
            b=key
            c=f[key]
            j=[a,b,c]
            users2.append(j)
            
with open('C:\\Users\harikrishna\\Desktop\\friendscount.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["name", "category","total count"])            
    for i in range(len(users2)):
        writer.writerow([users2[i][0],users2[i][1],users2[i][2]])
#Month wise tweets for each search term
import time
import month
import datetime
from datetime import datetime
import calendar
monthwise={}
monthwise={}
#inputquery='hillary,trump'
separatedvalues=query
for i in range(len(separatedvalues)):
    q=separatedvalues[i]
    for i in range(len(filedata)):
        if(filedata[i]['query']==q):
            if(q in monthwise.keys()):
                ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(filedata[i]['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
                dt2 = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
                m=dt2.month
                y=dt2.year
                mo=calendar.month_name[m]
                ye=str(y)
                moyear=mo+'_'+ye
                if(filedata[i]['created_at']!=''):
                    if(moyear in monthwise[q].keys()):   
                        monthwise[q][moyear]+=1
                    else:
                        monthwise[q][moyear]=2
                        
            else:
                monthwise[q]={}
        
                
print(monthwise)
import csv
hh=[]
for key,value in monthwise.items():
        print(key)
        a=key
        f=value
        for key,values in f.items():
            b=key
            c=f[key]
            j=[a,b,c]
            hh.append(j)
            
with open('C:\\Users\harikrishna\\Desktop\\monthwise.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["name", "month","tweets"])            
    for i in range(len(hh)):
        writer.writerow([hh[i][0],hh[i][1],hh[i][2]])


#Determining the query for user with maximum followers and friends
user={}
for i in range(len(filedata)):
    if('highest' in user.keys()):
        if(filedata[i]['user']['followers_count']>user['highest']['followers']):
            
            user['highest']['followers']=filedata[i]['user']['followers_count']
            user['highest']['friends']=filedata[i]['user']['friends_count']
            user['highest']['query']=filedata[i]['query']
            user['highest']['id']=filedata[i]['user']['id']
    else:
        print(filedata[i]['user']['followers_count'])
        user['highest']={}
        user['highest']['followers']=filedata[i]['user']['followers_count']
        user['highest']['friends']=filedata[i]['user']['friends_count']
        user['highest']['query']=filedata[i]['query']
        user['highest']['id']=filedata[i]['user']['id']

import csv
cc=[]
for key,value in user.items():
        print(key)
        a=key
        f=value
        for key,values in f.items():
            b=key
            c=f[key]
            j=[a,b,c]
            cc.append(j)
            
with open('C:\\Users\harikrishna\\Desktop\\usermax.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["category", "category","tweets"])            
    for i in range(len(cc)):
        writer.writerow([cc[i][0],cc[i][1],cc[i][2]])
