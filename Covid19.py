import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("covid19_patient_data.csv")
print(df)

print(df.head())

print(df.tail())

print(df.dtypes)

print(df.isnull().sum())
print("Total number of age group: ",df['Age'].max())

print("All the unique ages are: ",df['Age'].unique())

print("Total no of unique ages are: ",len(df['Age'].unique()))

max_bloodpressure=df['BloodPressure'].max()
print(max_bloodpressure)

print('Name of the team win by maximum runs= ',df.loc[df.BloodPressure==max_bloodpressure]['Insulin'])


#seaborn package - barplot(bydefault)
sns.countplot(x='ThroatInfections',data=df)
















#scatter plot
x=df['BloodPressure']
y=df['Insulin']
plt.scatter(x,y,color='green',cmap='Dark2',alpha=0.5)
plt.colorbar()
plt.show()





#xpoint=df['BMI']
#ypoint=df['Symptom']
#plt.plot(xpoint,ypoint)
#plt.xlabel('BMI')
#plt.ylabel('Symptom')
#plt.show()

#xpoint=df['Age']
#ypoint=df['Death']
#plt.bar(xpoint)
#plt.xlabel('Age')
#plt.ylabel('Death')
#plt.legend()
#plt.show()



