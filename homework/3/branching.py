abbr = input ("What is the three letter abbreviation of this course? ")


answer_status = ('correct' if abbr == "ECL" else 'wrong')

if answer_status=='correct':
    print('Your answer is correct!')
else:
    print("wrong buddy...try again"
