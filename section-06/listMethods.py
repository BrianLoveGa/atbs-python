spam = ['helo', 'hello', 'howdy', 'hey hey hey']

print(spam.index('hello'))


# variable . methodName('paramater/value')

# value error exception raised if query item not in list
# index will only return the first insatnce of value

# append add value to end

spam.append('hola')
print(spam)

spam.insert(1, 'aloha')

print(spam)

spam.append('bat')
print(spam)
spam.remove('bat')
print(spam)
del spam[1]
del spam[0]

print(spam)

# .append and .insert and .remove only works on lists


num = [2, 5, -7, 1, 3.14]

num.sort()
print(num)

spam = ['dog', 'cat', 'rat', 'bat']
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

# an error will occur if strings and ints can't be sorted
# uses ASCII key - Caps come before lower case

trash = ['ants', 'bats', 'cars', 'Trucks', 'Vans', "Planes"]
trash.sort()
print(trash)
trash.sort(key=str.lower)

print(trash)


# methods are functions that are called on values
# The index() list method returns the index value of an item
# the append() adds a value to end of list
# the insert() adds a value where you specify in list
# the remove() removes item specified by value
# the del list[n] deletes list item by index value
# the sort() orders lists
# can use sort(reverse=True) for backwards sort
# can use sort(key=str.lower) to sort regardless of Caps 
# these operate on the list in place instead of returning a new list value