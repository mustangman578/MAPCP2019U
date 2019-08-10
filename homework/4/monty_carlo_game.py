import random
from matplotlib import pyplot as plt
import numpy as np

def get_chance_of_win_switch():
    #prize is 1
    choice = random.randint(1,3)
    if choice == 2 or choice == 3:
        return 1.0
    else:
        return 0.0

def get_chance_of_win_stay():
    #prize is 1
    choice = random.randint(1,3)
    if choice == 1:
        return 1.0
    else:
        return 0.0

nsim = 100000
avg_chance_of_win_stay = np.zeros(nsim)
avg_chance_of_win_switch = np.zeros(nsim)
experiment_number = [i for i in range(0,nsim)]

avg_chance_of_win_stay[0] = get_chance_of_win_stay()
avg_chance_of_win_switch[0] = get_chance_of_win_switch()
for i in experiment_number[1:]:
    avg_chance_of_win_stay[i] = (i*avg_chance_of_win_stay[i-1] + get_chance_of_win_stay()) / (i+1)
    avg_chance_of_win_switch[i] = (i*avg_chance_of_win_switch[i-1] + get_chance_of_win_switch()) / (i+1)

print( "  average chance of winning by staying: {}".format(avg_chance_of_win_stay[-1]) )
print( "average chance of winning by switching: {}".format(avg_chance_of_win_switch[-1]) )

plt.semilogx(experiment_number,avg_chance_of_win_stay)
plt.semilogx(experiment_number,avg_chance_of_win_switch)
#plt.xscale('log')
plt.show()
