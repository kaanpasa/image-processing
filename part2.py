#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
array =np.zeros( (2,3) )
print(array)


# In[2]:


import numpy as np
array =np.ones( (1,5) )
print(array)


# In[4]:


n=int(input("Number of the inputs: "))
arr=[]
for i in range(0,n):
    elem=int(input("Enter the number: "))
    arr.append(elem)
avg=sum(arr)/n    
print("Average of the given numbers: ", round(avg,2))


# In[ ]:




