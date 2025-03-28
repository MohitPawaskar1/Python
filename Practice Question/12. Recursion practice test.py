
# Q1. Write a recursive function to calculate the sum of the first natural numbers.

def natural_sum(n):

    if (n == 1):
        return 1
    return n + natural_sum(n-1)

n = int(input("Enter a number: "))
print(f"The sum of first {n} natural numbers is: {natural_sum(n)}")



# Q2. Write a function to print first n lines of the following pattern.
'''
    ***
    **
    *

'''

def star_patter(n):
    if (n == 0):
        return 
    print("*" * n)
    star_patter(n-1)

star_patter(3)



# Q3. Write a python function to print multiplication table of a given number.
def table_recursive(n, i=1):
    if i > 10:  # Base case: Stop when i exceeds 10
        return
    print(f"{n} X {i} = {n * i}")
    table_recursive(n, i + 1)  # Recursive call with incremented i

n = int(input("Enter a number: "))
table_recursive(n)
