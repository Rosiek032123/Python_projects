import pandas as pd

hour=pd.read_csv('/Users/rosie/Desktop/Python_projects/files/hour.csv')
print(hour.head())

print(hour['count'].mean())
print(hour['count'].median())
print(hour['count'].std())
print(hour['registered'].min())
print(hour['registered'].max())

print(hour.describe()) #a quick way to get summary statistics


print(hour.loc[3,'count'])

print(hour.loc[2:4,'registered'])


print(hour.loc[hour['hr']<5,'registered'].mean())


print(hour.loc[(hour['hr']<5) & (hour['temp']<.50),'count'].mean())#and indicats two things must be true simultaneously
print(hour.loc[(hour['hr']<5) & (hour['temp']>.50),'count'].mean())


print(hour.loc[(hour['temp']>0.5) | (hour['hum']>0.5),'count'].mean())
#| means or


#groupby function
print(hour.groupby(['season'])['count'].mean())#in this data we are grouping by seaon and looking at the column count
print(hour.groupby(['season','holiday'])['count'].mean())#group by can group by multiple columns

#plotting
import numpy as nm
import matplotlib.pyplot as plt
plt.subplots(figsize=(10, 6))
plt.scatter(x = hour['instant'], y = hour['count'])
plt.show()
#recreating this with ggplot
from plotnine import ggplot, aes, geom_point
ggplot(hour)+ aes(x='instant',y='count')+geom_point()


#plotting with titles and labels
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x = hour['instant'], y = hour['count'])
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Ridership Count by Hour")
plt.show()
#recreating using ggplot
from plotnine import ggplot, aes, geom_point,labs
ggplot(hour)+aes(x='instant',y='count', title='Ridership Count by Hour')+ geom_point()+labs(x="hour",y="Count")


hour_first48=hour.loc[0:48,:]
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x = hour_first48['instant'], y = hour_first48['count'])
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Count by Hour - First Two Days")
plt.show()


#plotting while changing colors
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x = hour_first48['instant'], y = hour_first48['count'],c='red',marker='+')
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Count by Hour - First Two Days")
plt.show()


#doing a line plot and dashed plot 
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(hour_first48['instant'], hour_first48['casual'],c='red',label='casual',linestyle='-')
ax.plot(hour_first48['instant'],\
hour_first48['registered'],c='blue',label='registered',linestyle='--')
ax.legend()
plt.show()
