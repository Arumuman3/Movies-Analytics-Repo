#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[7]:


genreDateRevenue = pd.read_csv("C:/Users/Virtual Bull/Documents/Arumuman3/Portfolio/dataAnalyst/Movies/movies(genreDateRevenueCleanTwo).csv")
pd.set_option("display.max_rows", None)


# In[9]:


genreDateRevenue


# In[11]:


check = genreDateRevenue.isnull().sum()
print(check)


# In[16]:


checkTwo = np.isnan(genreDateRevenue["genreId"]).sum()
print("Nan in the genreId column is", checkTwo)


# In[15]:


checkThree = np.isnan(genreDateRevenue["month"]).sum()
print("Nan in the month column is", checkThree)


# In[17]:


checkFour = np.isnan(genreDateRevenue["day"]).sum()
print("Nan in the day column is", checkFour)


# In[18]:


checkFive = np.isnan(genreDateRevenue["year"]).sum()
print("Nan in the year column is", checkFive)


# In[19]:


checkSix = np.isnan(genreDateRevenue["revenue"]).sum()
print("Nan in the revenue column is", checkSix)


# In[20]:


genreDateRevenue.to_numpy()


# In[21]:


checkMean = np.mean(genreDateRevenue["revenue"])


# In[22]:


print(checkMean)


# In[24]:


genreDateRevenue.to_csv('C:/Users/Virtual Bull/Documents/Arumuman3/Portfolio/dataAnalyst/Movies/movies(genreDateRevenueThree)', encoding = 'utf-8', index = False)


# In[ ]:




