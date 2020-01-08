# import this
# x=0 ... while  x > 5 print hello and add 1 to x returns hellohellohellohellohello
# x=0 ... while  x >= 5 print hello and add 1 to x returns hellohellohellohellohellohello

spam = 0
while spam < 5:
    print('Hello Jello Hola Bonjour tout le monde')
    spam = spam +1

eggs = 0   
if eggs <5:
    print("my dad is a lumberjack and he's ok")
    eggs = eggs +1

# without a break statement if only goes through once, while goes until condition met

name = ""

while name != 'your name':
    print('please enter your name')
    name= input()
print("thanks")


# break statements

pw = ""

while True:
    print("please enter your password")
    pw = input()
    if pw == 'your password':
        break
print('thanks for reading carefully')

##

bacon = 0
while bacon < 5:
    bacon = bacon +1
    if bacon == 3:
        continue
    print('bacon is good and ' + str(bacon))



# ctrl c if stuck in infinite loop - 
# or just always have one break case / base case when looping

# don't get caught in recursion 
# don't get caught in recursion 
# don't get caught in recursion 
# don't get caught in recursion 
# don't get caught in recursion 
# don't get caught in recursion 
# don't get caught in recursion 
