from math import pi, exp, sqrt

def gaussian (x, mu, sig):
    return 1/(sqrt(2*pi)*sig)*exp(-((x-mu)/sig)**2/2)

gaussian(1,0,2)
