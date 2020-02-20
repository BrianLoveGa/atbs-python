#! /usr/bin/env python3

print("hello there")


# Running Python Programs on macOS
# On macOS, you can create a shell script to run your Python scripts by creating a text file with the .command file extension. 
# Create a new file in a text editor such as TextEdit and add the following content:

#     #!/usr/bin/env bash
# python3 / path/to/your/pythonScript.py

# Save this file with the .command file extension in your home folder(for example, on my computer it’s / Users/al). 
# In a terminal window, make this shell script executable by running chmod u+x yourScript.command. 
# Now you will be able to click the Spotlight icon(or press image-SPACE) and enter yourScript.command to run the shell script, 
# which in turn will run your Python script.


# An absolute path, which always begins with the root folder
# A relative path, which is relative to the program’s current working directory


# Let’s put these concepts together. Enter the following into the interactive shell:

# >> > baconFile = open('bacon.txt', 'w')
# >> > baconFile.write('Hello, world!\n')
# 13
# >> > baconFile.close()
# >> > baconFile = open('bacon.txt', 'a')
# >> > baconFile.write('Bacon is not a vegetable.')
# 25
# >> > baconFile.close()
# >> > baconFile = open('bacon.txt')
# >> > content = baconFile.read()
# >> > baconFile.close()
# >> > print(content)
# Hello, world!
# Bacon is not a vegetable.


# Project: Generating Random Quiz Files
# Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately, you know some Python.

# Here is what the program does:

# Creates 35 different quizzes
# Creates 50 multiple-choice questions for each quiz, in random order
# Provides the correct answer and three random wrong answers for each question, in random order
# Writes the quizzes to 35 text files
# Writes the answer keys to 35 text files
# This means the code will need to do the following:

# Store the states and their capitals in a dictionary
# Call open(), write(), and close() for the quiz and answer key text files
# Use random.shuffle() to randomize the order of the questions and multiple-choice options
