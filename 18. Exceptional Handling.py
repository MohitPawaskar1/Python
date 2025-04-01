try: 
    n = int(input("Enter a number: "))
    print(f"You entered {n}")

except Exception as e:
    print(e)
finally:
        n = int(input("Enter a number: "))
        print(f"You entered {n}")

print("Done")


# Zerodivisionerror

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if (b ==0):
     raise ZeroDivisionError(f"Hey the number {a} is not divisible by 0")
else:
     print(f"The Division is {a/b}")

print("Done")



# try-else 
'''
    else part will only run when the try part is properly executed.
'''
try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else: 
    print("I am inside else")



# try-finally
'''
    finally part will run when the try or except part is properly executed normally,
    
    but if there is function in which try is there finally must be present there.

'''
def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return
    
    finally: 
        print("I am inside finally")

main()



#global

a = 90

def fun():
    global a
    a = 3
    print(a)

fun()
print(a)



# Enumerate

l = [1,5,9,7,8,6,4,2,3]

index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1

# Using Enumerate function

for index, item in enumerate(l):
     print(f"The item number at index {index} is {item}")



# List Comprehensions

l = [9,5,7,8,2,1,4,6,3]

newl = [x**2 for x in l ]

print(newl)