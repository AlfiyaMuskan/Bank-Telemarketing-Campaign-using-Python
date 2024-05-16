#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import matplotlib.pyplot as plt


# In[25]:


# Loading the Data
df = pd.read_csv(r"C:\Users\yash.dawra\Downloads\Python_Project\bank_marketing_updated_v1.csv")
df


# In[26]:


# Describe the Data Types
print(df.dtypes)


# In[27]:


# Summary Statistics (mean, median, standard deviation) for relevant columns
df.describe()


# In[28]:


# Examine the distribution of the target variable, indicating responses to the term deposit campaign


df['response'] = df['response'].replace('','NA')
count = df['response'].value_counts()
count


# In[29]:


# Distribution of age

print(df['age'].value_counts().sort_index().to_string())


# Summary statistics of age
print(df['age'].describe())  



# In[30]:


# Distribution of call duration 
print(df['duration'].value_counts().sort_index().to_string())



# Summary statistics of duration
print(df['duration'].describe())


# In[31]:


# Distribution of balance
print(df['balance'].value_counts().sort_index().to_string()) 


# Summary statistics of balance
print(df['balance'].describe())


# In[32]:


# Create a bar chart of marital status vs response
marital_grouped = df.groupby('marital')['response'].value_counts().unstack()
marital_grouped.plot.bar()
plt.title('Marital Status vs Response')
plt.xlabel('Marital Status')
plt.ylabel('Count')


# In[33]:


# Create a stacked bar chart of job/education level vs response
jobedu_grouped = df.groupby('jobedu')['response'].value_counts().unstack()
jobedu_grouped.plot.bar(stacked=True)
plt.title('Job/Education Level vs Response')
plt.xlabel('Job/Education') 
plt.ylabel('Count')


# In[34]:


# Create a heatmap of age and salary vs response
pivot_table = pd.pivot_table(df, values='response', index='age', columns='salary', aggfunc='count', fill_value=0)
plt.pcolor(pivot_table)
plt.colorbar()
plt.xlabel('Salary')
plt.ylabel('Age')
plt.title('Age vs Salary by Response')

plt.show()


# In[35]:


# Look at distribution of job type
print(df['jobedu'].value_counts().to_string()) 


# In[36]:


# Distribution of education level
df['education'] = df['jobedu'].apply(lambda x: x.split(',')[1])
print(df['education'].value_counts())


# In[37]:


# Distribution of marital status
print(df['marital'].value_counts().to_string()) 


# In[38]:


# Marital status vs response
marital_grouped = df.groupby(['marital', 'response'])['response'].count().unstack()
marital_grouped.plot.bar()
plt.title('Marital Status vs Response')
plt.xlabel('Marital Status')
plt.ylabel('Count')


# In[39]:


# Job/education level vs response 
jobedu_grouped = df.groupby(['jobedu', 'response'])['response'].count().unstack()
jobedu_grouped.plot.bar()
plt.title('Job/Education vs Response')
plt.xlabel('Job/Education')
plt.ylabel('Count')


# In[40]:


# Education level vs response
edu_grouped = df.groupby(['education', 'response'])['response'].count().unstack()
edu_grouped.plot.bar()
plt.title('Education vs Response')
plt.xlabel('Education Level')
plt.ylabel('Count')


# In[43]:


# Map response to numeric
df['response'] = df['response'].map({'yes': 1, 'no': 0})

# Groupby day  
daily = df.groupby('day')['response'].mean()

# Groupby month
monthly = df.groupby('month')['response'].mean() 

# Plot daily response  
daily.plot()
plt.xlabel('Day')
plt.ylabel('Response Mean') 
plt.title('Daily Campaign Response')

# Plot monthly response
monthly.plot() 
plt.xlabel('Month')
plt.ylabel('Response Mean')
plt.title('Monthly Campaign Response') 

plt.show()


# In[ ]:





# In[ ]:




