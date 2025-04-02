# Q1. WAP to open three files 1.txt, 2.txt and 3.txt if any of these files are not present,
#     a message without exiting the program must be printed prompting the same.

try:
    with open("1.txt") as f1:
        print(f1.read())
except Exception as e:
    print(e)

try:
    with open("2.txt") as f1:
        print(f1.read())
except Exception as e:
    print(e)

try:
    with open("3.txt") as f1:
        print(f1.read())
except Exception as e:
    print(e)

print("Thanks")



# Q2. WAP to print 3rd, 5th & 7th element from a list using enumerate function.

l = [1,2,3,4,5,6,7,8,9]

for index, item in enumerate(l):
    if (index == 2 or index == 4 or index == 6):
        print(item)



# Q3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input("Enter a number: "))

table = [n * i for i in range(1, 11)]
print(table)



# Q4. WAP to display a/b where a and b are integers. If b = 0, display infinite by handling the 'ZeroDivisionError'

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a/b)

except ZeroDivisionError as z:
    print("Infinite")



# Q5. Stoe the multiplication table generated in Q3 in a file named Tables.txt.

n = int(input("Enter a number: "))

table = [n * i for i in range(1, 11)]
print(table)
with open('16.1 Tables.txt', 'w') as f:
    f.write(str(table) + "\n")
