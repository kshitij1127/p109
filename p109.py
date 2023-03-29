import csv 
import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")

math_score = []

math_df = df.groupby("gender")["math score"].mean()
print(math_df)

std = statistics.stdev(math_df)
print(std)
math_score.append(df)

std1_st, std1_end = math_df - std, math_df + std
std2_st, std2_end = math_df - (2*std), math_df + (2*std)
std3_st, std3_end = math_df - (2*std), math_df + (2*std)

