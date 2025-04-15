#4. Party-wise Vote Share Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df=pd.read_csv(r"C:\python\datasetss\python Dataset 2.csv")

#(a) Group candidates by party and calculate total votes received by each party
party_votes = df.groupby('party')['votes'].sum().sort_values(ascending=False)
print("Total Votes Received by Each Party:")
print(party_votes)

#(b) Find the party with the highest average vote share percentage
party_avg_vote_share = df.groupby('party')['vote_share_percentage'].mean().sort_values(ascending=False)
print("Party with Highest Average Vote Share Percentage:")
print(party_avg_vote_share.head(1))

#(c) Identify the party that won the most number of seats (first-place positions)
winning_parties = df[df['position'] == 1]['party'].value_counts()
top_party = winning_parties.idxmax()
print(f"Party with Most Wins: {top_party} ({winning_parties.max()} seats)")

#(d) Calculate the average margin percentage of victory for each party
party_margin_avg = df[df['position'] == 1].groupby('party')['margin_percentage'].mean()
print("Average Margin Percentage of Victory per Party:")
print(party_margin_avg)
