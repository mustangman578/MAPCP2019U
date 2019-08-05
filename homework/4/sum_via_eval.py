import sys

num = sys.argv[1:]
summ = 0

myStr = ""

for string in num:
    myStr += string + " "

for number in num:
    summ += eval(number)

print("The sum of ",myStr,"is ", summ)


