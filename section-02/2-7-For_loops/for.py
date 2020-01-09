# mmmm pie, i could go for PI, pie, PY


import random
print('my name is')
for i in range(5):
    print('Jimmy Five times ' + str(i))


# guess i should look up Gauss
###

total = 0
for num in range(101):
    total = total + num
    print(total)


    # same as 1 + 99, 2+ 98, 3+97 .... 49+51 (49 100's + 50 + 100)
    # === 50  100's + 50
    # ... == 5050

# like JS while and for loops can almost always be interchanged


# print('my name is')
# for i in range(5):
#     print('Jimmy Five times ' + str(i))

# or

# print('my name is')
# i = 0
# while i < 5:
#     print('Jimmy Five times ' + str(i))
#     i=i+1


# print('my name is')
# for i in range(12, 16):
#     print('Jimmy Five times ' + str(i))


# starts at 12
# works at 12, 13, 14, 15

# format for range function (start#, stop#, step#)    Step default is 1

print('even numbers two thru twenty four')
for i in range(2,25,2):
    print('even this # ' + str(i))

print('fast count down')
for x in range(30,-1,-1):
    # for good luck
    if x == 13:
        continue
    print('Tee minus ... ' +str(x))
    
    if x==7:
        print("start rockets") # they used to do it like this
    if x==0:
        print('blastoff')

# lucky lottery numbers fantasy 5 numbers 1 - 42
for j in range(5):
    print(random.randint(1, 42))



#evaluate


print(bool((5 > 4) and (3 == 5)))
print(bool(not (5 > 4)))
print(bool((5 > 4) or (3 == 5)))
print(bool(not ((5 > 4) or (3 == 5))))
print(bool((True and True) and (True == False)))
print(bool((not(False)) or (not(True))))


print(abs(7))
