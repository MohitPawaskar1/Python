'''
                             +----------------------+
                             |      Class           |
                             |----------------------|
                             | - Attributes         |
                             | - Methods            |
                             +----------------------+
                                        ▲
                       ----------------------------------------
                        │                 │                  │
                 +------------+    +------------+    +------------+
                 |  Object 1  |    |  Object 2  |    |  Object 3  |
                 +------------+    +------------+    +------------+

                   ----------------------------------------------
                    │                 │                         │
                +------------+   +------------+                +----------------+
                |  Parent    |   |  Child 1   |  ◄──────       |  Child 2       |
                |  (Base)    |   | (Derived)  |  Inheritance   | (Derived)      |
                +------------+   +------------+                +----------------+
                 │                      ▲
                 │                      │
                 └─────────────►  Method Overriding (Polymorphism)

                +----------------------------------------------------------+
                |                 Encapsulation                            |
                |  Private attributes & methods are hidden from outside    |
                +----------------------------------------------------------+

'''



# Creating basic class

# class Employee:
#     role = "AI/ML Engineer"
#     salary = 2000000


# mohit = Employee()
# print(mohit.salary, mohit.role)

# mohan = Employee
# print(mohan.role, mohan.salary) 



# StaticMethod

'''
    @staticmethod is used where you don't need the atrributes from the class like 'self'.
'''
class Student:
    language = "Python"
    year = 4

    def getinfo(self):
        print(f"The Student is in {self.year}th year & studies {self.language}")

    @staticmethod
    def greet():
        print("Good Morning")


mohit = Student()
mohit.getinfo()
mohit.greet()