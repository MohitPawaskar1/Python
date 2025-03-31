'''
    Inheritance in Python 👨‍👩‍👦
    
    Inheritance allows a child class to inherit properties and methods from a parent class. 
    
    It helps in code reusability and organization.

                                [Base Class]  
                                │  
                   ┌────────────┴─────────────┐  
                   │                          │  
                   [Child Class 1]          [Child Class 2]   ← Hierarchical Inheritance  
                   │  
                   [Grandchild Class]  ← Multilevel Inheritance  

                             [Parent Class 1]      [Parent Class 2]  
                                    │                   │  
                                    └───────────[Child Class]  ← Multiple Inheritance  

                                [Hybrid Inheritance]  
                        (Combination of above types)  

'''
# Single Inheritance

class Employee:
    company = "Apple"
    name = "Mohit"

    def show(self):
        print(f"The name of the Employee is {self.name} and his comapny is.{self.company}")

class Programmer(Employee):
    company = "Apple Inc."

    def show_Language(self):
            print(f"The company name is {self.company} and He is good with {self.language} language.")

a = Employee()
b = Programmer()

print(a.company, b.company)



# Multi-Level Inheritance

class Employee:
    company = "Apple"
    name = "Mohit"
    salary = 2000000
    def show(self):
        print(f"The name of the Employee is {self.name} and his salary is Rs.{self.salary}")

class Coder:
     language = "Python"

     def print_languages(self):
          print(f"Out of all the languages here is your language {self.language}")


class Programmer(Employee, Coder):
    company = "Apple Inc."

    def show_Language(self):
            print(f"The name is {self.company} and He is good with {self.language} language.")

a = Employee()
b = Programmer()

b.show()
b.print_languages()
b.show_Language()



# Super 

class Employee:
     def __init__(self):
          print("Constructor of Employee")
     a = 1
  
class Programmer(Employee):
     def __init__(self):
          print("Constructor of Programmer")
     b = 2

class Manager(Programmer):
     def __init__(self):
          super().__init__()
          print("Constructor of Manager")
     c = 3

o = Manager()
print(o.a)
  


# @classmethod
'''
    A classmethod is used where you want to keep the attribute of class unchanged.

    Use cls instead of self.

'''
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45
e.show()



# Property Decoraters
'''
    ✅ Encapsulation:

        Hides data inside a class and only allows access through methods.

        Protects the data from direct modification.

        Achieved using private (__variable) and protected (_variable) attributes.

        
    ✅ Abstraction:

        Hides implementation details and only shows necessary features.

        Used to create a blueprint (abstract class) that other classes must follow.

        Achieved using abstract classes (ABC module in Python).    
               
 '''

class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Mohit Pawaskar"
print(e.fname, e.lname)



# Operator Overloading (Polymorphism)
'''
    print(n + m)

    Traceback (most recent call last):
  File  OOPS 2.py", line 174, in <module>
    print(n + m)""
          ~~^~~
TypeError: unsupported operand type(s) for +: 'Number' and 'Number'

'''

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)
print(n + m)
