'''
    Anything written inside Single Quotes ''
    Anything written inside Double Quotes ""
    Anything written inside Triple Quotes ''' '''
    
    In Slicing [start, stop, step] where stop is excluding

'''

# Slicing of String
name = "Mohit"

sliced_name = name[-5:-2] # Moh

print(sliced_name)



# Slicing with skip value
word = "amazing"

print(word[1::2]) 



# length function
print(len(name)) # Return's the length of the String



# Other Functions
print(name.endswith("it")) # Returns True if ends with matches

print(name.startswith("M")) # Returns True if starts with matches

print(word.capitalize()) # Returns the First word in Capital



# Escape Sequence Characters
'''
    '\n' is used for the new line

    '\t' is used for the tab space i.e. 4 spaces

    '\"\"' is used for using Double Quotes in a string
 
'''