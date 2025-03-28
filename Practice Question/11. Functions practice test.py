# Q1. WAP using functions to find greatest of three numbers.

def greatest():
    
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    if(a>b and a>c):
        print(f"{a} is the Greatest number.")

    elif(b>a and b>c):
        print(f"{b} is the Greatest number.")

    else:
        print(f"{c} is the Greatest number.")

greatest()



# Q2. WAP using functions to convert Celcius to Fahrenheit.

def converter():

    celcius = int(input("Enter the Temperature in Celcius: "))

    fahrenheit = ((celcius * 9) / 5 ) + 32

    print(f"The {celcius}°C is {fahrenheit}°F.")

converter()



# Q3. How to prevent a ptython program to print a new line at the end.
'''
    print("Hello, World", end="") where end="" prevents from printing the new line

# '''
print("Hello,")
print("Mohit", end="")
print(" How are you?")



# Q4. Write a function to print first n lines of the following pattern.
'''
    ***
    **
    *

'''

def star_patter(n):

    for i in range(n, 0, -1):
        print("*" * i, end="")
        print(" " * (i -1), end="")
        print()

star_patter(5)
star_patter(3)



# Q5. Write a python function which converts inches to cms.

def size_convert(n):
    print(f"{n} inches = {n * 2.54} cm")

n = int(input("Enter inches: "))
size_convert(n)



# Q6. Write a function to remove a given word from a list and strip it at the same time.

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Mohit", "Raj", "Ojas", "Venky", "Adarsh", "Akash", "Ishwari", "Mihir", "Rohan"]
#l = ["Harry", "Rohan", "Shubham", "an"]

print(rem(l, "an"))



# Q7. Write a python function to print multiplication table of a given number.

def table(n):

    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

n = int(input("Enter a number: "))
table(n)


