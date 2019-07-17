def fib():
    
    while True:
        
        try:
            userInput = input("Please enter a positive integer or type stop: ")
            if userInput == "Stop" or userInput == "stop":
                break
            sequenceNumber = int(userInput)
            
        except:
            print("Cannot be a string")
            continue
        
        if sequenceNumber < 0:
            print("Should be a positive integer")
            continue
            
        
        elif sequenceNumber == 0:
            print("Fib(0) = ",sequenceNumber)
            continue
            
        else:
            count = 1
            fibnumOld = 0
            fibnumNew = 1
            
            while count < sequenceNumber:
                update = fibnumOld + fibnumNew
                fibnumOld,fibnumNew = fibnumNew,update
                count += 1
            print("The Fib sequence = ",update)
