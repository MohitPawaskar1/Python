# Q1. WAP to add two numbers

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

Sum = num1 + num2

print(f"The Sum of {num1} + {num2} is {Sum}")



# Q2. WAP to find remaim=nder when a number is divided by z

num3 = int(input("Enter 3rd Number: "))
num4 = int(input("Enter 4th Number: "))

Remainder = num3 % num4

print(f"The Remainder of {num3} / {num4} is {Remainder}")



# Q3. Check the type of variable assigned using input () function.

check_type = input("Enter to check type: ")
print(f"The {check_type} you entered is of {type(check_type)}")



# Q4. Use comparison operator to find out whether a given variable 'a' is greater than 'b' or not. Take a = 34 & b = 40.

a = 34

b = 80

print(f"{a} is greater than {b} is, {a > b} ")



# Q5. WAP to find an average of two numbers entered by the user.
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

avg = (num1 + num2) / 2

print(f"The average of {num1} & {num2} is {avg}")



# Q6. WAP to calculate the square of a number entered by the user.

num = int(input("Enter number: "))

square = num **2

print(f"The square of {num} is {square}")
