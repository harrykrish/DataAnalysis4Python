import argparse
#import Image
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
parser = argparse.ArgumentParser()
parser.add_argument("--c",dest="city", type=str,
                    help="input a city name")
parser.add_argument("--n",dest="country", type=str,
                    help="input a country name")
parser.add_argument("--v",help="input a city name  using --c and country code using --n")
args = parser.parse_args()
cityname = args.city
countrycode = args.country
if(len(countrycode)!=2):
    parser.error('Enter correct country code my friend!! I already told you!(Two characters AU, US etc)')

count=0

def Rest(count,cityinput,countryinput):
    if(count<2):
        #Number of restaurants per capita
        df1=pd.read_csv("Other Files\\ProcessedData.csv",encoding='utf-8')
        cityinput=cityname
        countryinput=countrycode
        df2=df1[(df1['city_x']== cityinput)& (df1['country']== countryinput)]
        print("Length of df2")
        h=len(df2)
        print(h)
        if(h>0):
            df3=pd.DataFrame(columns=['City Name', 'restaurant_per_capita'])
            populationofcity=df2['population'].mean()
            nrow=len(df2.index)
            pl=populationofcity/1000
            index=nrow/pl
            dictt={'City Name': cityinput,'restaurant_per_capita':index}
            df3.loc[0]=dictt
            df4=df1[(df1['country']== countryinput)]

            uniqcity=df4['city_x'].unique()
            values=[]
            for i in range(len(uniqcity)):
                pop=df4[(df4['city_x']==uniqcity[i])]['population'].mean()
                nrow=len(df4[(df4['city_x']==uniqcity[i])])
                popp=pop/1000
                indexx=nrow/popp
                dictt2={'City Name': uniqcity[i],'restaurant_per_capita':indexx}
                values.append(dictt2)
            for i in range(len(values)):
                if(values[i]['City Name']!=cityinput):
                    df3.loc[i+1]=values[i]

            newdf3=pd.DataFrame()
            newdf3=df3[df3['restaurant_per_capita'].notnull()]
            newdf33=newdf3.iloc[[0]]
            tempdf=newdf3.loc[1:].sort_values(by='restaurant_per_capita',ascending=False)
            tempdfcsv=newdf33.append(tempdf)
            tempdfcsv.to_csv("Output Files\\Analysis 1\\CSV Files\\restaurant-per-capita.csv")
            tempdff=tempdf.head(9)
            final=newdf33.append(tempdff)
            #Plotting the data - City input and other top ten cities
            ax=sns.factorplot("City Name", "restaurant_per_capita",
                               data=final, kind="bar",
                               size=6, palette="muted", legend=False)
            plt.savefig(r'Output Files\Analysis 1\Plot\Restaurant-Per-Capita.jpg')
            print('CSV Files and Plots saved successfully')
            plt.title("Restaurant per Capita (every 1000 people)for "+str(cityinput)+str(" ")+str("compared to other cities in ")+str(countryinput),fontsize=15)
            plt.show()
        elif(h<1):
            count=count+1
            a=cityinput
            il=input('Im sorry..No data about the city\n No issues. Just enter the category you want to get the data about.\n 1. hotels,2.restaurants or 3.attractions')
            ill=int(il)
            if(ill==1):
                b='hotels'
            if(ill==2):
                b='restaurants'
            if(ill==3):
                b='attractions'
            if(ill>3):
                print('Invalid input')
                
            os.system("python gathering_data_function.py --c "+a+" --n "+b)
            Rest(count,cityinput,countryinput)
    if(count==2):
        print('Tried to get data. Could not fetch!!')

Rest(count,cityname,countrycode)

            
