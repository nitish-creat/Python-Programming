
import seaborn as sns
import matplotlib.pyplot as plt

s = sns.load_dataset("iris")

# corr = s.corr(numeric_only=True)
# plt.imshow(corr)
# plt.colorbar()
# plt.xticks(range(len(corr)), corr.columns, rotation=45)
# plt.yticks(range(len(corr)), corr.columns)
# plt.title("Correlation Matrix") 
# plt.show()

# plt.figure(figsize=(10,5))
# sns.heatmap(s.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
# plt.title("Correlation Matrix") 
# plt.show()


sns.boxplot(x="species",y="sepal_length",data=s)
plt.title("Sepal length by species")
plt.show()
