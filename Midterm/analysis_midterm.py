#Reading all data
import os
import json
import operator
import time
from datetime import datetime 
path = 'StackExchange\\questions'
stackquestions=[]
stackanswers=[]
stackbadges=[]
stackusers=[]
stackques = [os.path.join(root, name)
            for root, dirs, files in os.walk(path)
            for name in files
            if name.endswith((".json", ".jsons"))]

for js in stackques:
    with open(js) as json_file:
        stackquestions.append(json.load(json_file))

#Answers
path_to_ans = 'StackExchange\\answers'
json_ans = [pos_json for pos_json in os.listdir(path_to_ans) if pos_json.endswith('.json')]
for js in json_ans:
    with open(os.path.join(path_to_ans, js)) as json_fil:
        stackanswers.append(json.load(json_fil))
#Users
path_to_user = 'StackExchange\\users'
json_user = [pos_json for pos_json in os.listdir(path_to_user) if pos_json.endswith('.json')]
for js in json_user:
    with open(os.path.join(path_to_user, js)) as json_fil:
        stackusers.append(json.load(json_fil))
#badges
path_to_badges = 'StackExchange\\badges'
json_badges = [pos_json for pos_json in os.listdir(path_to_badges) if pos_json.endswith('.json')]
for js in json_badges:
    with open(os.path.join(path_to_badges, js)) as json_fil:
        stackbadges.append(json.load(json_fil))

#Getting analysis input from user
inp=input("Case 1: Finding user specialization\nCase 2:Top questions posted by users\nCase 3:Top and bottom ten users based on reputation over last one year\nCase 4:Find the most active and popular questions and topics\nCase 5: Top characteristics of user (badge characteristics)")
inp=int(inp)
if inp==1:
#Finding user specialization based on answers
#user specialist
    useranswers={}
    for i in range(len(stackusers)):
        userid=stackusers[i]['user_id']
        for j in range(len(stackanswers)):
            if(stackanswers[j]['owner']['user_id']==userid):
                if(stackanswers[j]['owner']['user_id'] not in useranswers.keys()):
                    useranswers[userid]={}
                    for k in range(len(stackanswers[j]['tags'])):
                        if(stackanswers[j]['tags'][k] in useranswers[userid].keys()):
                            
                            tagname=stackanswers[j]['tags'][k]
                            useranswers[userid][tagname]+=1
                        else:
                            tagname=''
                            tagname=stackanswers[j]['tags'][k]
                            useranswers[userid][tagname]=1 
                    
                elif(stackanswers[j]['owner']['user_id'] in useranswers.keys()):
                    for k in range(len(stackanswers[j]['tags'])):
                        if(stackanswers[j]['tags'][k] in useranswers[userid].keys()):
                            tagname=stackanswers[j]['tags'][k]
                            useranswers[userid][tagname]+=1
                        else:
                            tagname=''
                            tagname=stackanswers[j]['tags'][k]
                            useranswers[userid][tagname]=1

    #Checking which topic each user has maximum answered and assigning him a specilization 
    #Due to a limitation of number of answers I am fetching, if a user has answered about a particular topic 
    #same number of times, all occurences will be returned
    listt=list(useranswers.keys())
    userspec={}
    #for key,value in useranswers.items():
    #for key2,value2 in 
    #useranswers[4044318]
    useranswers[listt[0]].keys()
    for i in range(len(listt)):
        for key,value in useranswers[listt[i]].items():
                h=max(useranswers[listt[i]].values())
                maxval = max(useranswers[listt[i]].items(), key=operator.itemgetter(1))[1]
                keyss = [k for k,v in useranswers[listt[i]].items() if v==maxval]
                userspec[listt[i]]={}
                userspec[listt[i]]['Specialist']=keyss

    rowspecq=[]
    for key,value in userspec.items():
        keyy=key
        v=value
        ls=value['Specialist']
        for i in range(len(ls)):
            rowspecq.append(str(keyy)+','+str(userspec[keyy]['Specialist'][i])+'\n')
        
    with open('Reports\\Case 1\\userspecialization.csv', 'w') as csv_file:
        csv_file.write('user_id,specialization\n')
        for a in rowspecq:
            csv_file.write(a)

    print('CSV has been generated')
