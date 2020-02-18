import copy  # - formatter moves to top but it was called 3/4 thru lesson
# # 93 -103 strings and lists

spam = list('Hello')
for letter in spam:
    print(letter)

print(spam)
print(spam[0]+spam[-2])
print(spam[2:4])
print('h' in spam)
print('l' in spam)
print('h' in 'hello')

# string value = immutable can't be changed
# list value mutable = can be changed

# make new strings form old ones with slice
name = 'Sophie a cat'
print(name)
newName = name[0:7] + 'the' + name[8:12]
print(newName)


# refrences

spam = 42
cheese = spam
spam = 100
print(str(cheese) + " and " + str(spam))

spam = [0,1,2,3,4,5]
print(spam)

cheese = spam

cheese[1] = 'green'
print(cheese)
print("what")
print(spam)
# how did spam change when we only changed cheese?
# underneath python assigns a uniqe numeric id to each variable as a refrence
# immutable values don't have this problem b/c they can onky be replaced by new values
# this can lead to bugs if you are re-using variables and functions too much

def eggs(cheese):
    cheese.append('hello')

bacon = [1,2,3]
eggs(bacon)
print(bacon)

# import copy - formatter moves to top but it was called 3/4 thru lesson
print("copy copy")
frog = ['a','b','c','d']
lizard=copy.deepcopy(frog)
lizard[1] = 42
print(frog)
print(lizard)

# line continuation

# lists can span multiple lines


# \ line character or \n to skip and make new line (from simple game moons ago)

print("four score and seven years ago " + \
    "our forefathers did their laundary and watched halo2 on you tube")


#  strings and lists can do a lot of the same things
#  STRINGS ARE IMMUTABLE
#  immutable values (strings and tuples) can't be modified in place
# mutable values (like lists) can be changed in place
# variables contain refrences to lists
# when passing a list argument to a function you are actually passing a list refrence
# changes made to a list in a function will affect the list outside the function
# the \ line continuation character - used to stretch code qcross multiple lines if needed
# for read - ability