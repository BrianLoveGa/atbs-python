# Practice Questions
# 1. Which of the following are operators, and which are values?

# *
# 'hello'
# -88.8
# -
# /
# +
# 5

#####
# answer operator = * , - , / , +
#        values = -88.8 , 5
#        string = 'hello'
#####


# 2. Which of the following is a variable, and which is a string?

# spam
# 'spam'


#####
# answer - spam == variable && 'spam' == String
#####


# 3. Name three data types.

#####
# answer here's 4 - Int, float, string, boolean
#####

# 4. What is an expression made up of? What do all expressions do?

#####
# answer - Expressions consist of values (such as 2) and operators (such as +),
#          and they can always evaluate (that is, reduce) down to a single value.
#          That means you can use expressions anywhere in Python code that you
#          could also use a value.
#####

# 5. This chapter introduced assignment statements, like spam = 10.
#    What is the difference between an expression and a statement?


#####
# answer - statement is evaluated as it's written / read _-_ spam = 10 == statement - already reduced
#          expression has to be reduced _-_ spam = 6 + 4 == expression
#####


# 6. What does the variable bacon contain after the following code runs?

# bacon = 20
# bacon + 1


#####
# answer - 21
#          bacon is now equal to the int 21
#####


# 7. What should the following two expressions evaluate to?

# 'spam' + 'spamspam'
# 'spam' * 3

#####
# answer - they will both equal 'spamspamspam' with string concatenation (con-cat-eh-nation)
#####

# 8. Why is eggs a valid variable name while 100 is invalid?

#####
# answer - using a number value as a variable is confusing and bad practice - don't cut your hair with a weed whacker
#          A good variable name describes the data it contains
#          var names do not start with a number and do not have hyphens, spaces, or special characters.
#####

# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?


#####
# answer - int()   ... health = 50 ... int(health) == 50
#          float() ... health = 50 ... float(health) == 50.0
#          str()   ... health = 50 ... str(health) == '50'
#####


# 10. Why does this expression cause an error? How can you fix it?

# 'I have eaten ' + 99 + ' burritos.'

#####
# answer - can't concatenate ( how do you spell that?) a string and an integer.
#        instead use
#        'I have eaten ' + str(99) + ' burritos.'
#        or
#         'I have eaten 99 burritos.'
#####


# Extra credit: Search online for the Python documentation for the len() function. It will be on a web page titled “Built-in Functions.”
# Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell.


# len() function - pass into parenthesis an object and it returns the length of the object
#            EXAMPLE - len("tony") == 4  .....  len("three") == 3  .....  len('3') == 1

# round() function - syntax - round(number, digits) rounds a float or int to x amount of decimal places (digits default is 0)
#            EXAMPLE - round(4) == 4 ..... round(4,4) == 4 ..... round(4.45678,2) == 4.46 more examples below


print(round(4))                    # rounds to 4
print(round(4, 4))                 # rounds to 4
print(round(4.45678, 2))           # rounds to 4.46
print(round(44.444444, 3))         # rounds to 44.444
print(round(432.123, 1))           # rounds to 432.1
print(round(556.8, 3))             # rounds to 556.8
print(round(55.667788, 2))         # rounds to 55.67
print(round(-.098636435, 4))       # rounds to -0.0986
