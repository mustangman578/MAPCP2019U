numbers = list(range(10))
print(numbers)

for n in numbers:
    i = len(numbers)//2
    del numbers[i]
    print ('n={}, del {}'.format(n,i), numbers)


    '''
    What this code is doing is creating list with 10 elements.
    This going through a for loop and creating a variable i
    which is the number of elements divided by 2.  Then it deletes
    whatever number that is from the list.  I think the werid 
    behavior comes from round errors.  After it divides an int by
    5, it then needs to divide 9 by 2 but this is then casted as 
    an int.  So 9//2 is rounded to 4.  Python then just deletes the 
    rounded value.
    '''
