import datetime
import json
import requests
import time
from datetime import datetime
import os
m={}
u=[]
#site=stackoverflow
for i in range(1,20):
    u.append(requests.get('http://api.stackexchange.com//2.2/questions?fromdate=1451606400&todate=1477612800&order=desc&sort=activity&page='+str(i)+'&pagesize=100&site=stackoverflow').json())

questiondata=[]
for i in range(len(u)):
    for j in range(len(u[i]['items'])):
           questiondata.append(u[i]['items'][j])

import json
import os
foldername='questions'
directory='StackExchange'
for i in range(len(questiondata)):
    #print(questiondata[0])
    dt=questiondata[i]['creation_date']
    dt2=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dt))
    dt3=dt2[0:10]
    dt4=dt3.replace('-','')
    qid=questiondata[i]['question_id'] 
    jsonid=str(qid)
    if not os.path.exists(directory+'\\'+str(foldername)):
        os.makedirs(directory+'\\'+str(foldername))
        if not os.path.exists(directory+'\\'+str(foldername)+'\\'+dt3):
            os.makedirs(directory+'\\'+str(foldername)+'\\'+str(dt3))
            with open(directory+'\\'+str(foldername)+'\\'+str(dt3)+'\\'+jsonid+'.json', 'w') as outfile:
                json.dump(questiondata[i], outfile)
        else:
            with open(directory+'\\'+str(foldername)+'\\'+str(dt3)+'\\'+jsonid+'.json', 'w') as outfile:
                json.dump(questiondata[i], outfile)
    elif os.path.exists(directory+'\\'+str(foldername)):
        if not os.path.exists(directory+'\\'+str(foldername)+'\\'+dt3):
            os.makedirs(directory+'\\'+str(foldername)+'\\'+str(dt3))
            with open(directory+'\\'+str(foldername)+'\\'+str(dt3)+'\\'+jsonid+'.json', 'w') as outfile:
                json.dump(questiondata[i], outfile)
        else:
            with open(directory+'\\'+str(foldername)+'\\'+str(dt3)+'\\'+jsonid+'.json', 'w') as outfile:
                json.dump(questiondata[i], outfile)


ansids=[]
for i in range(len(questiondata)):
    if('accepted_answer_id' in questiondata[i]):
        ansid=''
        ansid=str(questiondata[i]['accepted_answer_id'])
        ansids.append(ansid)

#Splitting each 100
answeridd=[]
answeriddstring=[]
answeridd=[ansids[i:i+100] for i in range(0, len(ansids), 100)]   
for i in range(len(answeridd)):
    stringp=''
    count=0
    for j in range(len(answeridd[i])):
            leng=len(answeridd[i])-1
            if(j==leng):
                stringp=stringp+str(answeridd[i][j])
            else:
                stringp=stringp+str(answeridd[i][j])+';'
    answeriddstring.append(stringp)

answerlink=[]
for i in range(len(answeriddstring)):
    answerlink.append(requests.get('http://api.stackexchange.com//2.2/answers/'+answeriddstring[i]+'?order=desc&sort=activity&pagesize=100&site=stackoverflow&filter=!-*f(6t0VjPb5').json())
    answerdata=[]
    for i in range(len(answerlink)):
        for j in range(len(answerlink[i]['items'])):
               answerdata.append(answerlink[i]['items'][j])

#answerdataa
link='http://api.stackexchange.com//2.2/answers/'+answeriddstring[0]+'?order=desc&sort=activity&pagesize=100&site=stackoverflow&filter=!-*f(6sCNvG6L'
st='http://api.stackexchange.com//2.2/'
e='/'
folderans=link.split(st)[-1].split(e)[0]
import json
import os
directory='StackExchange'
for i in range(len(answerdata)):
    #print(questiondata[0])
    aid=answerdata[i]['answer_id']
    #jsonid=str(qid)
    if not os.path.exists(directory+'\\'+str(folderans)):
        os.makedirs(directory+'\\'+str(folderans))
        with open(directory+'\\'+str(folderans)+'\\'+str(aid)+'.json', 'w') as outfile:
                json.dump(answerdata[i], outfile)
    elif os.path.exists(directory+'\\'+str(folderans)):
            with open(directory+'\\'+str(folderans)+'\\'+str(aid)+'.json', 'w') as outfile:
                json.dump(answerdata[i], outfile)

