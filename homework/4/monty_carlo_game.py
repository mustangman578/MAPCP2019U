import random
def getWins_choose():
    win = False

    choice = random.randint(1,3)
    #prize is 1
    
    if choice == 2 or choice == 3:
        win = True
    return win
        
    
def getWins_stay():
    win = False
    #prize is 1
    choice = random.randint(1,3)
    
    if choice == 1:
        win = True
    return win


    
    
    
    
n = 100000    
avg_choice = 0
avg_stay = 0



for i in range(n):
    Win_choose = getWins_choose()
    Win_stay = getWins_stay()
    if Win_choose == True:
        avg_choice += 1/n
    if Win_stay == True:
        avg_stay += 1/n
        
print(avg_choice)
print(avg_stay)
