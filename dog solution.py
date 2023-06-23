#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:


df=pd.read_csv(r'C:\Users\LIBITHARAN\Desktop\jupyter\dog.csv')


# In[12]:


df


# In[13]:


df.info()


# In[14]:


df.describe()


# In[15]:


df.drop_duplicates()


# In[19]:


df.sample()


# In[20]:


df.head()


# In[21]:


df.tail()


# In[22]:


df.shape


# In[23]:


df.sample()


# In[25]:


df.reset_index()


# In[26]:


df.columns


# In[28]:


df.iat[2,3]


# In[29]:


df.iloc[:,[2,4]]


# In[31]:


df.at[4,'Position']


# In[32]:


df.at[100,'Breed']


# In[33]:


df.at[123,'Position']


# In[34]:


df.sort_values('Breed')


# In[35]:


df.nlargest(1,'Year')


# In[36]:


df.nlargest(10,'Year')


# In[38]:


df.nsmallest(10,'Year')


# In[39]:


df.sample(frac=0.2)


# In[40]:


df.melt()


# In[41]:


df.dtypes


# In[42]:


df.rename(columns={'Breed':'Brand'})


# In[43]:


df.isna().sum()


# In[44]:


print("Position:",df['Position'].unique())
print("Registrations:",df['Registrations'].unique())


# In[45]:


df['Registrations'].value_counts()


# In[46]:


df.Breed.value_counts()


# In[48]:


df.sum()


# In[49]:


df.count()


# In[50]:


df.median()


# In[51]:


df.mean()


# In[52]:


df.min()


# In[53]:


df.max()


# In[54]:


df.var()


# In[55]:


df.std()


# In[56]:


data=df.copy()
dog_data=data[data['Breed']=='v Labrador Retriever']
dog_data.describe()


# In[57]:


df['Year'].value_counts()


# In[58]:


df['Year'].value_counts().plot(kind='pie')


# In[ ]:




