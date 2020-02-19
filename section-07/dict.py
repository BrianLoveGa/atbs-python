# like a list a dictionary is a collection of many values

# key value pair

myCat = {'size': "fat", 'name': "spunky", 'color': "orange"}

print('my cat has ' + myCat['color'] + ' fur')
print(myCat['size'])

# dictionaries have no 'order'
print([1, 2, 3] == [3, 2, 1]) # false
print([1, 2] == [1, 2]) # true

spam = {'color': "orange", 'size': "fat", 'name': "spunky"}

print(spam == myCat) # true

# trying to access a key that does not exist will cause error  
# use in and not in to check if key or value is in dict

print('name' in spam)
print('orange' not in myCat)
print('fat' in myCat)

print(list(spam.items())) # returns tuples

for k, v in spam.items():
    print(k,v)

# tuples are like lists but immutable and use () instead of []    



eggs = {'name':'Zophie', 'species':'cat', 'age':8}

print(eggs.get('age', 0))
print(eggs.get('color', 'color undefined'))

if 'color' not in eggs:
    eggs['color'] = 'black'

eggs.setdefault('legs', 4)

print(eggs)

