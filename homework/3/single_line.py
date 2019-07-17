(first,last,univ) = ((input('Enter the first name, last name, and the city of the person (comma-separated): ').replace(' ','')).lower()).split(',')

def dummy(i):
    j = (i if i in range(0,3) else 'j is not in [0,1,2]') 
    return j
