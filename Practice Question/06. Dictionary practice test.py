# Q1. WAP to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

my_dict = {'Paani':'Water',
           'Gaadi':'Car',
           'Makaan': 'House'}

word = input("Enter a word you want to look for: ")

print(f"The meaning of Hindi word {word} is {my_dict[word]} in English")



# # Q2. What is the type of s?

s = {}

print(f"The type of {s} is {type(s)}")



# Q3. Create an empty dictionary. Allow 4 friends to enter thier favorite languageas as value and use key as their names.
#     Assume that the names are unique.

friends = {}

name = input("Enter your name: ")
sub = input(f"Enter {name}'s fav subject: ")
friends.update({name:sub})

name = input("\nEnter your name: ")
sub = input(f"Enter {name}'s fav subject: ")
friends.update({name:sub})

name = input("\nEnter your name: ")
sub = input(f"Enter {name}'s fav subject: ")
friends.update({name:sub})

name = input("\nEnter your name: ")
sub = input(f"Enter {name}'s fav subject: ")
friends.update({name:sub})
print(f"\n{friends}")


# Q4. If the names of 2 friends are same; what will happen to program in Q3?

'''
    Enter your name: Mohit
    Enter Mohit's fav subject: C

    Enter your name: Rohan
    Enter Rohan's fav subject: CPP

    Enter your name: Mohit
    Enter Mohit's fav subject: Machine Learning

    Enter your name: Karan
    Enter Karan's fav subject: Rust

    {'Mohit': 'Machine Learning', 'Rohan': 'CPP', 'Karan': 'Rust'}

    The old value simply gets replace by new value if the keys are same

'''



# Q5. If Languages of 2 friends are same; what will happen to program in Q3?
 
'''
    Enter your name: Mohit
    Enter Mohit's fav subject: Python

    Enter your name: Rohan
    Enter Rohan's fav subject: C

    Enter your name: Karan
    Enter Karan's fav subject: Python

    Enter your name: Raj
    Enter Raj's fav subject: Rust
    {'Mohit': 'Python', 'Rohan': 'C', 'Karan': 'Python', 'Raj': 'Rust'}

    Nothing happens as values can be duplicate in a dictionary

 '''
