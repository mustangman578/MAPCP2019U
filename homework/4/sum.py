import sys

num = sys.argv[1:]
myStr = ""

for string in num:
    myStr += string + " "


my_list = [line for line in num]

summ = sum([float(line) for line in my_list])

print("The sum of", myStr, "is ", summ)
