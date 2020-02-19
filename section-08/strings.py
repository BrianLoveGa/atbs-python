# strings

#  'hello'   - works

#  'that is alice's cat  - no work

# 'say Hi to Bob\'s mom' - works

# "say Hi to Bob's mom" - works

print('Hello there! \n How Are You?\n I\'m Fine Thanks.')  # - works

print(r'That is Carol\'s Cat')

print(""" Dear Alice,
Eve's cat has been arrested for :
cat napping, cat burglary, and catnip posession.""")

# can't change string, but can change case - recall .upper() .lower() .join() .split()

# string tests and checks
# .isalpha() - letter only
# .isalnum() - letters and numbers
# .isdecimal() - numbers only
# .isspace() - white space (tab or spacebar)
# .istitle() - Title Case Only
# .startswith() - the first character
# .endswith() - the last character

print('Hello World'.startswith('H'))  # - returns True

# .split() - splits string up on any character
# .rjust() - right justify
# .ljust() - left justify
# .center() - add chars to either side
# .strip() - remove all spaces
# .lstrip() - remove spaces from left side
# .rstrip() - remove spaces from right side

print("middle".center(20, '*'))
print("middle".rjust(20, '*'))
print("middle".ljust(20, '*'))

print('hello ' + 'world ' + ' turnips')

name = 'Michelle'
place = "Sarah's Apartment"
time = '6 pm'
food = 'Spinach Dip'

print('Hello '+name+', you are invited to a party at ' +
      place+' at '+time+' please bring '+food+'.')

# string interpolation
print('Hello %s, you are invited to a party at %s at %s please bring %s.' % (name,place,time,food))