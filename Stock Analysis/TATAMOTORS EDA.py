#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')



# In[42]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import seaborn as sns
from datetime import datetime


# In[43]:


df  = pd.read_csv('S:\\GUVI\\BUSINESS ANALYSIS\\Stock Analysis\\Quote-Equity-TATAMOTORS-EQ-10-03-2021-to-10-03-2023.csv')


# In[44]:


df.head()


# In[45]:


df.isnull().sum()


# In[46]:


df.shape


# In[47]:


df.info()


# In[54]:


df['Date'] = pd.to_datetime(df['Date'])


# In[55]:


print(df.dtypes)


# In[56]:


df.describe()


# In[57]:


# Line plot of stock price over time
plt.plot(df.index, df['close'])
plt.xlabel('Date')
plt.ylabel('close')
plt.title('Stock Price over Time')
plt.show()


# In[58]:


# Histogram of daily returns
returns = (df['close'] - df['close'].shift(1)) / df['close'].shift(1)
sns.histplot(returns, kde=True)
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')
plt.title('Histogram of Daily Returns')
plt.show()


# In[63]:


# Correlation matrix
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()


# In[64]:


# Scatterplot of two variables
sns.scatterplot(data=df, x='VOLUME', y='close')
plt.xlabel('Volume')
plt.ylabel('Closing Price')
plt.title('Scatterplot of Volume vs Closing Price')
plt.show()


# In[ ]:




