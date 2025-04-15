import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df=pd.read_csv(r"C:\python\datasetss\python Dataset 2.csv")
# Set seaborn style
sns.set(style="whitegrid")
#Histogram – Margin Percentage Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['margin_percentage'], bins=20, kde=True, color='tomato')
plt.title("Distribution of Margin Percentage")
plt.xlabel("Margin Percentage")
plt.ylabel("Number of Candidates")
plt.tight_layout()
plt.show()
#Pie Chart – Candidate Gender Proportion
gender_counts = df['sex'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title("Gender Proportion of Candidates")
plt.axis('equal')
plt.tight_layout()
plt.show()
#Scatter Plot – Valid Votes vs Turnout Percentage
plt.figure(figsize=(8, 6))
sns.scatterplot(x='valid_votes', y='turnout_percentage', hue='sex', data=df, palette='Dark2', alpha=0.7)
plt.title("Valid Votes vs Turnout Percentage by Gender")
plt.xlabel("Valid Votes")
plt.ylabel("Turnout (%)")
plt.legend(title='Gender')
plt.tight_layout()
plt.show()
#Line Plot – Top 10 Candidates by Votes
top_candidates = df.sort_values(by='votes', ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.lineplot(x='candidate_name', y='votes', data=top_candidates, marker='o', sort=False, color='darkblue')
plt.xticks(rotation=45)
plt.title("Top 10 Candidates by Vote Count")
plt.xlabel("Candidate")
plt.ylabel("Votes")
plt.tight_layout()
plt.show()
#Cleaned Correlation Heatmap
df = df.drop(columns=["_id", "index", "year", "month", "pc_code"])
numeric_df = df.select_dtypes(include=["number"])
corr_matrix = numeric_df.corr()

plt.figure(figsize=(10, 7))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Cleaned Correlation Heatmap")
plt.tight_layout()
plt.show()


