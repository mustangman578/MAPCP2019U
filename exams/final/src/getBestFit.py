import math
from scipy.io import loadmat
import scipy.optimize as so
import numpy as np
data = loadmat('../data/cells.mat')
cells = data['cells']
times = [0,10,12,14,16,18,20,22]
cell_count = [0 for i in range(len(times))]

for day in range(len(times)-1):
    summ = 0
    for i in cells[:,:,:,day]:
        for j in i:
            for k in j:
                summ += k
                cell_count[day+1] = summ

print(cell_count)



def predictedNumber(lambd,c,time):
    return 100000.0 * math.exp(lambd*(1-(math.exp(-c*time))))

def leastSquares(param):
    SS = 0.0
    for i,time in enumerate(globals()['times']):
        lambd=param[0]
        c=param[1]
        x = predictedNumber(lambd,c,time)
        N = globals()['cell_count'][i]
        SS += (N - x)**2
    return SS 


best_fit = so.fmin(leastSquares,x0=[1,0])
lambd_new = best_fit[0]
c_new = best_fit[1]
print(lambd_new,c_new)
time_vec = np.linspace(0,22,100)
y = [0 for i in range(len(time_vec))]

for i in range(len(time_vec)):
    y[i] = predictedNumber(lambd_new,c_new,time_vec[i])

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.scatter(times,cell_count,label='Experimental Data')
plt.plot(time_vec,y,label='Gompertzian Fit')
plt.legend(fontsize='x-large')
plt.title('Gompertzian Fit to Rat\'s Brain Tumor Growth',fontsize=22)
plt.xlabel('Time[days]',fontsize=14)
plt.ylabel('Tumor Cell Count',fontsize=14)
plt.savefig('../results/best_fit.png')
