'''
    list is a collection of objects of any/ different datatypes & is denoted by '[]',

    unlike strings lists are mutable.

    list = ["Apple", 40, 3.14, True]


'''

# List of Cars & accessing the value using index number
cars = ["BMW", "Mercedes", "Audi", "Jaguar", "Volvo"]
print(cars[0])


# Updating the value of list using index 
cars[4] = "VW" 
print(cars)


# Appending the list is also possible using '.append' function
cars.append("RR") 
print(cars)



# Using Sort Function for sorting the list in ascending or descending order
l1 = [9,5,7,8,6,4,3,2,1,6]
l1.sort()
print(l1)


# Using Reverse Function for reversing the list
l1.reverse()
print(l1)


# Using Insert Function for inserting the object in the middle of the list by (index at which want to add object, object)
cars.insert(3, "Range Rover")
print(cars)


# Using POP Function for deleting the object.
print(l1.pop(3))
print(l1)


# Using Remove Method it takes the object inside (), not the index value
print(l1.remove(9))
print(l1)