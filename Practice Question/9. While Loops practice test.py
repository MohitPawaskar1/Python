# Q1. WAP to to print multiplication table of a given number using 'while' loop.

n = int(input("Enter a number to print a table: "))

i = 1

print(f"The table of {n}")

while (i <=10):
    print(f"{n} X {i} = {n * i}")
    i += 1






# Q2. WAP to find the sum of first n natual numbers using while loop.

n = int(input("Enter the number to get sum of all numbers : "))

i = 1

sum = 0

while(i<=n):
    sum += i 
    i += 1

print(f"The sum of the First {n} numbers is {sum}")





# Q3. WAP to calculate the factorial of a given number using for loop.

n = int(input("Enter the number to get factorial: "))

i = 1

fact = 1

while(i<=n):
    fact *= i
    i += 1

print(f"The Facotrial of {n} is {fact}")




# Q4. WAP to to print multiplication table of a given number using 'while' loop in reversed order.

n = int(input("Enter a number to print a table in reverse order: "))

i = 10

print(f"The table of {n}")

while (i >=1):
    print(f"{n} X {i} = {n * i}")
    i -= 1

