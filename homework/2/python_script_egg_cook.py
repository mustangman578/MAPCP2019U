from math import log, pi

p = 1.038
c = 3.7
k = 5.4e-3
Tw = 100
Ty = 70
a = c*p**(1/3)
b = k*((pi)**(2))*(((4*pi)/3)**(2/3))

def time (M,T0):
    return ((((M)**(2/3))*a)/b)*log((0.76)*((T0-Tw)/(Ty-Tw)))

largeEgg_4_degrees = time(67,4)
largeEgg_20_degress = time(67,20)

print("Large Egg at 4 degress is", largeEgg_4_degrees)
print("Large Egg at 20 degress is", largeEgg_20_degress)
