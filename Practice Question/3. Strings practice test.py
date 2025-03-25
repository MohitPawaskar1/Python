# WAP to display a user entered name followed by Good Afternoon using Input() function.

name = input("Enter the Name: ")
print(f"Hello {name}, Good Afternoon..!")



# WAP to fill in a letter template given below with name and date.

date = (input("Enter a date: "))

letter = (f'''Dear {name},
            You are selected!
            {date}
            ''')
print(letter)

# Using Replace function

letter = '''Dear <|Namee|>,
            You are selected
            <|Date|>'''

print(letter.replace("<|Namee|>", "Mohit"). replace("<|Date|>", "20th May")) # Chaining of Replace function



# Q3. WAP to detect double space in a string.

name = "Mohit is a bad boy  and"

print(name.find("  ")) # Returns the index number at which element is presented. If returned -1 it means element is not present



# Q4. Replace the double space in a string

print(name.replace("  ", " "))




# Q5. WAP to format the following letter using escape sequence characters.

Letter = "Dear Mohit, this python course is  nice. Thanks!"

new_letter = "Dear Mohit, \n\tThis python course is  nice. \nThanks!"

print(new_letter)