# this program says hello and asks for your name


print("hello there world - Brian can code")


print("what is your name?") # ask the user for their name as input
my_name=input() # originally as myName - but this is python not JS
print("it is good to meeet you, " + my_name)
print("the length of your name is:")
print(len(my_name))


print("what is your age?") # ask user for their age - hope they don't think it's rude
my_age = input()
print("You will be " + str(int(my_age) +5)+ " years old about five years from now")

# extra credit

x = int(my_age) - 2
print(my_name + " was " + str(x) + " years old 2 years ago")