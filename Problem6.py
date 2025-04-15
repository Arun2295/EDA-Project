import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\python\datasetss\python Dataset 2.csv")
df = df.drop(columns=["_id", "index", "year", "month", "pc_code"])
numeric_df = df.select_dtypes(include=["number"])
corr_matrix = numeric_df.corr()

plt.figure(figsize=(10, 7))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Cleaned Correlation Heatmap")
plt.tight_layout()
plt.show()
