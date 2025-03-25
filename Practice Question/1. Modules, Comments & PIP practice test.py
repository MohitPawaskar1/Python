# Q1. WAP to print a Story in Python.

print('''The Lion and the Mouse:
      
Initial Encounter:
                A lion, the king of the jungle, is sleeping when a little mouse, startled by his presence, runs across his nose.

      
The Lion's Anger:
                The lion wakes up, angered by the disturbance, and grabs the mouse, intending to kill it.

The Mouse's Plea:
                The mouse, fearing for its life, begs the lion to spare him and promises to repay him in the future.

The Lion's Reluctant Mercy:
                The lion, amused by the mouse's promise, decides to let the mouse go, thinking a mouse could never help him.

A Change of Fortune:
                Later, the lion gets caught in a hunter's net and roars for help, unable to free himself.

The Mouse's Reciprocity:
                The mouse, hearing the lion's cries, rushes to his aid and chews through the ropes of the net, freeing the lion.

The Lion's Gratification:
                The lion, humbled by the mouse's help, thanks the mouse and realizes that even the smallest creature can be helpful.

The Moral:
                The story teaches that kindness is never wasted and that even the most unlikely person can be helpful. ''')


# Q2. Use REPL & print the table of 5 using it.

n= 5

i = 1
while i<=10:
    print(f"{n} * {i} = {n * i}")
    i += 1


# Install an external module & use it to perform an operation of your interset.

import pyttsx3
engine = pyttsx3.init()
engine.say("Mohit is the Richest man of the Fucking World & He will buy is first BMW before Monsoon 2026!")
engine.runAndWait()


# WAP to print the contents of a directory using the os module.

import os # importing the OS module


# Selecting the Directory i.e the current directory
current_directory = os.getcwd()
print(f"Contents of directory: {current_directory}") # print the directory

for item in os.listdir(current_directory): # using for loop for iteration
    print(item)
