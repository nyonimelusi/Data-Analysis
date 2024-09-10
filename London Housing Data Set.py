#!/usr/bin/env python
# coding: utf-8

# This dataset is primarily centered around the housing market of London. It contains a lot of additional relevant data:
# 
# * Monthly average house prices
# * Yearly number of houses sold
# * Monthly number of crimes committed

# The data used here is from year 1995 to 2019 of each different area.

# This data is available as a CSV file, downloaded from Kaggle.

# We will analyze this data using the Pandas DataFrame.

# Here, random sets of quesitons are given for which we have to find correct results.

# This project is for analyzing this data set using python

# In[3]:


import pandas as pd


# In[4]:


data = pd.read_csv(r"C:\Users\DELL\Downloads\London Housing Data Set\Housing+Data.csv")


# In[5]:


data


# In[12]:


data.head(2)


# In[7]:


# 1. 
# df.count()
# df.isnull().sum()


# In[8]:


data.count()


# In[9]:


data.isnull().sum()


# In[10]:


# 2.
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.heatmap(df.isnull())
# plt.show()


# In[14]:


import seaborn as sns
import matplotlib. pyplot as plt


# In[15]:


sns.heatmap(data.isnull())
plt.show()


# # (A) Convert the Datatype of 'Date' column to Date-Time format.

# In[16]:


#data.dtypes
#data.date = pd.to_datetime(data.date)


# In[22]:


data.head()


# In[25]:


data.dtypes


# In[26]:


data.date = pd.to_datetime(data.date)


# In[27]:


data


# # (B.1) Add a new column ''year'' in the dataframe, which contains years only.

# In[28]:


# data['New_Column'] = df.Date_Column.dt.year


# In[29]:


data.head()


# In[30]:


data['year'] = data.date.dt.year
# data['month'] = data.date.dt.month


# In[33]:


data.head()


# # (B.2) Add a new column ''month'' as 2nd column in the dataframe, which contains month only.

# In[32]:


# df.insert( index , ‘new_column_name’, new_column_values)
# data.insert (1 , 'month' , data.date.dt.month)


# In[35]:


data.insert(1 ,'month' , data.date.dt.month)


# In[36]:


data.head()


# # (C) Remove the columns 'year' and 'month' from the dataframe.

# In[38]:


#data.drop(['month', 'year'] , axis=1 , inplace = True)


# In[39]:


data.head()


# In[40]:


data.drop(['month', 'year'] , axis=1 , inplace = True)


# In[41]:


data.head()


# # (D) Show all the records where 'No. of Crimes' is 0. And, how many such records are there ?

# In[43]:


# data[data.no_of_crimes == 0]
# len(data[data.no_of_crimes == 0])


# In[42]:


data.head()


# In[45]:


data.no_of_crimes == 0
#false means the condition is not satisfied


# In[46]:


data[data.no_of_crimes == 0]


# In[47]:


len(data[data.no_of_crimes == 0])
#use len function to show lenght of our output


# # (E) What is the maximum & minimum 'average_price' per year in england ?

# In[48]:


# df1 = data[data.area =='england']
# df1.groupby('year').average_price.max()/min()/mean()


# In[49]:


data['year'] = data.date.dt.year


# In[50]:


data.head()


# In[51]:


data.area == 'england'


# In[53]:


df1 = data[data.area == 'england']
df1


# In[55]:


# df1.groupby('year').average_price.max()/min()/mean()
data.groupby('year').average_price.max()


# In[56]:


data.groupby('year').average_price.min()


# In[57]:


data.groupby('year').average_price.mean()


# # (F) What is the Maximum & Minimum No. of Crimes recorded per area ?

# In[58]:


# data.groupby('area').no_of_crimes.max()
# data.groupby('area').no_of_crimes.min().sort_values(ascending= True)


# In[59]:


data.groupby('area').no_of_crimes.max()


# # (G) Show the total count of records of each area, where average price is less than 100000.

# In[60]:


#data[data.average_price < 100000].area.value_counts()


# In[64]:


data[data.average_price < 100000].area.value_counts()


# # By Melusi Nyoni

# In[ ]:




