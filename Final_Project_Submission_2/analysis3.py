import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
parser = argparse.ArgumentParser()
parser.add_argument("--c",dest="country", type=str,
                    help="input a country code")
parser.add_argument("--v",help="input a country codeusing --c")
args = parser.parse_args()
countrycode = args.country
if(len(countrycode)!=2):
    parser.error('Enter correct country code my friend!! I already told you!(Two characters AU, US etc)')
#Number of restaurants in each cuisine in a country
countryliving=countrycode
datafr=pd.read_csv(r"Other Files\ProcessedData.csv",encoding='utf-8')
datafr= datafr.ix[:,'id':]
cuisine=pd.read_csv(r"Other Files\RestaurantCategory.csv",encoding='utf-8')
datafr2_country=datafr[(datafr['country']==countryliving)&(datafr['place_category']!='attractions')]
unid=list(datafr2_country['id'].unique())
df_category=pd.DataFrame()
for i in range(len(unid)):
    t=cuisine[(cuisine['id']==unid[i])]
    df_category=df_category.append(t,ignore_index=True)

groupcategory=df_category.groupby(['title']).count().sort_values(['id'],ascending=False)
topgroups=groupcategory[0:5]
topcateg=list(topgroups.index.values)
groupcategory2=groupcategory.reset_index(drop=False).head(10)
groupcategory.to_csv(r'Output Files\Analysis 3\CSV Files\TopCuisines.csv')
colors=["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]

plt.pie(
    groupcategory2['id'],
    labels=groupcategory2['title'],
    shadow=False,
    startangle=90,
    colors=colors,
    # with the percent listed as a fraction
    autopct='%1.1f%%',
    )


# View the plot drop above
plt.title("Top Cuisines distribution "+str("in ")+str(countryliving),y=1.08)
plt.axis('equal')
plt.savefig(r'Output Files\Analysis 3\Plot\Top-Cuisines.jpg')
toptmm=pd.DataFrame()
for i in range(len(topcateg)):
    toptm=cuisine[(cuisine['title']==topcateg[i])]
    toptmm=toptmm.append(toptm,ignore_index=True)

comb=pd.merge(toptmm,datafr,how='left', left_on=['id'],right_on=['id'])

comb=comb[['id','name','review_count','rating','title']]
f_10=comb[['name','title','rating','review_count']].sort_values(by=['rating','review_count'], ascending=[0,0])

f_12=pd.DataFrame()
for i in range(len(topcateg)):
    f_11=f_10[(f_10['title']==topcateg[i])]
    f_12=f_12.append(f_11.head(3))

f_12.to_csv(r"Output Files\Analysis 3\CSV Files\Top5-Category-Restaurants.csv")
#ax = sns.barplot(x="City Name", y="restaurant_per_capita", data=final)
ax=sns.factorplot("name", "review_count",
                   data=f_12, kind="bar",
                   size=6, palette="muted", legend=False)
ax.set_xticklabels(rotation=90)
plt.savefig(r'Output Files\Analysis 3\Plot\Top-Cuisines-Restaurants.jpg')
print("Plots have been generated")
