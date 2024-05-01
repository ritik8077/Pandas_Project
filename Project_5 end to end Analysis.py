#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


import pandas as pd
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# In[3]:


import warnings
warnings.filterwarnings('ignore')


# # Gather and clean the data

# In[10]:


data = pd.read_csv('superstore_dataset2011-2015.csv', encoding='ISO-8859-1')


# # Explore the data
# 

# # 1. Display Top 5 Rows of Dataset

# In[16]:


data.head(5)


# In[60]:


data[data['Ship Mode'].str.contains('Standard Class')]


# In[70]:


data['Average Sales'] = data.groupby(['Sub-Category'])['Sales'].mean()


# In[71]:


data.head(2)


# In[74]:


data['total_sum'] = data.groupby(['Sub-Category'])['Sales'].sum()


# In[75]:


data.head(3)


# In[ ]:





# # 2. Check the last 5 rows of the dataset

# In[12]:


data.tail()


# # 3. Find Shape of our Dataset

# In[13]:


print('number of rows:',data.shape[0])
print('number of Columns:',data.shape[1])


# # 4. Get information About Our Dataset 

# In[14]:


data.info()


# # 5. Check Null Values In the Dataset

# In[17]:


data.isnull().sum()


# # 6. Check for Duplicate Data and Drop Them

# In[18]:


data.duplicated().any()


# In[ ]:





# # 7. Get Overall Statistics About The Dataset

# In[19]:


data.describe()


# In[21]:


data.describe(include='all')


# # 8. Drop unnecessary Columns

# In[22]:


data.columns


# In[24]:


data = data.drop(['Row ID', 'Order ID', 'Customer ID', 'Postal Code'],axis=1)


# In[25]:


data.columns


# In[ ]:





# # Hypothesis
# 
# ## Hypothesis 1. Technology products have the highest profit margin compared to other product categories.

# In[26]:


data.columns


# In[29]:


cat_profit = data.groupby('Category')['Profit'].sum()
cat_profit.plot(kind='bar')
plt.title('Profit by Category')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.show

# Conclusion : The hypothesis is supported as tech products have the highest
# profit margin of the three categories


# ## Hypothesis 2. The East region has the highest sales compared to other regions.

# In[30]:


data.columns


# In[34]:


reg_sales = data.groupby('Region')['Sales'].sum()
reg_sales.plot(kind='bar')
plt.title('Tatal sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show

# hypothesis does not supported as the east region has the highest sales


# In[ ]:





# ## Hypothesis 3. Sales are higher during certain months of the year .

# In[35]:


data.columns


# In[37]:


data['Order Month'] = pd.DatetimeIndex(data['Order Date']).month


# In[42]:


month_sales = data.groupby(['Order Month'])['Sales'].sum()
month_sales.plot(kind='line')
plt.title("Total sales by month")
plt.xlabel('Order Month')
plt.ylabel('Sales')
plt.show

# conclusion : our hypothesis is supported as sales are higher 
# during certain months of year


# ## Hypothesis 4: Orders with same-day shipping have the lowest rate of returned products. 

# In[43]:


data.columns


# In[ ]:





# In[ ]:





# In[ ]:





# ## Hypothesis 5: The company's profit is more on weekdays than on weekends 

# In[51]:


data.columns


# In[56]:


data['Order Day'] = pd.DatetimeIndex(data['Order Date']).day_name()

day_profit = data.groupby(['Order Day'])['Profit'].sum()
day_profit.plot(kind='bar')
plt.title('Total profit by the day of the week')
plt.xlabel('Order Day')
plt.ylabel('Profit')
plt.show

# conclusion : The hypothesis is supported as companys profit 
# is higher on weekdays compared to weekends


# In[ ]:





# In[ ]:




