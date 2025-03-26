# Q1. WAP to input eight numbers from the user & display all the unique number:s(once).

s = set()

n1 = int(input("Enter a number: "))
s.add(n1)
n2 = int(input("Enter a number: "))
s.add(n2)
n3 = int(input("Enter a number: "))
s.add(n3)
n4 = int(input("Enter a number: "))
s.add(n4)
n5 = int(input("Enter a number: "))
s.add(n5)
n6 = int(input("Enter a number: "))
s.add(n6)
n7 = int(input("Enter a number: "))
s.add(n7)
n8 = int(input("Enter a number: "))
s.add(n8)

print(s)



# Q2. Can we have a set with 18(int) and '18'(str) as a value in it?

s = {18, '18'}
print(s, type(s))



# Q3. What will be the length of the following set s:

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(f"The set {s}, has a length of {len(s)}")



# Q4. Can you change the value inside a list which contains in a set S?

'''
    No, you cannot change the value inside a list that 
    
    is contained in a set because lists are mutable 
    
    and sets only allow immutable (hashable) elements.

    s = {8, 7, 12, "Mohit", [1,2]}

'''


