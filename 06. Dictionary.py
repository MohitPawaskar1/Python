'''
    Dictionary is a collection of objects but in a key : value pair & is denoted by '{}',

    objects can be accesed by the object name, but not by indexing, 

    Dictionaries are mutable but can't contains duplicate keys.

            'key'  : 'value'
    dict = {'Brand':'BMW',
            'Model': 'M5 F90',
            'Color': 'Jet Black'}

'''

# Creating Simple Dictionary 

marks = {'Mohit':100,
         'Shubham':95,
         'Rohan':80,
         }

print(marks, type(marks))



# Accesing objects

print(marks['Mohit'])
print(marks.keys())
print(marks.values())



# Updating the Dictionary

marks.update({"Mohit":97, 'Karan':92})
print(marks)



# Get Function

print(marks.get('Rohan')) # If Key is not there it returns None
print(marks['Rohan']) # If Key is not there it returns Error
