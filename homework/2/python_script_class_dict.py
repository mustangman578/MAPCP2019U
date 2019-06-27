list = [
'Christian-Andrew Bagby-wright',
'Matthew Chrysler',
'Niyousha Davachi',
'Pauline Dredger',
'Marcos Guillen',
'Lauren Kuffel',
'Shashank Kumbhare',
'Hany Mahdy',
'Sarah Moorman',
'Andrew Myers',
'Joshua Osborne',
'Rebecca Proni',
'Amir Shahmoradi',
'Carolina Vedovato',
]

class_dict ={}


for person in list:
    if person == 'Amir Shahmoradi':
        class_dict.update({'Amir Shahmoradi':'instructor'})
    else:
        class_dict.update({person:'student'})
        
print(class_dict)
