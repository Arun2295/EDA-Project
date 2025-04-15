#5. Candidate Position Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
df=pd.read_csv(r"C:\python\datasetss\python Dataset 2.csv")

#(a) Identify how many candidates secured each position
position_counts = df['position'].value_counts().sort_index()
print("Number of Candidates by Position:")
print(position_counts)

#(b) Find the average margin percentage for each position
position_margin_avg = df.groupby('position')['margin_percentage'].mean()
print("Average Margin Percentage by Position:")
print(position_margin_avg)

#(c) Identify the most competitive election (smallest margin of victory)
most_competitive = df[df['position'] == 1].sort_values(by='margin').iloc[0]
print("Most Competitive Election:")
print(most_competitive[['candidate_name', 'party', 'margin']])

