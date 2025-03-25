#  Differentg types of Data types

name = "BMW M5 F90" # String Data type
top_speed = 305 # Integer Data type
engine = 4.3 # Float Data type
m_car = True # Booleon Data type

# printing all the Data with their types

print(f"{name} is of {type(name)} data type")
print(f"{top_speed} km/hr is of {type(top_speed)} data type")
print(f"{engine} cc is of {type(engine)} data type")
print(f"{m_car} is of {type(m_car)} data type")


# Boolean Values & its table
'''
    Whenever "OR" is used if one value is True it returns True

    Whenever "AND" is used if both values are True then only it returns True else Fale

'''
# Truth table of 'OR'
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'AND'
print("\nTrue and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False ands ", False and False)



# Type Conversion
a = "3.14"
b = float(a)
print(f"\nBefore conversion {a} is a {type(a)} type")
print(f"After converting {b} is a {type(b)} type")



# Using INPUT function
'''
    Always define the input type
    else by default it will be passed
    as string

'''

a = int(input("Enter 1st Number: ")) 
b = int(input("Enter 2nd Number: "))

print("Number a is ", a)
print("Number b is ", b)
print(f"Sum of {a} & {b} is  {a + b}")