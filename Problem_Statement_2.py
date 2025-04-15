#3. Gender-Based Candidate Performance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df=pd.read_csv(r"C:\python\datasetss\python Dataset 2.csv")

#(a) Count the number of male and female candidates
gender_counts = df['sex'].value_counts()
print("Gender-wise Candidate Count:")
print(gender_counts)

#(b) Compare the average vote share percentage of male vs. female candidates
gender_vote_share = df.groupby('sex')['vote_share_percentage'].mean()
print("Average Vote Share Percentage by Gender:")
print(gender_vote_share)

#(c) Find the highest vote share percentage among male and female candidates
highest_vote_share_male = df[df['sex'] == 'Male']['vote_share_percentage'].max()
highest_vote_share_female = df[df['sex'] == 'Female']['vote_share_percentage'].max()
print(f"Highest Vote Share - Male: {highest_vote_share_male}%")
print(f"Highest Vote Share - Female: {highest_vote_share_female}%")

#(d) Determine whether male or female candidates had a higher success rate
success_rate = df[df['position'] == 1].groupby('sex').size() / df.groupby('sex').size() * 100
print("Success Rate by Gender (% of winning candidates):")
print(success_rate)

