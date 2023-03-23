# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 15:13:33 2023

@author: Aishwarya
"""


import pandas as pd 
import matplotlib.pyplot as plt 

corona_dataset_csv = pd.read_csv('covid data analysis.csv')
print(corona_dataset_csv)

print(corona_dataset_csv.head(10))

print(corona_dataset_csv.shape )

columns = corona_dataset_csv.columns
print(columns)

corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace = True)
print(corona_dataset_csv.head(10))

corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
print(corona_dataset_aggregated)

#print(corona_dataset_aggregated.loc['China'].plot())

#corona_dataset_aggregated.loc['China'].plot()
#corona_dataset_aggregated.loc['Egypt'].plot()
#plt.legend()

#corona_dataset_aggregated.loc["China"].diff().plot()

print(corona_dataset_aggregated.loc["China"].diff().max())

#Datatraining
countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for c in countries :
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
max_infection_rates

#scatter plot
x=corona_dataset_csv['min'][:10]
y=corona_dataset_csv['max'][:10]
plt.scatter(x,y,color='green',cmap='Dark2',alpha=0.5)
plt.colorbar()
plt.show()