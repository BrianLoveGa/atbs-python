import math
import random
#  import this
import sys
import os  # seperate with space and comma
import pyperclip


random.randint(1, 10)  # been using this

# print("hello")
# sys.exit()
# print("bye bye")  # never reached due to sys exit function above


pyperclip.copy("hello there world")

pyperclip.paste()


def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello()
hello()
hello()


def greet(name):
    print("hello there " + name)

greet("Brian")
greet("Billy")
greet("Bobby")
