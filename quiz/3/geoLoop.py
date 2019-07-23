def geoLoop(m):
    sum = 0
    for num in range(m+1):
        sum += 1.0/2**num
    return sum