if inp==2:
    #Top questions based on user status (badges) - 2
    userques={}
    for i in range(len(stackusers)):
        usid=stackusers[i]['user_id']
        sumbadges=sum(stackusers[i]['badge_counts'].values())
        maxques=0
        userques[usid]={}
        for j in range(len(stackquestions)):
            if('user_id' in stackquestions[j]['owner'].keys()):
                if(stackquestions[j]['owner']['user_id']==usid):
                    if(stackquestions[j]['view_count']>maxques):
                        userques[usid]['view']=0
                        userques[usid]['question']=0
                        userques[usid]['tag']=0
                        maxques=stackquestions[j]['view_count']
                        userques[usid]['view']=stackquestions[j]['view_count']
                        userques[usid]['question']=stackquestions[j]['title']
                        userques[usid]['tag']=stackquestions[j]['tags']

    #Top users
    topusers={}
    for i in range(len(stackusers)):
        ud=stackusers[i]['user_id']
        topusers[ud]=0
        sumbadges=sum(stackusers[i]['badge_counts'].values())
        topusers[ud]=sumbadges  
        
    topten = dict(sorted(topusers.items(), key=operator.itemgetter(1), reverse=True)[:10])
    toptenkeys=list(topten.keys()) #Saving top ten users

    #Passing userid to fetch max view question (top users)
    maxuserquestion={}
    for i in range(len(toptenkeys)):
        maxuserquestion[toptenkeys[i]]={}
        maxuserquestion[toptenkeys[i]]['question']=''
        maxuserquestion[toptenkeys[i]]['tag']=''
        q=userques[toptenkeys[i]]['question']
        tag=userques[toptenkeys[i]]['tag']
        maxuserquestion[toptenkeys[i]]['question']=q
        maxuserquestion[toptenkeys[i]]['tag']=tag

    rowmaxq=[]
    for key,value in maxuserquestion.items():
        keyy=key
        v=value
        rowmaxq.append(str(maxuserquestion[keyy]['question'])+','+str(keyy)+'\n')
        
    import csv
    with open('Reports\\Case 2\\top_questions_user_weightage.csv', 'w') as csv_file:
        csv_file.write('question,posted_by\n')
        for a in rowmaxq:
            csv_file.write(a)

    print('CSV has been generated')
if inp==3:
    #Change in reputation -3 
    userrepyear={}
    for i in range(len(stackusers)):
        ussid=stackusers[i]['user_id']
        userrepyear[ussid]={}
        repyear=stackusers[i]['reputation_change_year']
        userrepyear[ussid]=stackusers[i]['reputation_change_year']

    #Top ten and bottom ten users based on reputation change over the year
    usertopandbottom=[]
    userrepyeartopten = dict(sorted(userrepyear.items(), key=operator.itemgetter(1), reverse=True)[:10])
    userrepyeartoptenkeys=list(userrepyeartopten.keys()) #Saving top ten users
    userrepyearbottomten = dict(sorted(userrepyear.items(), key=operator.itemgetter(1), reverse=False)[:10])
    userrepyearbottomtenkeys=list(userrepyearbottomten.keys()) #Saving bottom ten users
    userrepyeartoptenkeys
    for i in range(len(userrepyeartoptenkeys)):
        usertopandbottom.append(userrepyeartoptenkeys[i])
        
    for i in range(len(userrepyearbottomtenkeys)):
        usertopandbottom.append(userrepyearbottomtenkeys[i])

    #Top ten and bottom ten users reputation change
    userrep={}
    for i in range(len(usertopandbottom)):
        for j in range(len(stackusers)):
            if(stackusers[j]['user_id']==usertopandbottom[i]):
                uss=stackusers[j]['user_id']
                userrep[uss]={}
                rep=stackusers[j]['reputation']
                repold=(stackusers[j]['reputation']-stackusers[j]['reputation_change_year'])
                repchange=(((stackusers[j]['reputation'])-(stackusers[j]['reputation']-stackusers[j]['reputation_change_year']))/(stackusers[j]['reputation']-stackusers[j]['reputation_change_year']))*100
                repchangee=round(repchange,2)
                userrep[uss]['current_reputation']=0
                userrep[uss]['old_reputation']=0
                userrep[uss]['reputation_change_percent']=0
                userrep[uss]['current_reputation']=rep
                userrep[uss]['old_reputation']=repold
                userrep[uss]['reputation_change_percent']=repchangee

    row=[]
    for key,value in userrep.items():
        keyy=key
        v=value
        row.append(str(keyy)+','+str(userrep[keyy]['current_reputation'])+','+str(userrep[keyy]['old_reputation'])+','+str(userrep[keyy]['reputation_change_percent'])+'\n')
        
    import csv
    with open('Reports\\Case 3\\user_reputation.csv', 'w') as csv_file:
        csv_file.write('user_id,current_reputation,old_reputation,percent_change\n')
        for a in row:
            csv_file.write(a)

    print('CSV has been generated')
if inp==4:
    #Active & Popular Questions - 4
    
    popquestions={}
    for i in range(len(stackquestions)):
        popquestions[stackquestions[i]['question_id']]=0
        created=stackquestions[i]['creation_date']
        lastactivity=stackquestions[i]['last_activity_date']
        created2=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(created))
        lastactivity2=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lastactivity))
        day1 = datetime.strptime(created2, '%Y-%m-%d %H:%M:%S')
        day2 = datetime.strptime(lastactivity2, '%Y-%m-%d %H:%M:%S')
        diff=(day2-day1).days
        popquestions[stackquestions[i]['question_id']]=diff

    #Questions accessed after many days
    quespop=[]
    quespoptopten = dict(sorted(popquestions.items(), key=operator.itemgetter(1), reverse=True)[:10])
    quespoptoptenkeys=list(quespoptopten.keys()) #Saving top ques

    questionpopularitems={}
    poptags=[]
    for i in range(len(quespoptoptenkeys)):
        for j in range(len(stackquestions)):
            if(stackquestions[j]['question_id']==quespoptoptenkeys[i]):
                qid=stackquestions[j]['question_id']
                questionpopularitems[qid]={}
                questionpopularitems[qid]['title']=''
                titlee=stackquestions[j]['title']
                questionpopularitems[qid]['title']=titlee
                questionpopularitems[qid]['tags']=[]
                for k in range(len(stackquestions[j]['tags'])):
                    t=stackquestions[j]['tags'][k]
                    questionpopularitems[qid]['tags'].append(t) 
                    poptags.append(t)

    rowdata=[]
    for key,value in questionpopularitems.items():
        keyy=key
        v=value
        rowdata.append(str(keyy)+','+str(questionpopularitems[keyy]['title'])+','+str(popquestions[keyy])+'\n')
        
    import csv
    with open('Reports\\Case 4\\topquestions.csv', 'w') as csv_file:
        csv_file.write('question_id,question,day diff between posting and last activity\n')
        for a in rowdata:
            csv_file.write(a)

    #Popular topics for questions over time (under previous analysis)
    populartags={}
    for i in range(len(poptags)):
        if poptags[i] not in populartags.keys():
            populartags[poptags[i]]=1
        else:
            populartags[poptags[i]]+=1  


    #Top 2 popular tags
    popp=[]
    import heapq
    l=sorted(populartags.values(), reverse=True)
    lis=heapq.nlargest(2, l)
    for i in range(len(lis)):
        for key,value in populartags.items():
            if(value==lis[i]):
                popp.append(key)
                
    rowwdata=[]
    for i in range(len(popp)):
        rowwdata.append((str(popp[i])+','+str(populartags[popp[i]])+'\n'))
        
    import csv
    with open('Reports\\Case 4\\top_two_tags.csv', 'w') as csv_file:
        csv_file.write('tag_name,Number of times repeated\n')
        for a in rowwdata:
            csv_file.write(a)

    print('CSV has been generated')
if inp==5:
    #Determing dominant characteristics of user range-5
    rankmedals={}
    for i in range(len(stackbadges)):
        charrank=stackbadges[i]['rank']
        count=stackbadges[i]['award_count']
        if(charrank not in rankmedals.keys()):
            rankmedals[charrank]=0
            rankmedals[charrank]=count
        else:
            rankmedals[charrank]+=count  
            
    badgespercentgold={}
    badgespercentsilver={}
    badgespercentbronze={}
    for i in range(len(stackbadges)):
        badgename=stackbadges[i]['name']
        badgecount=stackbadges[i]['award_count']
        rankofbadge=stackbadges[i]['rank']
        if(rankofbadge=='bronze'):
            badgespercentbronze[badgename]=0
            percentag=round((badgecount/rankmedals['bronze'])*100,2)
            badgespercentbronze[badgename]=percentag
        elif(rankofbadge=='silver'):
            badgespercentsilver[badgename]=0
            percentag=round((badgecount/rankmedals['silver'])*100,2)
            badgespercentsilver[badgename]=percentag
        elif(rankofbadge=='gold'):
            badgespercentgold[badgename]=0
            percentag=round((badgecount/rankmedals['gold'])*100,2)
            badgespercentgold[badgename]=percentag  

    #Sorting
    badgesgoldthree = dict(sorted(badgespercentgold.items(), key=operator.itemgetter(1), reverse=True)[:3])
    badgesgoldthreekeys=list(badgesgoldthree.keys()) #Saving top three characteristics

    badgessilverthree = dict(sorted(badgespercentsilver.items(), key=operator.itemgetter(1), reverse=True)[:3])
    badgessilverthreekeys=list(badgessilverthree.keys()) #Saving top three characteristics

    badgesbronzethree = dict(sorted(badgespercentbronze.items(), key=operator.itemgetter(1), reverse=True)[:3])
    badgesbronzethreekeys=list(badgesbronzethree.keys()) #Saving top three characteristics

    #hardcoding characteristic of badge name
    badgestop=[]
    for i in range(len(badgesgoldthreekeys)):
        badgestop.append(badgesgoldthreekeys[i])

    for i in range(len(badgessilverthreekeys)):
        badgestop.append(badgessilverthreekeys[i])

    for i in range(len(badgesbronzethreekeys)):
        badgestop.append(badgesbronzethreekeys[i])

    #hardcoding characteristics:
    charc={'Famous Question':'Question with 10000 views','Fanatic':'Visit the site each day for 100 consecutive days',
          'Great Answer':'Answer score of 100 or more','Notable Question':'Question with 2500 views','Necromancer':'Answer a question more than 60 days later with score of 5 or more',
          'Yearling':'Active member for a year earning at least 200 reputation','Editor':'First edit',
          'Student':'First question with score of 1 or more','Popular Question':'Question with 1000 views'}

    #Top characteristics 
    topcharacteristics={}
    for i in range(len(stackbadges)):
        if(stackbadges[i]['name']==badgesgoldthreekeys[0]):
            namee=stackbadges[i]['name']
            topcharacteristics[namee]={}
            rankk=stackbadges[i]['rank']
            topcharacteristics[namee]['rank']=''
            if(rankk=='bronze'):
                percentt=badgespercentbronze[namee]
            if(rankk=='silver'):
                percentt=badgespercentsilver[namee]
            if(rankk=='gold'):
                percentt=badgespercentgold[namee]
            
            topcharacteristics[namee]['rank']=rankk
            topcharacteristics[namee]['percentage']=percentt
            topcharacteristics[namee]['description']=''
            topcharacteristics[namee]['description']=charc[namee]
            
        if(stackbadges[i]['name']==badgessilverthreekeys[0]):
            namee=stackbadges[i]['name']
            topcharacteristics[namee]={}
            rankk=stackbadges[i]['rank']
            topcharacteristics[namee]['rank']=''
            if(rankk=='bronze'):
                percentt=badgespercentbronze[namee]
            if(rankk=='silver'):
                percentt=badgespercentsilver[namee]
            if(rankk=='gold'):
                percentt=badgespercentgold[namee]
            
            topcharacteristics[namee]['rank']=rankk
            topcharacteristics[namee]['percentage']=percentt
            topcharacteristics[namee]['description']=''
            topcharacteristics[namee]['description']=charc[namee]
            
        if(stackbadges[i]['name']==badgesbronzethreekeys[0]):
            namee=stackbadges[i]['name']
            topcharacteristics[namee]={}
            rankk=stackbadges[i]['rank']
            topcharacteristics[namee]['rank']=''
            if(rankk=='bronze'):
                percentt=badgespercentbronze[namee]
            if(rankk=='silver'):
                percentt=badgespercentsilver[namee]
            if(rankk=='gold'):
                percentt=badgespercentgold[namee]
            
            topcharacteristics[namee]['rank']=rankk
            topcharacteristics[namee]['percentage']=percentt
            topcharacteristics[namee]['description']=''
            topcharacteristics[namee]['description']=charc[namee]

    rowchardata=[]
    for key,value in topcharacteristics.items():
        keyy=key
        v=value
        
        rowchardata.append(str(keyy)+','+str(topcharacteristics[keyy]['rank'])+','+str(topcharacteristics[keyy]['percentage'])+','+str(topcharacteristics[keyy]['description'])+'\n')
        
    import csv
    with open('Reports\\Case 5\\topbadges_per_category.csv', 'w') as csv_file:
        csv_file.write('Badge Name,Rank,Percentage of badges awarded in this rank,description\n')
        for a in rowchardata:
            csv_file.write(a)
            
    #Top 3 badges in each category
    rowbadgedata=[]
    for i in range(len(badgestop)):
        rowbadgedata.append(badgestop[i]+','+str(charc[badgestop[i]])+'\n')
        
    import csv
    with open('Reports\\Case 5\\top_three_badges_categorywise.csv', 'w') as csv_file:
        csv_file.write('Badge Name,description\n')
        for a in rowbadgedata:
            csv_file.write(a)
    print('CSV has been generated')

elif inp>5:
    print('Please enter a valid input (Cases 1-5)')
    
