import pandas as pd

hour=pd.read_csv('/Users/rosie/Desktop/Python_projects/files/hour.csv')
print(hour.head())

print(hour['count'].mean())
print(hour['count'].median())
print(hour['count'].std())
print(hour['registered'].min())
print(hour['registered'].max())

print(hour.describe()) #a quick way to get summary statistics



