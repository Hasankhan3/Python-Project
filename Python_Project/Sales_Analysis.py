#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[68]:


df = pd.read_csv(r"C:\Users\Gopi\OneDrive\Desktop\Hasan\Python_Project\Diwali Sales Data.csv", encoding = "unicode_escape")


# In[69]:


df


# In[70]:


df.head()


# In[71]:


df.columns


# In[72]:


df.info


# In[73]:


df.drop(["Status", "unnamed1"], axis =1 , inplace = True)


# In[74]:


df.info()


# In[75]:


# to get the null values and their counts
pd.isnull(df).sum()


# In[76]:


# to drop null values
df.dropna(inplace = True)


# In[77]:


pd.isnull(df).sum()


# #Explotary Data Ananysis (EDA)

# In[78]:


df.columns


# In[79]:


# plot without labels
a = sns.countplot(x= "Gender", data = df)


# In[80]:


# plot with labels
a = sns.countplot(x = "Gender", data = df)
for bars in a.containers:
    a.bar_label(bars)


# In[81]:


sales_gender = df.groupby(["Gender"], as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)


# In[82]:


sales_gender


# In[83]:


sns.barplot(x = "Gender", y = "Amount", data = sales_gender)


# In[84]:


ag = sns.countplot(x = "Age Group",hue = "Gender", data = df)


# In[85]:


# plot with label
ag = sns.countplot(x = "Age Group",hue = "Gender", data = df)
for bars in ag.containers:
    ag.bar_label(bars)


# In[86]:


df.columns


# In[87]:


# total number of orders from top 10 states.
st = df.groupby(["State"], as_index = False)["Orders"].sum().sort_values(by = "Orders",ascending = False).head(10)
st


# In[88]:


sns.barplot(data = st, x = "State", y = "Orders")
sns.set(rc={"figure.figsize":(20,5)})


# In[89]:


# Here we have set the plot size and all the states are properly visible.
sns.barplot(data = st, x = "State", y = "Orders")
sns.set(rc={"figure.figsize":(20,5)})


# In[90]:


df.columns


# In[91]:


ms = sns.countplot(data = df, x = "Marital_Status")
for bars in ms.containers:
    ms.bar_label(bars)
sns.set(rc={"figure.figsize":(5,5)})


# In[92]:


mt = df.groupby(["Marital_Status","Gender"], as_index = False)["Amount"].sum().sort_values(by = "Amount",ascending = False)
mt


# In[93]:


sns.barplot(x = "Marital_Status", y = "Amount", data = mt, hue = "Gender")


# In[107]:


oc = sns.countplot(data = df, x = "Occupation")
sns.set(rc={"figure.figsize":(20,5)})
for bars in oc.containers:
     oc.bar_label(bars)


# In[95]:


oc1 = df.groupby(["Occupation"], as_index = False)["Amount"].sum().sort_values(by = "Amount",ascending = False)


# In[96]:


oc1


# In[108]:


sns.barplot(x = "Occupation", y = "Amount", data = oc1)
sns.set(rc={"figure.figsize":(20,5)})


# **From above graph we can see that most of the buyers are working in IT Sector.**

# In[98]:


df.columns


# In[99]:


df["Product_Category"]


# In[110]:


cat = sns.countplot(data = df, x = "Product_Category")
sns.set(rc={"figure.figsize":(25,8)})
for bars in cat.containers:
    cat.bar_label(bars)


# **From the above chart we can analyse that Clothing & Apparel, Food and Electronic Gagdets are the top 3 category of customers purchases.**

# In[101]:


cat1 = df.groupby(["Product_Category"], as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending = False).head(10)


# In[102]:


cat1


# In[103]:


sns.barplot(x = "Product_Category", y = "Amount", data = cat1)
sns.set(rc={"figure.figsize":(20,5)})


# **From above graph we can analyse that most of the sold products are fromn food, clothing & Appareal and Electronics & Gadgets.**

# In[104]:


sp = df.groupby(["Product_ID"], as_index = False)["Orders"].sum().sort_values(by = "Orders", ascending = False)


# In[105]:


sp


# In[106]:


fig1,ax1 = plt.subplots(figsize = (12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending = False).plot(kind = 'bar')


# **CONCLUSION**

# **Married women age group 26-35 years from UP, Maharashtra and Karnataka workin in IT, Healthcare and Aviaton sector are more likely to buy products from food, clothing & Electronic categories.**
