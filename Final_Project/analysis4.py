#Relationship between number of attractions and temperature range
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
temp_data=pd.read_csv(r"Other Files\weather_state_yrmonth.csv")
dt_data=pd.read_csv(r"Other Files\ProcessedData.csv")
temp_data= temp_data.ix[:,'YearMonth':]
temp_data=temp_data[temp_data['AvgTemp']!='M']
temp_data=temp_data.reset_index(drop=True)
temp_data['AvgTemp'] = pd.to_numeric(temp_data['AvgTemp']).fillna(0)
temp_data_avg=temp_data.groupby('State',as_index=False)['AvgTemp'].mean()
dt_data_country=dt_data[(dt_data['country']=='US')&(dt_data['place_category']=='attractions')]
dt_data_country_attractions_count=dt_data_country.groupby('state',as_index=False)['place_category'].count()
dt_data_country_attractions_count_desc=dt_data_country_attractions_count.sort_values(by='place_category',ascending=False).reset_index(drop=True)
state_temp=pd.merge(dt_data_country_attractions_count_desc,temp_data_avg,how='inner', left_on=['state'],right_on=['State'])
state_temp.to_csv(r"Output Files\Analysis 4\CSV Files\Statewise-attractions_temp_relation.csv")
sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")
sns.set(style="darkgrid")

    
sns.lmplot(x="place_category", y="AvgTemp", hue='state',data=state_temp)
plt.title('Relationship between temperature and number of attractive places in the state')
plt.xlabel('place_category')
plt.ylabel('avgTemp')
plt.savefig(r'Output Files\Analysis 4\Plot\Attractions-Temperature-relation.jpg')
plt.show()
