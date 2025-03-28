# Q1. WAP to to print multiplication table of a given number using 'for' loop.

n = int(input("Enter the number to get the table: "))

print(f"The table of {n}")

for i in range(1,11):
    print(f"{n} X {i} = {n * i}")

print()

# Q2. WAP to greet all the person names stored in a list 'l' and which starts with S.

l = ["Mohit", "Soham", "Sachin", "Shantanu", "Gaurav"]

for i in l:
    if i[0] == 'S':
        print(f"Hello {i}, Good Morning.")

'''
    For better optimization we can also used builtin function 'startswith'

'''

for i in l:
    if(i.startswith('M')):
        print("Hello", i,  "How are You?")



# Q3. WAP to find whether a given number is prime or not.

num = int(input("Enter a number to see is it prime: "))

if num < 2:
    print(f"{num} is Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is Not a Prime Number")
            break
    else:
        print(f"{num} is a Prime Number")



# Q4. WAP to calculate the factorial of a given number using for loop.

n = int(input("Enter the number to get the Factorial: "))

i = 1

fact = 1

for i in range(1, n+1):
    fact *= i

print(f"The Factorial of {n} is {fact}")



# Q5. WAP to print the following star pattern:
'''
    For n = 3

      *  
     ***
    ***** 

'''

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print(" " * (n - i), end="")
    print("*" * (2*i-1), end="")
    print()



# Q6. WAP to print the following star pattern:
'''
    For n = 3

    *  
    **
    ***

'''

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print("" * (n - i), end="")
    print("*" * (i), end="")
    print()



# Q7. WAP to print the following star pattern:
'''
    For n = 3

    * * *

    *   *

    * * *

'''

n = int(input("Enter the number: "))

for i in range(1, n+1):
    if (i==1 or i == n):
        print("*" * (n), end="")
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print()



# Q8. WAP to print multiplication table of n using for loop in reversed order.

n = int(input("Enter the number to print the table in reverse order: "))

for i in range(10, 0, -1):
    print(f"{n} X {i} = {n * i}")