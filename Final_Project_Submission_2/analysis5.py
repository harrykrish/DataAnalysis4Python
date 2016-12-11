import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
b=pd.read_csv(r"C:\Users\harikrishna\Desktop\ProcessedData.csv")
bb=b[(b['rating'].notnull())&(b['Price Rating'].notnull())]
corrfactor=bb.corr()[['review_count','rating','Price Rating']]
sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")
sns.set(style="darkgrid")
#df.applymap(atof)


#figure = plt.subplots(ncols=2, sharey=True)

plt.figure(figsize=(45,10))
sns.lmplot(x="review_count", y="Price Rating", hue='country',data=bb)
plt.title('Relationship between review count and price rating')
plt.xlabel('Review Count')
plt.ylabel('Price Rating')
plt.savefig(r"Output Files\Analysis 5\Plot\Review Count Vs Place Rating.jpg")
sns.lmplot(x="rating", y="Price Rating", hue='country',data=bb)
#plot.text
#plt.yticks([1, 0.1, 0.01, 0.001])
#f = plt.figure()
plt.title('Relationship between place rating and price rating')
plt.xlabel('Rating of place')
plt.ylabel('Price Rating')
plt.savefig(r"Output Files\Analysis 5\Plot\Rating of place Vs Place Rating.jpg")
print("Plots saved successfully")
plt.show()
