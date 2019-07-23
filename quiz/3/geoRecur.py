def geoRec(m):
    if m == 0:
        return 1
    
    else:
        equation = 1.0/(2.0**m) + geoRec(m-1)
    return equation
