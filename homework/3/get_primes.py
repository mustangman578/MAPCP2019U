from math import sqrt

def is_prime(n):
    if n < 2: return False

    for i in range(2,int(sqrt(n)+1)):
       #print(i)
        if n%i == 0:
            return False
            break
    return True

def get_primes(n):
    count = 1
    while count < n:
        for i in range(n):
            check = is_prime(i)
            if check == True:
            print(i)
            count += 1



# The looping method is faster
