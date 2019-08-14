import os
import matplotlib.pyplot as plt

x_list = []
y_list = []
filelist = os.listdir()
for i in filelist:
    if i.endswith('.txt'):
        with open(i,'r',encoding='ascii') as y:
            for line in y:
                data = line.split('\\n')
                for i in data:
                    y_value = i[0:5]
                    x_value = i[7:13]
                    x_list.append(x_value)
                    y_list.append(y_value)

plt.scatter(x_list,y_list)
plt.show()
