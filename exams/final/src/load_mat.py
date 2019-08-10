import matplotlib.pyplot as plt
from scipy.io import loadmat
data = loadmat('cells.mat')
cells = data['cells']
days = [10,12,14,16,18,20,22]

tumor_cells = [0 for i in range(len(days))]



for day in range(len(days)):

    fig = plt.figure(figsize=(10, 10))
    #im=[0]*16
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('voxel number in x direction')
    ax.set_ylabel('voxel number in y direction')
    ax.set_title('Time = %s days. Brain MRI slices along Z-direction,Rat W09. No radiation treatment' %days[day])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.yaxis.labelpad = 20
    cbaxes = fig.add_axes([1.0, 0.1, 0.03, 0.8])
    for i in range(len(cells[0][0])):
        #for j in range(len(cells[0])):
            #for k in range(len(cells)):
        fig.add_subplot(4, 4, i+1)
        plt.imshow((cells[:,:,i,day]), cmap='RdBu')
                #plt.plot(cells[0:41][0:41][i][1], cells[0:41][0:41][i][1],'r')
    cbar = plt.colorbar(cax = cbaxes)

    fig.savefig("day%s.png" %days[day])


