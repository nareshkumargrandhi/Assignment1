#!/usr/bin/env python
# coding: utf-8

# In[7]:


n=[]
for x in range(2000,3200):
    if (x%7==0) and (x%5!=0):
        n.append(str(x))
print (','.join(n))


# In[25]:


firstname = input("Input your First Name : ")
lastname = input("Input your Last Name : ")
print (" "+ lastname + " " + firstname)


# In[5]:


r=float(12/2)
pi = 3.1415926535897931
v=float((4.0/3.0)*pi*r**3)
print(v)


# In[10]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[27]:


values = input("Input some comma seprated numbers : ")
list = values.split(",")
print(list)


# In[29]:


sstr=str(input("Enter a string: "))
print("Reverse of the string is: ")
print(sstr[::-1])


# In[21]:


print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")

