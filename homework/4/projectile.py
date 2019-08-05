import sys

try:
    v0 = float(sys.argv[1]); g = 9.81; t = float(sys.argv[2])
except:
    v0 = float(input("v0 = ?\n"))
    t = float(input("t = ?\n"))
if t < 0 or t > 2*v0/g:
    raise ValueError("t = %f is a non-physical value" %t)
else:
    y = v0*t - 0.5*g*t**2
    print(y)
        
