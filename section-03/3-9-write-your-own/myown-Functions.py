# mini programs

def hello():
    print("howdy!")
    print("howdy CHEF !!! ")
    print("Well hello there children!")


hello()
hello()
hello()

# avoid duplication when possible


def greet(name):
    print('Hello ' + name)

greet('Alice')
greet('Bob')


# name = parameter in function 
# Alice and Bob are arguments / values

# 'hello has ' + str(len('hello')) + ' letters in it.'
# # 'hello has ' + str(5) + ' letters in it.'
# # # 'hello has ' + '5' + ' letters in it.'
# # # # 'hello has 5' + ' letters in it.'
# # # # # 'hello has 5 letters in it.'

print('plusone')

def plusOne(number):
    return number + 1

new = plusOne(5)
newNumber = plusOne(1000)

print(new)
print(newNumber)

def silly():
    print('cat', 'dog', 'mouse', sep="---dOIXIOb---")

silly()



# Functions are like 'mini programs' inside your program
# The main point of them os to avoid duplicate code
# def statement defines function
# function inputs are called arguments
# function output is called return value
# parameters are the variables in between the functions parentheses in the def statement
# return value is specified by the return statement
# every function has a return value - if there is no return statement default value is none 
# keyword arguments to functions are usually for optional arguments 
# the print function has keyword arguments end and sep 

