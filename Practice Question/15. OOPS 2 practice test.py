# Q1. Create a class (2-D vector) and use it to create another class representing a (3-D vector).

class TwoDVector:
    def __init__(self, i , j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2d vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i , j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The 3d vector is {self.i}i + {self.j}j + {self.k}k")


v1 = TwoDVector(1, 2)
v2 = ThreeDVector(1,2,3)

v1.show()
v2.show()



# Q2. Create a class 'Pets' from 'Animal' and further create a class 'Dog' from 'Pets'.
# Add a method 'bark' to class 'Dog'

class Animal:
    pass

class Pets(Animal):
    pass

class Dogs(Pets):

    @staticmethod
    def bark():
        print("Bow Bow")

d = Dogs()
d.bark()



# Q3. Create a class 'Employee' and add salary and increment properties to it.

class Employee:
    increment = 20  # Class variable

    def __init__(self, salary):
        self.salary = salary

    @property
    def incremented_salary(self):
        return self.salary + self.salary * (self.increment / 100)  # Returns the incremented salary

    @incremented_salary.setter
    def incremented_salary(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100  # Recalculates the increment percentage

e = Employee(90000)
print(e.incremented_salary)  # Output: 108000.0 (90000 + 20% of 90000)

e.incremented_salary = 99000  # Setting new salary, updates increment percentage
print(e.increment)  # Output: 10.0 (since 99000 is 10% more than 90000)



# Q4. Write a class 'Complex' to represent complex numbers, along with overload
#     operators '+' and '*' which adds and multiply them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r , self.i + c2.i)
    
    def __mul__(self, c2):
        return Complex(self.r * c2.r , self.i * c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = Complex(1,2)
c2 = Complex(3,4)
print(f"The addition of 2 Complex numbers is {c1 + c2}")
print(f"The multiplication of 2 Complex numbers is {c1 * c2}")



# Q5. Write a class vector representing a vector of n dimensions. 
# Overload the + and * operator which calculates the sum and the dot(.) product of them.

class ThreeDVector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, v2):
        return ThreeDVector(self.i + v2.i, self.j + v2.j, self.k + v2.k)

    def __mul__(self, v2):  
        return ThreeDVector(self.i * v2.i, self.j * v2.j, self.k * v2.k)  # Fixed here

    def __str__(self):  
        return f"{self.i}i + {self.j}j + {self.k}k"

v1 = ThreeDVector(1, 2, 3)
v2 = ThreeDVector(3, 2, 1)

print(f"The addition of 2 3D Vectors is: {v1 + v2}")
print(f"The multiplication of 2 3D Vectors is: {v1 * v2}")



# Q6. Override the __len__() method on vector of Q5 to display the dimension of the vecotr.

class ThreeDVector:
    def __init__(self, l):
        self.l = l
    
    def __len__(self):
        return len(self.l)

v1 = ThreeDVector([1, 2, 3])
print(len(v1))