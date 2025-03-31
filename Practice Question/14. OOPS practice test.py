# Q1. Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:

    company = "Microsoft"

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def get_info(self):
        print(f"{self.name} is a {self.role} at {self.company} & His Salary is {self.salary}")

e1 = Programmer("Mohit", "AI/ML Engineer", 2000000)
e1.get_info()



# Q2. Write a class "Calculator" capable of findings square, cube and square root of a number.

import math

class Calculator:

    def __init__(self, n):
        self.number = n

    def square(self):
        print(f"The Square of {self.number} is {self.number ** 2}")

    def cube(self):
        print(f"The Cube of {self.number} is {self.number ** 3}")

    def square_root(self):
        print(f"The Square root of {self.number} is {math.sqrt(self.number)}")

n = int(input("Enter a number: "))

n1 = Calculator(n)
n1.square()
n1.cube()
n1.square_root()

    

# Q3. Create a class with a class attribute a; create an object from it and set 'a' directly using object a = o. 
# Does this change the class attribute?

class Demo:

    a = 4

o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not present.

o.a = 0    # Instance attribute is set.

print(o.a) # Prints instance attributes because instance attribute is present.

print(Demo.a) # Prints the class attributes.

print("No Class Attributes remains unchanged")



# Q4. Add a static method in problem 2, to greet the user with hello.

import math

class Calculator:

    def __init__(self, n):
        self.number = n

    @staticmethod
    def greet():
        print("Hello")

    def square(self):
        print(f"The Square of {self.number} is {self.number ** 2}")

    def cube(self):
        print(f"The Cube of {self.number} is {self.number ** 3}")

    def square_root(self):
        print(f"The Square root of {self.number} is {math.sqrt(self.number)}")

Calculator.greet()

n = int(input("Enter a number: "))

n1 = Calculator(n)
n1.square()
n1.cube()
n1.square_root()



# Q5. Write a class Train which has methods to book a ticket, get status  (no of seats) & get fare
#     information of train running under Indian Railways.

from random import randint

class Train:

    def __init__(self, pickup, destination):
        self.pickup = pickup
        self.destination = destination
        self.train_no = randint(10000, 20000)  

    def booking(self):
        print(f"✅ Ticket Booked! Train No: {self.train_no}, From {self.pickup} → {self.destination}")

    def status(self):
        queue_no = randint(1, 100)
        print(f"⏳ Status: Train No: {self.train_no}, From {self.pickup} → {self.destination} is in waiting list. {queue_no} people ahead.")

    def fare(self):
        fare = randint(500, 2000)
        print(f"💰 Fare: Train No: {self.train_no}, From {self.pickup} → {self.destination} costs Rs.{fare}")


p1 = Train("Pune", "Mumbai")


p1.booking()
p1.status()
p1.fare()



# Q6. Can you change self-parameter inside a class to something else (say "mohit"). Try changing ti "slf" or "mohit" &  see the effects.
'''
from random import randint

class Train:

    def __init__(mohit, pickup, destination):
        mohit.pickup = pickup
        mohit.destination = destination
        mohit.train_no = randint(10000, 20000)  

    def booking(mohit):
        print(f"✅ Ticket Booked! Train No: {mohit.train_no}, From {mohit.pickup} → {mohit.destination}")

    def status(mohit):
        queue_no = randint(1, 100)
        print(f"⏳ Status: Train No: {mohit.train_no}, From {mohit.pickup} → {mohit.destination} is in waiting list. {queue_no} people ahead.")

    def fare(mohit):
        fare = randint(500, 2000)
        print(f"💰 Fare: Train No: {mohit.train_no}, From {mohit.pickup} → {mohit.destination} costs Rs.{fare}")


p1 = Train("Pune", "Mumbai")


p1.booking()
p1.status()
p1.fare()

'''
print("And The Answer is no changing the Name of self paramaeter doesn't affect the code unless and until the same name is used through-out the code")