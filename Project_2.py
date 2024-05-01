#!/usr/bin/env python
# coding: utf-8

# In[62]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('train.csv')


# In[3]:


data.head(5)


# In[5]:


data.tail(3)


# In[6]:


data.shape


# In[11]:


print("number of rows:",data.shape[0])
print("number of columns",data.shape[1])


# In[13]:


data.info()


# In[14]:


data.describe()


# In[7]:


data.describe(include='all')


# In[8]:


# Data filtering


# In[ ]:





# In[9]:


data.columns


# In[12]:


data[['Name', 'Age']]


# In[16]:


sum(data['Sex'] == 'male')


# In[4]:


data[data['Sex'] == 'male']


# In[5]:


data.columns


# In[8]:


data[data['Survived']==1]


# In[9]:


sum(data['Survived']==1)


# In[10]:


# check null values


# In[11]:


data.isnull().sum()


# In[12]:


sns.heatmap(data.isnull())


# In[13]:


per_missing = data.isnull().sum() * 100 / len(data)


# In[14]:


per_missing


# In[15]:


# drop columns


# In[ ]:





# In[16]:


data.drop('Cabin',axis=1,inplace=True)


# In[17]:


data.isnull().sum()


# In[22]:


data.columns


# In[20]:


data['Embarked'].mode()


# In[23]:


data['Embarked'].fillna('S',inplace=True)


# In[24]:


data.isnull().sum()


# In[25]:


data['Age'].fillna(data['Age'].mean(),inplace=True)


# In[26]:


data.isnull().sum()


# In[27]:


# Categorical Data Encoding


# In[28]:


data.head()


# In[29]:


data['Sex'].unique()


# In[30]:


data['Gender'] = data['Sex'].map({'male':1, 'female':0})


# In[31]:


data.head(2)


# In[32]:


x=data['Sex'].map({'male':1, 'female':0})


# In[33]:


data.insert(5,'Gender_New',x)


# In[34]:


data.head(1)


# In[ ]:





# In[37]:


data['Embarked'].unique()


# In[38]:


pd.get_dummies(data,columns=['Embarked'])


# In[41]:


data1 = pd.get_dummies(data,columns=['Embarked'],drop_first=True)


# In[42]:


data1.head(2)


# In[43]:


# unvariated analysis


# In[ ]:





# In[46]:


# Q1

data.columns


# In[49]:


data['Survived'].value_counts()


# In[81]:


sns.countplot(x='Survived',data=data)


# In[ ]:





# In[59]:


data.columns


# In[60]:


data['Pclass'].value_counts()


# In[80]:


sns.countplot(x='Pclass' ,data=data)


# In[ ]:





# In[69]:


data['Sex'].value_counts()


# In[71]:


plt.hist(data['Age'])


# In[76]:


sns.boxplot(data['Age'],orient='v')


# In[77]:


# Bivariate analysis


# In[ ]:





# In[78]:


data.columns


# In[79]:


sns.barplot(x='Sex' ,y='Survived' ,data=data)


# In[82]:


sns.barplot(x='Pclass' ,y='Survived' ,data=data)


# In[83]:


# Feature Engineering


# In[84]:


data.columns


# In[87]:


data['Family_Size'] = data['SibSp'] + data['Parch']


# In[88]:


data.head(2)


# In[89]:


data.columns


# In[92]:


data['Fare_per_person'] = data['Fare'] / (data['Family_Size'] + 1)


# In[93]:


data.head(2)


# In[ ]:




