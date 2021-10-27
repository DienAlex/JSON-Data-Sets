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
ax.set_ylabel('GDP (Trillions)')
ax.set_title('China V.S. USA GDP')
ax.set_xticks(a)
ax.set_xticklabels(x)
plt.tick_params(axis='x', which='major', labelsize=6)
plt.xticks(rotation = 90)
plt.xlabel('Year')
ax.legend()
fig.tight_layout()
plt.show()



                                
                
                # print (p["value"])
                # print('GDP Per Year: ' + p['date'] + p['value'])


# gdp = []
# with open('NY.GDP.MKTP.json', encoding='ascii') as json_file:
#     data = json.load(json_file)
#     for p in data['GDP']:
#         for key in p:
#                 if "value" in key:
#                         c = gdp.append(key['value'])
#                         print (c)




# i = 0
# with open('pokedex.json') as json_file:
#         data = json.load(json_file)
#         for p in data['pokemon']:
#                 x = (p['height'])
#                 y = (p['name'])
#                 b = (p['weight'])
#                 f = p.items()
                # r = y.split("\n")
                # fig, ax = plt.subplots()
                # u = json.loads(y)
                # width = 0.35
                # print (u)
                # x1 = ax.bar(u, width, label='test')
                # xr = ax.bar(x, width, label='safdk;a')
                # ax.bar_label(x1, padding=3)
                # ax.bar_label(xr, padding=3)

                # u = len(int(float(y)))
                # pkmn = (r)
                # y_pos = np.arange(y)
                # ax.barh(y_pos, x, align='center')
                # ax.set_yticks(y_pos)
                # ax.set_xlabel('Performance')
                # plt.show()



                


                # for z in y:
                #         y.extend(z)
                #         print(y)
                # fig, ax = plt.subplots()
                # ax.bar(x, r)
                # plt.show()
                

                # for i in range(10):
                #         fig, ax = plt.subplots()
                #         ax.bar(x, y)

                #         plt.show()
                




# with open('pokedex.json') as json_file:
#       data = json.load(json_file)
#       x = (data['height'])
#       y = (data['name'])
#       plt.scatter(x, y)
#       plt.show()


# with open('pokedex.json') as json_file:
#        data = json.load(json_file)
#        for p in data['pokemon']:
#                x = list(p['height'])
#                y = list(p['name'])


#                plt.scatter(x, y)
               
# plt.show()

              



        #   print('name: ' + p['name'] + p['height'])


        



# u = ['NY.GDP.MKTP.json']
# p = ['pokedex.json']
# y = []
# n = 0 
# x = u[n]
# n += 1

# z = json.dumps(u)

# y += json.loads(z)
# print (z['value'])

# for x in u:
#     with open(u, encoding='ascii') as f:
#         text = f.read()
#         print (text)
#         y += json.loads(text)
# print (y)
# for date in y:
    
