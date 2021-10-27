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


