#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[2]:


df = pd.read_csv('C:/Users/Rakesh/Datasets/data.csv')


# In[3]:


df.head()


# In[4]:


df.dtypes


# In[5]:


df['Engine Fuel Type'].unique()


# In[8]:


df['Market Category'].value_counts()


# In[9]:


df=df.drop(['Engine Fuel Type','Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)


# In[10]:


df.head()


# In[13]:


df=df.rename(columns={'Engine HP':'HP','Engine Cylinders':'Cylinders','Transmission Type':'Transmission','Driven_Wheels':'Drive Mode', 'highway MPG':'MPG-H', 'city mpg':'MPG-C', 'MSRP': "Price" })


# In[14]:


df.head()


# # Dropping the duplicate rows

# In[15]:


duplicate_df=df[df.duplicated()]


# In[18]:


duplicate_df.shape


# In[19]:


df.count()


# In[20]:


df.isnull().sum()


# In[21]:


df.shape


# In[23]:


df=df.drop_duplicates()


# In[24]:


df.head()


# In[25]:


df.count()


# In[26]:


df=df.dropna()


# In[27]:


df.count()


# In[28]:


df.describe()


# In[32]:


sns.boxplot(x=df['Price'])


# In[33]:


sns.boxplot(x=df['HP'])


# In[34]:


sns.boxplot(x=df['Cylinders'])


# In[35]:


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3-Q1
print(IQR)


# In[36]:


df = df[~((df < (Q1 - 1.5* IQR)) | (df >(Q3 + 1.5 * IQR))).any(axis=1)]
df.shape


# In[37]:


df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title('Number of cars by make')
plt.ylabel('Number of cars')
plt.xlabel('Make');


# In[38]:


plt.figure(figsize=(10,15))
c=df.corr()
sns.heatmap(c,cmap='BrBG', annot=True)
c


# In[39]:


fig, ax=plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()

