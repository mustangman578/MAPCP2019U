def Newton(f, dfdx, x, eps=1E-7, maxit=100):
    if not callable(f): raise TypeError( 'f is %s, should be function or class with __call__' % type(f) )
    if not callable(dfdx): raise TypeError( 'dfdx is %s, should be function or class with __call__' % type(dfdx) )
    if not isinstance(maxit, int): raise TypeError( 'maxit is %s, must be int' % type(maxit) )
    if maxit <= 0: raise ValueError( 'maxit=%d <= 0, must be > 0' % maxit )
    n = 0 # iteration counter
    while abs(f(x)) > eps and n < maxit:
        try:
            x = x - f(x)/float(dfdx(x))
        except ZeroDivisionError:
            raise ZeroDivisionError( 'dfdx(%g)=%g - cannot divide by zero' % (x, dfdx(x)) )
        n += 1
    return x, f(x), n



def test_Newton_div_by_zero():
    import math


    f = lambda x: math.cos(x)
    dfdx = lambda x: -(math.sin(x))
    x = 1
    try:
        Newton(f,dfdx,x)
        return True
    except:
        return False



test_Newton_div_by_zero()
