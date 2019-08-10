import matplotlib.pyplot as plt
from scipy.io import loadmat
data = loadmat('../data/cells.mat')
cells = data['cells']
days = [0,10,12,14,16,18,20,22]
tumor_cells = [0 for i in range(len(days))]
boundary_cells = [0 for i in range(len(days))]


def getTotalCells():
    for day in range(len(days)-1):
        summ = 0
        for i in cells[:,:,:,day]:
            for j in i:
                for k in j:
                    summ += k
                    tumor_cells[day+1] = summ
                    
    return tumor_cells


getTotalCells()
plt.figure(figsize=(10,10))
plt.scatter(days,tumor_cells)
plt.xlabel('Time[days]',fontsize=14)
plt.ylabel('Tumor Cell Count',fontsize=14)
plt.title('Gompertzian Fit to Rat\'s Brain Tumor Growth',fontsize=22)
plt.legend('Data')
plt.savefig('../results/plot.png')
