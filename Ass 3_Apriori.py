#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
from apyori import apriori
items = ['i1','i2','i3','i4','i5']
er = []
i = input("Do you want to add transaction ?(y/n) ")
while(i == 'y'):
    l = []
    a  = input("Is i1 purchased ?(y/n) ")
    if(a == 'y'):
        l.append(items[0])
    b  = input("Is i2 purchased ?(y/n) ")
    if(b == 'y'):
        l.append(items[1])
    c  = input("Is i3 purchased ?(y/n) ")
    if(c == 'y'):
        l.append(items[2])
    d  = input("Is i4 purchased ?(y/n) ")
    if(d == 'y'):
        l.append(items[3])
    e  = input("Is i5 purchased ?(y/n) ")
    if(e == 'y'):
        l.append(items[4])
    er.append(l)
    i = input("Do you want to add transaction ?(y/n) ")
ar = apriori(er,min_confidence=0.7)
res = list(ar)
print(len(res))
#print(er)
#print(res)
    


# In[ ]:


get_ipython().system('pip install apyori')

