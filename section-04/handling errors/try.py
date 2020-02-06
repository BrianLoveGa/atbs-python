# pages 72 & 73


def div42by(divideby):
    return 42 / divideby


# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))


# atbs-python/section-04/handling errors/try.py"
# 21.0     === 42 / 2
# 3.5      === 42 / 12
# Traceback(most recent call last):
#   File "/Users/brianloveless/Desktop/code/practice/2020/udemy/atbs-python/section-04/handling errors/try.py", line 10, in < module >
#   print(div42by(0))
#   File "/Users/brianloveless/Desktop/code/practice/2020/udemy/atbs-python/section-04/handling errors/try.py", line 5, in div42by
#   return 42 / divideby
# ZeroDivisionError: division by zero


def div44by(num):
    try:
        return 44 / num
    except ZeroDivisionError:
        print(" error you can't divide by 0 dummy ")


print(div44by(2))
print(div44by(12))
print(div44by(0))
print(div44by(1))


# below works fine unless user types NAN (not a number) 

# print('How many dogs do you have / own ?')   # b/c dogs > cats
# numDogs = input()
# if int(numDogs) >=4:
#     print("that's a lotta dogs")
# else:
#     print("that's not that many doggos")

# lets change it to include a try except block


print('How many dogs do you have / own ?')   # b/c dogs > cats
numDogs = input()
try:
    if int(numDogs) >=4:
        print("that's a lotta dogs")
    else:
        print("that's not that many doggos")
except ValueError:
    print("you should enter a number like 2 or 7 or 34276")