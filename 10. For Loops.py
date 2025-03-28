'''
    for i in range(5): range function is used to generate numbers till n-1

    range takes the following arguments (start, stop, step) where stop is excluded

    for i in range(1, 11, 2): will print the numbers from 1 to 10 and 2 will be the difference
        print(i)

    1,3,5,7,9
    
    Break : Exit the loop at current iteration.

    Continue : Continue the loop just skip the current iteration.
    
    Pass : It's just a place-holder does nothing just pass the current iteration.
      
'''
# list
# l = [1,2,3,4,5,6]

# for i in l:
#     print(i)


# # tuple
# t = (1,2,3,4,5,6,7,8,9)

# for i in t:
#     print(i)


# # String
# s = "Mohit"

# for i in s:
#     print(i)



# using else after for loop
# l = [1,2,3,4]

# for i in l:
#     print(i)

# else:
#     print("Loop Over.")



# Break

for i in range(10):
    if (i == 5):
        break
    print(i)

print()

# Continue

for i in range(10):
    if (i == 5):
        continue
    print(i)


print()
# Pass 

for i in range(10):
    if (i == 5):
        pass
    print(i)





