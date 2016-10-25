import requests
from requests_oauthlib import OAuth1
import argparse
import urllib.request,json
import datetime
import requests
import os
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
uauth = OAuth1('KQ7qB2uzSt90TXmzl7lfqiLL6', 'Vq8hIoUld8Yaeq2IfrvmEJKW8L8GgX4b8FKFsfPKaFTwZJQU50',
                  '548315766-cYHndHExgRtTyFBwkq9MG0QmsG9IhdMnmanyndFy', 'Zz1oqVWzzxpQDYv76ahPDmnUerb4GWA2bL3u7pZj0vFYb')
rq=requests.get(url, auth=uauth)
print(rq)
parser = argparse.ArgumentParser()
parser.add_argument("searchterm", type=str, 
                    help="display a square of a given number")
args = parser.parse_args()
query = args.searchterm
m={}
u=[]
u.append(requests.get('https://api.twitter.com/1.1/search/tweets.json?q='+query+'&count=30',auth=uauth).json())
dt=str(datetime.date.today()).replace('-','')
directory='C:\\Users\\harikrishna\\Documents\\Tweets'
if not os.path.exists(directory+'\\'+str(query)):
    os.makedirs(directory+'\\'+str(query))
    if not os.path.exists(directory+'\\'+str(query)+'\\'+dt):
        os.makedirs(directory+'\\'+str(query)+'\\'+str(dt))

mydict={}
for i in range(len(u[0]['statuses'])):
    u[0]['statuses'][i]['query']=query
    userid=str(u[0]['statuses'][i]['user']['id'])
    useridd=userid+'_'
    created=u[0]['statuses'][i]['created_at']
    for ch in [' ','+','0000',':']:
        if ch in created:
            created=created.replace(ch,"")
    created=created.replace(created[0:3],"")
    jsonid=useridd+created
    mydict[jsonid]=u[0]['statuses'][i]


mykeys=[key for key,value in mydict.items()]
for i in range(len(mydict)):
    with open('C:\\Users\\harikrishna\\Documents\\Tweets'+'\\'+str(query)+'\\'+str(dt)+'\\'+mykeys[i]+'.json', 'w') as outfile:
        json.dump(mydict[mykeys[i]], outfile)


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


