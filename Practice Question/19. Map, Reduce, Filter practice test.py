# Q1. WAP to input name, marks and phone number of a student and format it using the function like below.
''' The name of the Student is ____, His marks are ___ and phone number is ___________'''

name = input("Enter your Name: ")
marks = int(input("Enter your Makrs: "))
number = int(input("Enter your Number: "))

# using format
print("The name of the Student is {}, His marks are {} and phone number is {}".format(name, marks, number))

# Using f string
print(f"The name of the Student is {name}, His marks are {marks} % and phone number is {number}")



# Q2. A list contains the multiplication table of 7. WAP to convert it to vertical string of same number.

table = [str(7 * i )for i in range(1, 11)]

s = "\n".join(table)
print(s)



# Q3. WAP to filter a list of numbers which are divisible by 5.

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

div_list = filter(lambda x: x % 5 ==0, l)

print(list(div_list))



# Q4. WAP to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

max_ele = reduce(lambda x, y : x if x >y else y, l)
print(max_ele)



# Q5. Flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()
    