# 6.13 - like a JS array

#  ['cat', 'bat', 'rat', 'dog']

spam = ['cat', 'bat', 'rat', 'dog']

# spam[0] = 'cat'

# layered lists

cake = ['frog', 'lizard', ['car', ['ford', 'chevy'],
                           'bus', 'truck'], 'snake', 'toad', ['tree', 'flower']]

# can access forwards

print(cake[2][1][1])

print("The " + cake[0] + " can't drive a " + cake[2]
      [1][1] + " " + cake[2][3] + " all the way to Houston!")

# or backwards

print("the " + cake[-1][1] + " will grow if the "+cake[-2]+" doesn't eat it")


# splice
print(cake[1:4])


spam = [10, 20, 30]

spam[1] = 'hello'

print(spam)

sprite = [10, 20, 30]

sprite[1:1] = 'jim', 'tim'

print(sprite)

sprunk = [10, 15, 20, 25, 30]

# DELETE FROM LIST

del sprunk[2]

print(sprunk)

# get length
print(len(sprunk))
print(len(sprite))
print(len(sprunk + sprite))


# in and not in operators

5 in [2,3,4,5,6]

# is true

'cat' not in [2, 3, 4, 5, 6]

# also true since it's not in the list


# A list is a value that contains multiple values
# The values in the list are called items
# You access items in list with integer values
# indexes start at 0
# you can use negative ( -1 refers to last item in list)
# multiple items from list using slice
# slice has 2 indexes ... list[x : y]'list_addition' ==  start at X go up to but not including Y
# convert value into list with list()
# can use len() for length, add and multiply just like strings