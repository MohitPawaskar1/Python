# Define a Circle class to create a circle woth radius r using the constructor.
# Define an Area() method of the class which calculates the area of the Circle.
# Define a Perimeter() mothod of the class which allows you to calculate the perimeter of the circle.

# class Cirlce:
#     def __init__(self, r):
#         self.r = r

    
#     def Area(self):
#         print(f"Area of the Circle is {(22/7) * self.r * self.r }")

#     def Perimeter(self):
#         print(f"Perimeter of the Circle {2 * (22/7) * self.r: .2f}")

# c1 = Cirlce(21)
# c1.Area()
# c1.Perimeter()

# Define a Employee class with attributes role, department & Salary. This class also has a showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"The Employee working as {self.role} in {self.department} has salary of Rs.{self.salary} per month")



class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("SDE", "AI/ML", 200000)
       
    def show(self):
        print(f"The Employee {self.name}, working as {self.role} in {self.department} Department has salary of Rs.{self.salary} per mont at the age of {self.age}")

e2 = Engineer("Mohit", 22)
e2.show()



# Create a class called Order which stores item & its price.
# Use Dunder function __gt__() to convey that:
#        order1 > order2 if price of order1 > price of order2.

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price


order1 = Order("Chips", 20)
order2 = Order("Tea", 15)

print(order1 > order2)