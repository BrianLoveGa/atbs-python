name = 'Alice'
if name == 'Alice':
    # use the \ to escape when you need an ' in your string
    print('Well hello there little Alice, How\'s the white rabbit?')
print('done')

print('type the password below')
password = input()

if password == 'swordfish':  # what a good movie that was - any Travolta fans out there reading this?
    print('access granted')
else:
    print('wrong password - access denied - NO SOUP FOR YOU!')


print("if-elif-elif-elif")

name = 'bob'
age = 3000

if name == 'Alice':  # - False so skips it
    print('Hi Alice, nice to see you again.')
elif age < 12:  # - False so skips it
    print('You are not Alice, kiddo.')
elif age > 2000:  # - True so executed and program stops here
    print('Unlike you, Alice is not an undead, immortal vampire')
elif age > 100:  # not reached unless we change the values of age or name
    print("You are too old to be Alice, grannie.")
# extra credit
elif name == 'bob':
    print("it won't reach this line even though it is True")


print("no more of that")

############
# 'Truthy' and 'Falsey'

print("enter your name please")
name = input()
if name:
    print("thank you for entering your name as " + name)
    print(bool(name))
else:
    print("You did not enter a name. I even said please.")


# blank string or empty string or "" == Falsey == False
# 0 == Falsey
# 0.0 == Falsey

# 1 == Truthy
# 11.11 == Truthy
# "anything" == Truthy
# "any string or combo"
# "   " == Truthy - if you type spaces or even just one space it's techniccaly not an empty string

print(bool(0))  # returns False
print(bool(""))  # returns False
print(bool("zero"))  # returns True
print(bool("              "))  # returns True
print(bool("Chuck Norris"))  # returns True
print(bool(765439))  # returns True
