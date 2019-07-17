eps = 1.0
while 1.0 != 1.0 + eps:
    print ('...............', eps)
    eps /= 2.0
print ('final eps:', eps)

'''
What this code is doing is taking a value eps and going through a while loop that will continue as long at 1 + eps does not equal 1.
But in the while loop, we divide the eps by 2 each time.  As we do this, the value eps will get smaller until it gets so small 
that python's precision essentially rounds it to 1.

'''
