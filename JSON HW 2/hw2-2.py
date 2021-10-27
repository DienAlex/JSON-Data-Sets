import json 
import matplotlib.pyplot as plt
import numpy as np
i = 0
w = []
h = []
with open('pokedex.json') as json_file:
      data = json.load(json_file)
      for p in data['pokemon']:
                
                x = (p['height'])
                y = (p['name'])
                z = (p['weight'])
                x1 = x.split(" ")
                z1 = z.split(" ")
                x1.remove("m")
                z1.remove("kg")

                for z in range(len(z1)):
                    w.append(z1)
                for x in range(len(x1)):
                    h.append(x1)        

                    plt.scatter(h, w)
                    plt.title('Scatterplot of Pokemon Weight and Height') 
                    plt.xlabel('Height (M)')
                    plt.ylabel('Weight (KG)')
plt.show()


# i = 0
# with open('pokedex.json') as json_file:
#         data = json.load(json_file)
#         for p in data['pokemon']:
#                 x = (p['height'])
#                 y = (p['name'])
#                 b = (p['weight'])



#                 r = y.split("\n")
#                 fig, ax = plt.subplots()
#                 u = json.loads(y)
#                 width = 0.35
#                 print (u)
#                 x1 = ax.bar(u, width, label='test')
#                 xr = ax.bar(x, width, label='safdk;a')
#                 ax.bar_label(x1, padding=3)
#                 ax.bar_label(xr, padding=3)

#                 u = len(int(float(y)))
#                 pkmn = (r)
#                 y_pos = np.arange(y)
#                 ax.barh(y_pos, x, align='center')
#                 ax.set_yticks(y_pos)
#                 ax.set_xlabel('Performance')
#                 plt.show()



                


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
    
