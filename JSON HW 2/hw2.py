import json
import matplotlib.pyplot as plt
import numpy as np
import os

gdp = []
y = []
x = []
u = ['2NY.GDP.MKTP.json']
for q in u:
        with open(q, encoding='ascii') as json_file:
                r = json_file.read()
                data = json.loads(r)
                gdp += data
                for key in gdp[1]:
                        y.append(key['value'])
                for year in range(2020, 1959, -1):
                        x.append(year)
                

gdp2 = []
y2 = []
x2 = []
u2 = ['US.NY.GDP.MKTP.json']
x3 = []
for q2 in u2:
        with open(q2, encoding='ascii') as json_file2:
                r2 = json_file2.read()
                data2 = json.loads(r2)
                gdp2 += data2
                for key2 in gdp2[1]:
                        y2.append(key2['value'])
                for year2 in range(2020, 1959, -1):
                        x2.append(year2)
                for year3 in range(2020, 1959, -5):
                        x3.append(year3)
x.reverse()
x2.reverse()
y.reverse()
y2.reverse()
a = np.arange(len(x2))  
a2 = np.arange(len(x3))  
fig, ax = plt.subplots()
width = 0.5
rects1 = ax.bar(a - width/2, y2, width, label='USA')
rects2 = ax.bar(a - width/2, y, width, label='China')
ax.set_ylabel('GDP (USD)')
ax.set_title('Gross Domestic Product (GDP) \n China V.S. USA GDP (1960 - 2020)')
ax.set_xticks(a)
ax.set_xticklabels(x)
plt.tick_params(axis='x', which='major', labelsize=6)
plt.xticks(rotation = 90)
plt.xlabel('Year')
ax.legend()
fig.tight_layout()
plt.show()



                                
