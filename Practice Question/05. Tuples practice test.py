# Q1. Check that a tuple type cannot be changed in python.

my_tuple = ("Mohit", 22.9, 200000, True, [1,2,3], {"Car":"BMW"})
print(my_tuple)
# my_tuple[0] = "Rohit"

'''

my_tuple[0] = "Rohit" trying to change the object of index 1 to "Rohit" will through an error

Traceback (most recent call last):
  File "d:\Python\Practice Question\4,5 . Listd and tuples practice test.py", line 50, in <module>
    my_tuple[0] = "Rohit"
    ~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment

'''



# Q2. WAP to count the number of zeros in the following tuple:

a = (7, 0, 8, 0, 0, 9)

count = a.count(0)
print(f"The count of 0 in the tuple is {count}")



# Q3. WAP program that takes five numbers as input from the user, stores them in a tuple, and then:

# - Prints the tuple.

# - Finds and prints the maximum and minimum values in the tuple.

# - Calculates and prints the sum of all elements.

my_tup = []

n1 = int(input("Enter number: "))
my_tup.append(n1)
n2 = int(input("Enter number: "))
my_tup.append(n2)
n3 = int(input("Enter number: "))
my_tup.append(n3)
n4 = int(input("Enter number: "))
my_tup.append(n4)
n5 = int(input("Enter number: "))
my_tup.append(n5)

new_tuple = tuple(my_tup)
print(f"The Tuple is {new_tuple}")

print(f"The maximum number in the Tuple is {max(new_tuple)}")
print(f"The minimum number in the Tuple is {min(new_tuple)}")
print(f"The sum of all the numbers in the Tuple is {sum(new_tuple)}")
      

