#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("2019-XTern- Work Sample Assessment Data Science-DS.csv")
x = data.xcoordinate
y = data.ycoordinate
z = data.power_level

plt.scatter(x, y, c = z * 1000, s = z * 100, alpha = 0.1)
plt.show()


# In[58]:


import math
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("2019-XTern- Work Sample Assessment Data Science-DS.csv")
distance = pd.Series([])

for i in range(len(data)):
    distance[i] = math.sqrt(math.pow(20.19-data["xcoordinate"][i], 2) +
                            math.pow(20.19-data["ycoordinate"][i], 2) )
    
data.insert(4, "distance", distance)

d = data.distance
x0 = data.loc[data.power_level==0, 'distance']
x1 = data.loc[data.power_level==1, 'distance']
x2 = data.loc[data.power_level==2, 'distance']
x3 = data.loc[data.power_level==3, 'distance']
x4 = data.loc[data.power_level==4, 'distance']
x5 = data.loc[data.power_level==5, 'distance']

kwargs = dict(alpha=0.5, bins=100)

plt.hist(x0, **kwargs, color='r', label='power 0')
plt.hist(x1, **kwargs, color='lightsalmon', label='power 1')
plt.hist(x2, **kwargs, color='yellow', label='power 2')
plt.hist(x3, **kwargs, color='greenyellow', label='power 3')
plt.hist(x4, **kwargs, color='g', label='power 4')
plt.hist(x5, **kwargs, color='b', label='power 5')
plt.legend();


# In[ ]:




