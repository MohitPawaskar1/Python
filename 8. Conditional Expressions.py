'''
    IF-ELIF-ELSE are the Conditional Expressions,

    If 'if' is satisfied it will execute and 'elif' or 'else' will not be executed,

    otherwise it will check for all the conditions which ever gets satisfied it gets executed,

    if NONE condition satisfied then the 'ELSE' get's executed.

'''
# IF ELIF ELSE Ladder
age = int(input("Enter your age: "))
if(age%2 == 0):
    print("EVEN")

if(age>=18):
    print("You Can VOTE!!")

elif(age<=0):
    print("Enter a valid age...")

else:
    print("You can't VOTE!!")