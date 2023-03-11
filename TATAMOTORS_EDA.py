#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')



# In[67]:


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np 
import seaborn as sns
from datetime import datetime


# In[85]:


df  = pd.read_csv('S:\\GUVI\\BUSINESS ANALYSIS\\Stock Analysis\\Quote-Equity-TATAMOTORS-EQ-10-03-2021-to-10-03-2023.csv')


# In[86]:


df.head()


# In[87]:


df.isnull().sum()


# In[88]:


df.shape


# In[89]:


df.info()


# In[90]:


df['Date'] = pd.to_datetime(df['Date'])


# In[91]:


print(df.dtypes)


# In[92]:


df.describe()


# In[70]:


# Line plot of stock price over time

# Set the figure size
plt.figure(figsize=(18, 6))

# Plot the data
plt.plot(df['Date'], df['close'])

# Set the x-axis locator and formatter
months = mdates.MonthLocator()  # Every month
date_format = mdates.DateFormatter('%b %Y')  # Format the date as Month Year
plt.gca().xaxis.set_major_locator(months)
plt.gca().xaxis.set_major_formatter(date_format)

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Price Over Time')

# Show the plot
plt.show()


# In[58]:


# Histogram of daily returns
returns = (df['close'] - df['close'].shift(1)) / df['close'].shift(1)
sns.histplot(returns, kde=True)
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')
plt.title('Histogram of Daily Returns')
plt.show()


# In[93]:


# Correlation matrix
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()


# In[96]:


# Scatterplot of two variables
sns.scatterplot(data=df, x='VALUE', y='close')
plt.xlabel('Value')
plt.ylabel('Stock Price')
plt.title('Scatterplot of Value vs Stock Price')
plt.show()


# In[ ]:




