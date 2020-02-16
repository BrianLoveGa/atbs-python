for i in range(4):
    print(i)

0
1
2
3

print(list(range(10)))

spam = list(range(0, 100, 2))

print(spam)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders', 'paper clips']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])



# multiple assigment

cat = ['fat', 'orange', 'loud']

size = cat[0]
color = cat[1]

# ....

size, color, dispisotion = 'skinny', 'black', 'quiet'

a = 'AAA'
b = 'BBB'

a,b = b,a

print(a)

spam = 42
spam = spam +1
spam +=1
print("just like js with the += bit watch it'll be 44 down there")
print(spam)
print("told ya so")

# for loops iterate over values in a list
# range function returns list like value
# can be passed to list function if you need it spelled out
# variables can swap values simultaneously using multiple assigmnets
# augmented assigmnet operators like += are shortcuts


