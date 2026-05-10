import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

f = sns.load_dataset("flights")
# x = f['passengers']
# y = f['year']
print(f.describe())

plt.figure(figsize=(10,5))
# sns.lineplot(x="passengers",y="year",data=f, estimator="mean")
# plt.title("Huehuee")
# plt.show()


# sns.histplot(f['passengers'],bins=10,kde=True)# kde= kernel desity estimator
# plt.title("Hist")
# plt.show()



#Pie Chart

# pass_count = f["passengers"].value_counts()
# plt.pie( pass_count, labels=pass_count.index, autopct="%1.1f%%")
# plt.title("Species distribution")
# plt.show()

# plt.figure()
# sns.scatterplot(x="passengers",y="month",hue="year",data=f)
# plt.title("Passengers vs month")
# plt.show()

#pair plot
sns.pairplot(f,hue="passengers")
plt.show()