#!/usr/bin/env python
# coding: utf-8

# In[6]:


nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


# In[3]:


x = [1,2,3,4,5,6,7,8,9]
oddlistCount=0
evenlistCount=0

for y in x:
    if y%2 == 0:
        evenlistCount=evenlistCount+1
    else:
        oddlistCount=oddlistCount+1
        
print('even numbers', evenlistCount)
print('odd numbers', oddlistCount)


# In[4]:


x = ('Edyoda')
print(x[::-1])


# In[ ]:




