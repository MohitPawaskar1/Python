'''
        +---------------------+         +------------------------+
        |      Program        |         |       File             |
        +---------------------+         +------------------------+
        |   Open File         |  ---->  |   Opened for R/W       |
        |   Read/Write Data   |  <----  |   Data is Read/Written |
        |   Close File        |  ---->  |   File is Closed       |
        +---------------------+         +------------------------+


    open takes 2 parameter (file name, mode)

    mode - 1.'r' : opens a file in read mode

           2.'w' : opens a file in write mode

           3.'a' : opens a file in appending mode
        
           4.'rb' : opens a file in read in binary mode
           
           5.'rt' : opens a file in read in text mode

           6.'+' : opens a file for updating



'''
# Opening and Reading a file using .open

# f = open("13.1 file.txt")

# data = f.read()
# print(data)
# f.close



# Writing a file using 'r'

# st = "Mohit owns a BMW M5 F90 at the age of 23."

# f = open("13.2 write_file.txt", "w")

# f.write(st)

# f.close()



# Readline function.

f = open("13.1 file.txt")

# lines = f.readlines()

# print(lines)

# print(type(lines))


# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))




# f.close()



# Reading lines using while loop

# line =f.readline()

# while(line != ""):
#     print(line)
#     line = f.readline()



# Appending a file

# st = "\nMohit owns a BMW M5 F90 at the age of 23."

# f = open("13.1 file.txt", "a")

# f.write(st)

# f.close()



# Opening a file using 'with'

with open("13.1 file.txt") as f:
    print(f.read())

