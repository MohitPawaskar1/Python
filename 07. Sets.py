'''
    Sets is collection of well defined unique objects,

    Sets are represented by '{}', to create a empty set

    empty_set = set() & it don't contains any duplicate values,

    can't access by indexing

    You can also store different types of datatypes in Set.


'''

# Creating a Set
s = {1,2,3}
print(s, type(s))
print(len(s))


# Add Function
s.add(4)
print(s)

# Remove Function
s.remove(1)
print(s)

# Discard Function
s.discard(5) # Don't through Error if element is not present
print(s)

#  POP Function
removed_element = s.pop() # Pop's random element
print(removed_element)

# Union Function
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2) # All elements of both the sets but common elements are only once
print(result) # {1,2,3,4,5}


# Intersection Function
result = set1.intersection(set2) # Gets all the common elements of both the sets
print(result) # {3}


# Difference Function
result = set1.difference(set2) # Gives the elements of 1st Set but common and 2nd set elements are not there
print(result) # {1,2}


# Symmetric Difference
result = set1.symmetric_difference(set2) # Gives all uncommon elements from both the sets
print(result) # {1,2,,4,5}


# issubset Function
small_set = {1, 2} 
result = small_set.issubset(set1) # Check wether a is subset of b
print(result) # True


# issuperset Function
print(set1.issuperset(small_set)) # Check wether a is superset of b # True



# isdisjoint Function
set3 = {6,7}
print(set1.isdisjoint(set3)) # Returns True if there is no common element in both sets # True