#userids
userid=[]
for i in range(len(questiondata)):
    if('user_id'in questiondata[i]['owner'].keys()):
        us=questiondata[0]['owner']['user_id']  
        userid.append(us)
        
#useridd dividing for data
useridd=[]
useriddstring=[]
#for i in range(len(userid)):
useridd=[userid[i:i+100] for i in range(0, len(userid), 100)]   
for i in range(len(useridd)):
    stringp=''
    count=0
    for j in range(len(useridd[i])):
            leng=len(useridd[i])-1
            if(j==leng):
                stringp=stringp+str(useridd[i][j])
            else:
                stringp=stringp+str(useridd[i][j])+';'
    useriddstring.append(stringp)

ll=[]
for i in range(len(useriddstring)):
    ll.append(requests.get('http://api.stackexchange.com//2.2/users/'+useriddstring[i]+'?order=desc&sort=reputation&pagesize=100&site=stackoverflow').json())
    userrdata=[]
    for i in range(len(ll)):
        for j in range(len(ll[i]['items'])):
               userrdata.append(ll[i]['items'][j])

#userdataa
link='http://api.stackexchange.com//2.2/users/'+useriddstring[0]+'?order=desc&sort=reputation&pagesize=100&site=stackoverflow'
start='http://api.stackexchange.com//2.2/'
end='/'
folderuser=link.split(start)[-1].split(end)[0]
import json
import os
directory='StackExchange'
for i in range(len(userrdata)):
    #print(questiondata[0])
    uid=userrdata[i]['user_id']
    #jsonid=str(qid)
    if not os.path.exists(directory+'\\'+str(folderuser)):
        os.makedirs(directory+'\\'+str(folderuser))
        with open(directory+'\\'+str(folderuser)+'\\'+str(uid)+'.json', 'w') as outfile:
                json.dump(userrdata[i], outfile)
    elif os.path.exists(directory+'\\'+str(folderuser)):
            with open(directory+'\\'+str(folderuser)+'\\'+str(uid)+'.json', 'w') as outfile:
                json.dump(userrdata[i], outfile)

useriddstringg=useriddstring[7:11]

#questions from user id
quslink=[]
qusdata=[]
for i in range(len(useriddstringg)):
    for j in range(1,2):#page 1-25 
        quslink.append(requests.get('http://api.stackexchange.com//2.2/users/'+useriddstringg[i]+'/questions?order=desc&sort=activity&pagesize=100&key=XinmhjiFOa6sHZllDs4Y4Q((&page='+str(j)+'&site=stackoverflow&filter=!-*f(6t0VjPb5').json())
        for i in range(len(quslink)):
            for j in range(len(quslink[i]['items'])):
                   qusdata.append(quslink[i]['items'][j])

#questionfromuser

folderq='questions'
import json
import os
directory='StackExchange'
for i in range(len(qusdata)):
    #print(questiondata[0])
    dt=qusdata[i]['creation_date']
    dt2=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dt))
    dt3=dt2[0:10]
    dt4=dt3.replace('-','')
    qid=qusdata[i]['question_id'] 
    jsonid=str(qid)
    if not os.path.exists(directory+'\\'+str(folderq)):
        os.makedirs(directory+'\\'+str(folderq))
        if not os.path.exists(directory+'\\'+str(folderq)+'\\'+dt3):
            os.makedirs(directory+'\\'+str(folderq)+'\\'+str(dt3))
            if not os.path.isfile(directory+'\\'+str(folderq)+'\\'+str(dt3)+str(jsonid)+'\\'+'.json'):
                with open(directory+'\\'+str(folderq)+'\\'+str(dt3)+'\\'+jsonid+'.json', 'w') as outfile:
                    json.dump(qusdata[i], outfile)
        else:
            if not os.path.isfile(directory+'\\'+str(folderq)+'\\'+str(dt3)+str(jsonid)+'\\'+'.json'):
                with open(directory+'\\'+str(folderq)+'\\'+str(dt3)+'\\'+jsonid+'.json', 'w') as outfile:
                    json.dump(qusdata[i], outfile)
    elif os.path.exists(directory+'\\'+str(folderq)):
        if not os.path.exists(directory+'\\'+str(folderq)+'\\'+dt3):
            os.makedirs(directory+'\\'+str(folderq)+'\\'+str(dt3))
            if not os.path.isfile(directory+'\\'+str(folderq)+'\\'+str(dt3)+str(jsonid)+'\\'+'.json'):
                with open(directory+'\\'+str(folderq)+'\\'+str(dt3)+'\\'+jsonid+'.json', 'w') as outfile:
                    json.dump(qusdata[i], outfile)
        else:
            if not os.path.isfile(directory+'\\'+str(folderq)+'\\'+str(dt3)+str(jsonid)+'\\'+'.json'):
                with open(directory+'\\'+str(folderq)+'\\'+str(dt3)+'\\'+jsonid+'.json', 'w') as outfile:
                    json.dump(qusdata[i], outfile)

