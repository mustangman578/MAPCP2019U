from math import sqrt
for n in range(1, 60):
    r_org = 2.0
    r = r_org
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r ** 2
    print ('With {} times sqrt and then {} times **2, the number {} becomes: {:.16f}'.format(n,n,r_org,r))


    '''
    What this code is doing is take the square root of two and then squaring is again.  As it does this, it goes through a for loop square rooting and resquaring up to the specified number of times.
    However, the more times we square, the smaller the round error gets and that's why resquaring doesn't arrive back at our original value.
    '''
