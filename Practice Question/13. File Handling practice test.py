# Q1. WAP to read the text from a given file 'poem.txt' and find out whether it contains the word 'twinkle',

# with open(r"D:\Python\Practice Question\13.1 poem.txt") as f:
#     #print(f.read())
#     word = f.read().lower()
#     if ("twinkle" in word):
#         print("Yes Twinkle is present in the poem")

#     else:
#         print("No Twinkle is not present in the poem")



# Q2. The game() function in a program lets a user play a gameand returns the score as an integer. You need to read a file 'Hi-Scire.text' 
# which is either blank or contains the previous Hi-Score. You need to WAP to update the High-Score 
# whenever the game() function breaks the Hi-Score.

# import random

# def game():
#     print("Game Started....")
    
#     score = random.randint(1, 100)  # Simulate a random game score

#     file_path = r"D:\Python\Practice Question\13.2 Hi-Score.txt"  

#     try:
#         with open(file_path, "r") as f:
#             Hi_score = f.read().strip()  # Read and remove any whitespace
#             Hi_score = int(Hi_score) if Hi_score.isdigit() else 0  # Convert to int, default to 0 if empty
#     except FileNotFoundError:
#         Hi_score = 0  # If file doesn't exist, assume high score is 0

#     print(f"\nYou Scored: {score}")
    
#     if score > Hi_score:
#         print(f"🎉 New High Score! Updating file...")
#         with open(file_path, "w") as f:
#             f.write(str(score))  # Write the new high score
#     else:
#         print(f"Your Score: {score}. High Score remains: {Hi_score}.")

#     return score

# game()



# Q3. WAP to generate multiplication table from 2 to 20 & Write it to the different files.
# Place these files in an folder for a 13-year old.

# import os

# def table_generator():
#     folder_path = "Q3. 13-Year Old"  # Directory where files will be saved
#     os.makedirs(folder_path, exist_ok=True)  # ✅ Create folder if it doesn't exist

#     for i in range(2, 21):  # Generate tables from 2 to 20
#         file_path = os.path.join(folder_path, f"table_{i}.txt")  # Create file path

#         with open(file_path, "w", encoding="utf-8") as f:  # ✅ Use UTF-8 to avoid encoding issues
#             f.write(f"\n📌 Multiplication Table of {i}\n")
#             f.write("-" * 25 + "\n")
#             for j in range(1, 11):
#                 f.write(f"{i} X {j} = {i * j}\n")
#             f.write("\n")  # New line at the end for readability

#         print(f"✅ Table {i} saved in: {file_path}")

# # Call the function to generate all multiplication tables
# table_generator()



# Q4. A file contains a word "Donkey" multiple times. You need to WAP to replace this word with "Monkey" by updating the same file.

# word_to_replace = "donkey"
# replacement_word = "monkey"

# # Read the file content
# with open(r"D:\Python\Practice Question\13.4,5 Donkey Story.txt", "r", encoding="utf-8") as f:
#     content = f.read()

# # Replace all occurrences of "donkey" (case-insensitive)
# new_content = content.replace(word_to_replace, replacement_word)  # lowercase "donkey"
# new_content = new_content.replace(word_to_replace.capitalize(), replacement_word.capitalize())  # "Donkey"

# # Write the modified content back to the file
# with open(r"D:\Python\Practice Question\13.4 Donkey Story.txt", "w", encoding="utf-8") as f:
#     f.write(new_content)

# print("✅ All occurrences of 'donkey' have been replaced with 'monkey'.")



# Q5. Repeat program 4 for a list of such word to be censored

# words = ["Monkey", "foolish"]

# with open(r"D:\Python\Practice Question\13.4,5 Donkey Story.txt", "r", encoding="utf-8") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "Monkey")

# with open(r"D:\Python\Practice Question\13.4,5 Donkey Story.txt", "w", encoding="utf-8") as f:
#     f.write(content)



# Q6. WAP to mine a log file & find out whether it contains a word "python".

# with open(r"D:\Python\Practice Question\13.6,7 log.txt") as f:
#     content = f.read()

# if ("python" in content):
#     print("Yes the word in present.")

# else:
#     print("Not present")



# Q7. WAP to find out the line number where oython is present.

# line = 1

# with open(r"D:\Python\Practice Question\13.6,7 log.txt") as f:
#     lines = f.readlines()

# lineno = 1
# for line in lines:
#     if ("python" in line):
#         print("Yes the word in present at line no: ", lineno)
#         break
#     lineno += 1


# else:
#         print("Not present")



# Q8. WAP to make a copy of a text file "this.txt"

# with open(r"D:\Python\Practice Question\13.8,9 this.txt", "r") as f:
#     content = f.read()
    
# with open(r"D:\Python\Practice Question\13.8,9 this_copy.txt", "w") as f:
#     f.write(content)



# Q9. WAP to find out whether a file is identical & matches the content of another file.

# with open(r"D:\Python\Practice Question\13.8,9 this.txt", "r") as f:
#     content = f.read()
    
# with open(r"D:\Python\Practice Question\13.8,9 this_copy.txt", "r") as f:
#     content1 = f.read()

# if (content == content1):
#     print("Yes both files are identical")

# else:
#     print("No both files are not identical")



#  Q10. WAP to wipe out the content of a file using python.

# with open(r"D:\Python\Practice Question\13.10 wipe.txt", "r") as f:
#     content = f.read()
    
# with open(r"D:\Python\Practice Question\13.10 wipe.txt", "w") as f:
#     f.write("")



# Q11. WAP to rename a file to "13.10,11 wipe.txt"

import os

# Specify the current file name and the new name
old_name = r"D:\Python\Practice Question\13.10 wipe.txt"  # 🔹 Change this to your actual file name
new_name = r"D:\Python\Practice Question\13.10,11 wipe.txt" 

try:
    os.rename(old_name, new_name)  # Rename the file
    print(f"✅ File renamed successfully to: {new_name}")
except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: Permission denied. Close the file if it's open.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
