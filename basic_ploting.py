#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello world")


# In[4]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()


# In[6]:


xpoints = np.array([1, 18])
ypoints = np.array([3, 30])

plt.plot(xpoints, ypoints)
plt.show()


# In[7]:


xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()


# In[8]:


xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()


# In[9]:


ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()


# In[10]:


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()


# In[11]:


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()


# In[12]:


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()


# In[14]:


x = np.array([5])
y = np.array([5])

plt.scatter(x, y)
plt.show()


# In[15]:


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()


# In[16]:


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()


# In[18]:


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "black")
plt.show()


# In[19]:


x = np.random.normal(170, 10, 250)

print(x)


# In[20]:


plt.hist(x)
plt.show() 


# In[21]:


import sys
matplotlib.use('Agg')
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


# In[22]:


import mysql.connector

