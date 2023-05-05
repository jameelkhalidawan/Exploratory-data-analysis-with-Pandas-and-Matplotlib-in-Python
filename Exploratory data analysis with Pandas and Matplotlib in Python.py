#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd

# 1
drinks = pd.read_csv('Drinks.csv')

# 2.
print("Below is the head of the csv file\n\n")
print(drinks.head())
print("\n\nBelow is the tail of the csv file\n\n")
print(drinks.tail())
print("\n\nBelow is the default index, data types, and shape of the csv file\n\n")

# 3. 
print(drinks.index)
print(drinks.dtypes)
print(drinks.shape)
print("\n\nBelow is the beer_serving of the csv file\n\n")

# 4.
print(drinks['beer_servings'])
print("\n\nBelow is the mean of beer_serving of the csv file\n\n")

# 5.
mean_beer_servings = drinks['beer_servings'].mean()
print(mean_beer_servings)
print("\n\nBelow is the  number of occurrences of each 'continent' value of the csv file\n\n")

# 6.
continent_counts = drinks['continent'].value_counts()
print(continent_counts)
print("\n\nBelow is the  only include European countries with wine_servings > 300 of the csv file\n\n")

# 7.
print ( drinks[(drinks['continent'] == 'EU') & (drinks['wine_servings'] > 300)])


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt

# Read drinks.csv into a data frame called 'drinks'
drinks = pd.read_csv('drinks.csv')

# 1. Bar plot the values of total_litres_of_pure_alcohol consumption of each continent
continent_alcohol = drinks.groupby('continent')['total_litres_of_pure_alcohol'].sum()
continent_alcohol.plot(kind='bar')
plt.xlabel('Continent')
plt.ylabel('Total Litres of Pure Alcohol')
plt.title('Total Litres of Pure Alcohol Consumption by Continent')
plt.show()

# 2. Scatter plot of b/w beer_servings and spirit_serving
plt.scatter(drinks['beer_servings'], drinks['spirit_servings'])
plt.xlabel('Beer Servings')
plt.ylabel('Spirit Servings')
plt.title('Beer Servings vs Spirit Servings')
plt.show()

# 3. Plot the count of countries by continents
continent_counts = drinks['continent'].value_counts()
continent_counts.plot(kind='bar')
plt.xlabel('Continent')
plt.ylabel('Number of Countries')
plt.title('Count of Countries by Continent')
plt.show()


# In[ ]:




