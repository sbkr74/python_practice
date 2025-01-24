person={
    'first_name': 'Shubham',
    'last_name': 'Biruly',
    'age': 25,
    'country': 'India',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Dumbisai',
        'zipcode': '833201'
    }
    }

if 'skills' in person.keys():
    if 'p' in person['skills']:
        print(person['skills'])
    else:
        print(person['skills'],"\n Java as skill not persent")
else:
    print("nothing")
