# pages 67-71 in book


spam = 42 # global variable


print(spam)
print('some code here')


def eggs():
    spam = 'yum yum' # local variable

eggs()

print(spam)
# spam did not change values due to scope
print('some more code here')



# SCOPE RULES
# 1) Code in global scope cannot use any local variables
# 2) Code in a local scope can access global variable
# 3) Code in one function's local scope cannot use variables in another local scope
# 4) Code in one function's local scope cannot use variables in any other local scope


