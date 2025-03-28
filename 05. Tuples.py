'''
    Tuple is a collection of objects of same/different datatypes & is denoted by '()',

    unlike lists, tuples are immutable.

    my_tuple = (10, "Hello", 3.14, True, [1, 2, 3], {'key': 'value'})

'''
# Creating a tuple of mixed datatype
my_tuple = (10, "Hello", 3.14, True, [1, 2, 3], {'key': 'value'})
print(my_tuple)

# Using Count Function to count how many times the object is occured in the tuple
count = my_tuple.count(3.14)
print(count)


# Using Index Function to find index of the object in the tuple
idx = my_tuple.index(3.14)
print(idx)


# Length of Tuple
print(len(my_tuple))

# Using min, max, sum
numbers = (10, 50, 30, 90, 20)

print(min(numbers))
print(max(numbers))
print(sum(numbers))