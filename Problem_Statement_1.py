import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\ASUS\Downloads\python Dataset 2.csv")

#1. Election Winner Analysis
#(a) Identify the winning candidate based on the highest votes
winner = df.loc[df['votes'].idxmax(), ['candidate_name', 'party', 'votes']]
print("Election Winner:")
print(winner)

#(b) Display the margin and margin percentage by which the candidate won
winner_margin = df.loc[df['votes'].idxmax(), ['margin', 'margin_percentage']]
print("Winning Margin Details:")
print(winner_margin)

#(c) Find the runner-up candidate and their vote margin from the winner
sorted_candidates = df.sort_values(by='votes', ascending=False)
runner_up = sorted_candidates.iloc[1][['candidate_name', 'party', 'votes', 'margin']]
print("Runner-up Candidate:")
print(runner_up)

#(d) Calculate the percentage difference in votes between the winner and runner-up
vote_difference = ((sorted_candidates.iloc[0]['votes'] - sorted_candidates.iloc[1]['votes']) / sorted_candidates.iloc[0]['votes']) * 100
print(f"Percentage Difference in Votes: {vote_difference:.2f}%")
