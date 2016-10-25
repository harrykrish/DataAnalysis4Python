import requests
from requests_oauthlib import OAuth1
import argparse
import urllib.request,json
import datetime
import requests
import os


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
        
#Maximum retweeted tweet for each query term
separate=query
mydictt={}
for i in range(len(separate)):
    q=separate[i]
    for i in range(len(filedata)):
        if(filedata[i]['query']==q):
            if(q in mydictt.keys()):
                
                if(filedata[i]['retweet_count']>mydictt[q]['maxcount']):
                    mydictt[q]['maxcount']=filedata[i]['retweet_count']
                    mydictt[q]['text']=filedata[i]['text']
            else:
                mydictt[q]={}
                mydictt[q]['maxcount']=filedata[i]['retweet_count']
                mydictt[q]['text']=filedata[i]['text']

print(mydictt)
