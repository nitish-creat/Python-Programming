import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

f = sns.load_dataset("flights")
print(f.info())

# print(f.head())

# print(f['passengers'])

# x = f['passengers']
# y = f['year']

# plt.plot(x,y)
# plt.title("Huehue")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()


# pass_count = f["passengers"].value_counts()
# plt.figure(figsize=(5,5))
# plt.bar(pass_count.index , pass_count.values)
# plt.title("Flight data")
# plt.xlabel("Passengers")
# plt.ylabel("count")
# plt.show()



# plt.hist(f["passengers"],bins=10)
# plt.title("Hist")
# plt.xlabel("Pass")
# plt.ylabel("Count")
# plt.show()



# plt.figure(figsize=(10,5))
# plt.scatter(f["passengers"],f["month"])
# plt.title("Passengers vs month")
# plt.xlabel("Passengers")
# plt.ylabel("Month")
# plt.show()

plt.figure(figsize=(10,5))
f.boxplot(column="passengers", by="month")
plt.title("Boxplot of passengers by year")
plt.suptitle("")
plt.show()
