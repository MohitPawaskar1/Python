# Virtual Enviornment
""""
    pip install pandas==1.5

    pip install numpy
    
    pip install seaborn

    if version is not mentioned automatically the newest version available gets downloaded.

    But if older or specified version is downloaded the latest version gets deleted 
    
    so if you want both the version you have to setup the virtual environment.

    To setup the the virtual environment here are the steps:

    1 - Install the package

    - pip install virtualenv

    2 - set the name of your environment 

    - virtualenv (name)

    3 - open the env folder in powershell/cmd and type

    


"""


# Lambda Function
" lambda argument : expression "
square = lambda x: x *x
print(square(10))



# Join Method

a = ["Mohit", "Raj", "Akash"]

final = "::".join(a)
print(final)



# Format

a = "{0} is a good {1}". format("Mohit", "boy")
print(a)


# Map Function

l = [1,2,3,4,5]
newl = map(lambda x : x ** 2, l)
print(list(newl))


# Filter Function
fil_l = filter(lambda x :  x > 2, l)
print(list(fil_l))


# Reduce Function
from functools import reduce

red_l = reduce(lambda x, y : x + y , l)
print(red_l)