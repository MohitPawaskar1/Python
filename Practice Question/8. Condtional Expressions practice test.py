# Q1. WAP to find the greatest of four numbers eneted by the user.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))


if (num1>num2 and num1>num3 and num1>num4):
    print(f"In all 4 numbers num1: {num1} is the greatest number.")

elif (num2>num1 and num2>num3 and num2>num4):
    print(f"In all 4 numbers num2: {num2} is the greatest number.")

elif (num3>num2 and num3>num1 and num3>num4):
    print(f"In all 4 numbers num3: {num3} is the greatest number.")

else: 
    print(f"In all 4 numbers nume4: {num4} is the greatest number.")



# Q2. Write a program to finde out whether a student has passed or failed if it requires a total of 
#     40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

phy = int(input("Enter the marks of Physics: "))
chem = int(input("Enter the marks of Chemistry: "))
math = int(input("Enter the marks of Maths: "))

total_perecent = ((phy + chem + math) / 300) * 100

if (total_perecent > 40 and phy > 33 and chem > 33 and math > 33):
    print(f"The Student has been passed in all subjects with {total_perecent:.1f}%")

else: 
    print(f"The Student has been FAILED with {total_perecent:.1f}%")



# Q3. A spam comment is defined as a text containing following keywords:
#     "Make a lot of money", "buy now", "subscribe this", "click this". WAP to detect these spams.
'''
    This program is good but only problem is user has to enter only 
    
    specific words as input but cant find if whole message is given

    '''
word = input("Enter the sentence to verify: ")

if(word == "Make a lot of money" or word == "buy now" or word == "subscribe this" or word == "click this"):
    print("WARNING: THIS IS A SPAM MAIL")

else:
    print("This is not a spam")


# Using 'in' function
'''
    By using in function we can actually check for words in the message

'''
m1 = "Make a lot of money" 
m2 = "buy now"
m3 = "subscribe this"
m4 = "click this"

message = input("Enter a message: ")

if((m1 in message) or (m2 in message) or (m3 in message) or (m4 in message)):
    print("WARNING: THIS IS A SPAM MAIL")

else:
    print("This is not a spam")



# Q4. WAP to find whether a given username cantains less than 10 characters or not.

username = input("Enter Username: ")

if(len(username) < 10):
    print(f"The Username {username} contains less than 10 characters.")

else:
    print(f"The Username {username} contains more than 10 characters.")



# Q5. WAP which finds out whether a given name is present in a list or not.

lst = ['Adarsh', 'Akash', 'Mihir', 'Ishwari', 'Mohit', 'Ojas', 'Raj', 'Venky']

name = input("Enter the name: ")

if(name in lst):
    print(f"The name {name} is in the above list.")

else:
    print(f"The name {name} is not in the above list.")



# Q6. WAP to calculate the grade of a student from his marks from the following scheme:
'''
    90 - 100 => Ex
    80 - 90  => A
    70 - 80  => B
    60 - 70  => C
    50 - 60  => D
    <50      => F
'''
perecentage = int(input("Enter your percentage: "))

if(90<=perecentage<=100):
    print(f"The Student has scored {perecentage} passed with Ex grade")

elif(80<=perecentage<=90):
    print(f"The Student has scored {perecentage} passed with A grade")

elif(70<=perecentage<=80):
    print(f"The Student has scored {perecentage} passed with B grade")

elif(60<=perecentage<=70):
    print(f"The Student has scored {perecentage} passed with C grade")

elif(50<=perecentage<=60):
    print(f"The Student has scored {perecentage} passed with D grade")

else:
    print(f"The Student has scored {perecentage} passed with F grade")



# Q7. WAP to find out whether a givenpost is talking about "Mohit" or not.

p1 = "Mohit"

p2 = "mohit"

post = input("Enter the post: ")

if(p1 in post or p2 in post):
    print(f"YES...   The Post is talking about {p1}")

else:
    print(f"NO...   The Post is not talking about {p1}")


'''
    We can also use "Mohit directly in if statement no need to assign it to some variable,

    just convert all of them to lower().
'''


post = input("Enter the post: ")

if("Mohit".lower() in post.lower()):
    print(f"YES...   The Post is talking about Mohit")

else:
    print(f"NO...   The Post is not talking about Mohit")
