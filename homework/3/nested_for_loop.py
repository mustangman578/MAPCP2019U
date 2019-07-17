q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

string = ""
for array in q:
    for letter in array:
        string += letter

print(string)
