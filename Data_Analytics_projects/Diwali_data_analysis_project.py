#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


pro=pd.read_csv('D:\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv',encoding='unicode_escape')


# In[5]:


pro.head()


# In[6]:


pro.info()


# In[7]:


pro.shape


# In[8]:


pro.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[10]:


pro.head()


# from above table we can see that Status and unnamesd1 column are drop. we drop this column because its contain 0 data that why we don't need this

# In[11]:


pro.isnull().sum()


# In[19]:


pro.dropna(inplace=True)


# In[23]:


pro.isnull()


# In[24]:


pro.isnull().sum()


# In[25]:


pro.shape


# In[30]:


pro['Amount']=pro['Amount'].astype('int')


# In[32]:


pro['Amount'].dtypes


# In[34]:


pro.columns


# In[37]:


pro.rename(columns={'Marital_Status':'Marriage'})


# In[40]:


pro.describe()


# In[42]:


pro[['Age','Orders','Amount']].describe()


# # Data analysis
# 

# <h3>Gender</h3>

# In[49]:


gen=sns.countplot(x='Gender',data=pro)

for i in gen.containers:
    gen.bar_label(i)


# In[55]:


gen=pro.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
gen


# In[56]:


gen=pro.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


sns.barplot(x="Gender",y="Amount",data=gen)


# <i>From above we can see that most of the buyer are female and even the purchasing power of female is greater than men

# <h3>Age group</h3>

# In[65]:


gen=sns.countplot(x='Age Group',data=pro ,hue='Gender')

for i in gen.containers:
    gen.bar_label(i)


# In[66]:


age=pro.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
age


# In[68]:


age=pro.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


sns.barplot(x="Age Group",y="Amount",data=age)


# <i>from above graph we can see that most of the buyer are of age group between 26-35 year respectively</i>

# <h3> State </h3>

# In[14]:


states=pro.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})

sns.barplot(x="State",y="Orders",data=states)


# In[33]:


state1=pro.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)


sns.set(rc={'figure.figsize':(15,5)})

sns.barplot(x="State",y="Amount",data=state1)


# from above graph we can see that unexpectedly most of the order and the buyer are from utter Pradesh , Maharastra , Karnataka respectively.

# <h3>Marital Status</b>

# In[18]:


Married=sns.countplot(x='Marital_Status',data=pro)
sns.set(rc={"figure.figsize":(7,5)})
for i in Married.containers:
    Married.bar_label(i)


# In[19]:


gen=sns.countplot(x='Marital_Status',data=pro ,hue='Gender')

for i in gen.containers:
    gen.bar_label(i)


# In[21]:


state1=pro.groupby(['Marital_Status',"Gender"],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)



sns.barplot(x="Marital_Status",y="Amount",data=state1,hue="Gender")


# From Above graph we can see that most of the buyer are married (women) and they have high purchasing power
# 
# 
# <h3>Product Category</h3>

# In[43]:


sns.set(rc={"figure.figsize":(15,5)})
product=sns.countplot(x="Product_Category",data=pro)


for i in product.containers:
    product.bar_label(i)


# In[27]:


product1=pro.groupby(["Product_Category"],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)



sns.barplot(x="Product_Category",y="Amount",data=product1)


# From Above graph we can see that most of the sold product from Food , Clothing ,Electronic Category
# 
# <h3>Occupation</h3>

# In[31]:


occ=sns.countplot(x="Occupation",data=pro)

for i in occ.containers:
    occ.bar_label(i)


# In[32]:


pocc1=pro.groupby(["Occupation"],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.barplot(x="Occupation",y="Amount",data=occ1)


# From Above graph we can see that most of the buyer are working in It , Healthcare, Aviation

# <h3>Product iD</h3>

# In[52]:


productids=pro.groupby(["Product_ID"],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.barplot(x="Product_ID",y="Orders",data=productids)


# # Conclusion

# <b>Marriage women age  between 26-35 years from Up , Maharastra, Karnataka working in IT, Food , Avation are more likely to buy a product from Food, clothing and Electronic catrgory<b>

# 

# 

# In[ ]:




