#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import numpy as np


# In[28]:


genre = pd.read_csv('C:/Users/Virtual Bull/Documents/Arumuman3/Portfolio/dataAnalyst/Movies/movies(genreCleanTwo).csv')


# In[33]:


genre.to_numpy()


# In[45]:


genreNullValPdCheck = genre.isnull().sum()
print(genreNullVal)


# In[54]:


genreNullValNpCheck = np.isnan(genre["genreId"].sum())
print(genreNullValNpCheck)


# In[61]:


genre.duplicated()


# In[62]:


genre.drop_duplicates(inplace = True)


# In[64]:


genreDuplicateCheck = genre.duplicated().sum()
print(genreDuplicateCheck)


# In[65]:


genre


# In[70]:


genre.to_csv('C:/Users/Virtual Bull/Documents/Arumuman3/Portfolio/dataAnalyst/Movies/movies(genreCleaningThree)', encoding = 'utf-8', index = False)


# In[ ]:




