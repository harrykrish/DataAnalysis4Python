import argparse
import os
import pandas as pd
import seaborn as sns
print('Enter the case number of the analysis you want to perform')
analysisno=input('Case 1: You want to know the restaurants,hotels and attractions per capita for a city?\nCase 2: Feeling Hungry? Not to worry!!\nCase 3:Want to know the delacies of your place?\nCase 4:How is the temperature of a state related to the number of attractions it has?\nCase 5:Time for some statistics. Whats the correlation between ratings,reviews and price of a place.?\nCase 6: You want to find the country wide distribution of hotels,restaurants or atractions?')
anno=int(analysisno)
if(anno==1):
    print('I will pull up the stats..I need some information')
    a=input('Enter your city')
    b=input('Enter your country code. Eg : US, AU etc')
    os.system("python analysis1.py --c "+a+" --n "+b)
if(anno==2):
    print('There are many places to go and eat!!Il find out which ones are open at this time. I wont make you visit places closed right now :-)')
    c=input('Enter your city')
    d=input('Enter your country code. Eg : US, AU etc')
    os.system("python analysis2.py --c "+c+" --n "+d)
if(anno==3):
    e=input('Find out the popular delicacies in your country. Just enter your country code. Eg : US, AU etc ')
    os.system("python analysis3.py --c "+e)
if(anno==4):
    v=print('Im going to tell you if there is a relationship between the temperature of a state in US with the attractive places it has')
    os.system("python analysis4.py")
if(anno==5):
    v=print('I dont need your input here\n Your going to see some interesting stats!')
    os.system("python analysis5.py")
if(anno==6):
    z=input('Curious to know which country has many hotels or restaurants? Just enter hotels,restaurants or attractions and il get you the details')
    os.system("python analysis6.py --c "+z)
    
