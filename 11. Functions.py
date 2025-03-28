'''
    A Function is of two types 

                               Functions in Python
                                  │
        ┌─────────────────────────┴──────────────────────────┐
        │                                                   │
  Built-in Functions                                  User-defined Functions
        │                                                   │
        ├─ Print, Len, Type, etc.                           ├─ Regular Functions
        │                                                   │       ├─ With Parameters
        │                                                   │       ├─ With Return Values
        │                                                   │
        ├─ Math Functions (abs, pow, round, etc.)           ├─ Recursive Functions
        │                                                   │
        ├─ String Functions (lower, upper, split, etc.)     ├─ Lambda Functions (Anonymous)
        │                                                   │
        ├─ List Functions (append, pop, sort, etc.)         ├─ Higher-order Functions
        │                                                   │       ├─ Functions as Arguments
        ├─ File Handling Functions (open, read, write, etc.)│       ├─ Returning Functions
        │                                                   │
        ├─ Other Specialized Functions (map, filter, zip, etc.)  

'''

# Function Defination

# def avg():

#     num1 = int(input("Enter marks: "))
#     num2 = int(input("Enter marks: "))
#     num3 = int(input("Enter marks: "))

#     average = (num1 + num2 + num3) / 3
#     print(f"The Average is {average}%")

# avg()



# Gree Function

# def greet():

#     name = input("Enter your name: ")
#     print(f"Hello {name}, Have a GOOD DAY!!!")

# greet()



# Default argument

def greet(name, ending="Thank-You"):

    print(f"Hello {name}, Have a GOOD DAY, {ending}!!!")

greet("Mohit")