#answer from user id
answeruslink=[]
answerusdata=[]
for i in range(len(useriddstringg)):
    for j in range(1,2):#page 1-25 
        answeruslink.append(requests.get('http://api.stackexchange.com//2.2/users/'+useriddstringg[i]+'/answers?order=desc&sort=activity&pagesize=100&key=XinmhjiFOa6sHZllDs4Y4Q((&page='+str(j)+'&site=stackoverflow&filter=!-*f(6t0VjPb5').json())
        for i in range(len(answeruslink)):
            for j in range(len(answeruslink[i]['items'])):
                   answerusdata.append(answeruslink[i]['items'][j])

#answerdataa -2 
link='http://api.stackexchange.com//2.2/answers/'+answeriddstring[0]+'?order=desc&sort=activity&pagesize=100&site=stackoverflow&filter=!-*f(6sCNvG6L'
st='http://api.stackexchange.com//2.2/'
e='/'
folderans=link.split(st)[-1].split(e)[0]
import json
import os
directory='StackExchange'
for i in range(len(answerusdata)):
    #print(questiondata[0])
    aid=answerusdata[i]['answer_id']
    #jsonid=str(qid)
    if not os.path.exists(directory+'\\'+str(folderans)):
        os.makedirs(directory+'\\'+str(folderans))
        if not os.path.isfile(directory+'\\'+str(folderans)+'\\'+str(aid)+'\\'+'.json'):
            with open(directory+'\\'+str(folderans)+'\\'+str(aid)+'.json', 'w') as outfile:
                json.dump(answerusdata[i], outfile)
    elif os.path.exists(directory+'\\'+str(folderans)):
        if not os.path.isfile(directory+'\\'+str(folderans)+'\\'+str(aid)+'\\'+'.json'):
            with open(directory+'\\'+str(folderans)+'\\'+str(aid)+'.json', 'w') as outfile:
                json.dump(answerusdata[i], outfile)

#badges
bag=[]
#for i in range(1,5):#page 1-25 
bag.append(requests.get('http://api.stackexchange.com//2.2/badges/name?order=desc&min=bronze&max=bronze&sort=rank&pagesize=100&key=XinmhjiFOa6sHZllDs4Y4Q((&site=stackoverflow').json())

badgess=[]
for i in range(len(bag)):
            for j in range(len(bag[i]['items'])):
                   badgess.append(bag[i]['items'][j])

#badges
link='http://api.stackexchange.com//2.2/badges/name?order=desc&min=gold&max=gold&sort=rank&pagesize=100&key=XinmhjiFOa6sHZllDs4Y4Q((&site=stackoverflow'
st='http://api.stackexchange.com//2.2/'
e='/'
folderbad=link.split(st)[-1].split(e)[0]
hello=[]
import json
import os
directory='StackExchange'
for i in range(len(badgess)):
    #print(questiondata[0])
    bid=badgess[i]['badge_id']
    #jsonid=str(qid)
    if not os.path.exists(directory+'\\'+str(folderbad)):
        os.makedirs(directory+'\\'+str(folderbad))
        if not os.path.isfile(directory+'\\'+str(folderbad)+'\\'+str(bid)+'\\'+'.json'):
            with open(directory+'\\'+str(folderbad)+'\\'+str(bid)+'.json', 'w') as outfile:
                json.dump(badgess[i], outfile)
    elif os.path.exists(directory+'\\'+str(folderbad)):
        #hello.append(str(badges[i]['badge_id']))
        with open(directory+'\\'+str(folderbad)+'\\'+str(bid)+'.json', 'w') as outfile:
            json.dump(badgess[i], outfile)
