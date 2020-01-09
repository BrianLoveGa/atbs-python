# Practice Questions

******

1. What are the two values of the Boolean data type? How do you write them?

True and False - first letter cap

2. What are the three Boolean operators?

and &&
or ||
not !=

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).


Expression           Evaluates to . . .

True and True         True

not False             True

True or True          True

True or False         True

False or True         True

False or False        False

not True              False

True and False        False

False and True        False

False and False       False

4. What do the following expressions evaluate to?
    check bottom of for.py
(5 > 4) and (3 == 5) ..                  true and false = False
not (5 > 4) ..                                 not true = Flase
(5 > 4) or (3 == 5) ..                    true or false = True
not ((5 > 4) or (3 == 5)) ..          not true or false = False
(True and True) and (True == False) ..   true and false = False
(not False) or (not True) ..              true or false = True

5. What are the six comparison operators?

== equals
!= not equal
< greater than
> less than
<= greater than or equal to
>= less than or equal to

6. What is the difference between the equal to operator and the assignment operator?

= assignment / sets      ... spam = 10  ... = 10
== comparison / equal to ... spam == 10 ... = True ... spam == "ten" = False


7. Explain what a condition is and where you would use one.

The Boolean expressions you’ve seen so far could all be considered conditions, which are the same thing as expressions; condition is just a more specific name in the context of flow control statements. Conditions always evaluate down to a Boolean value, True or False. A flow control statement decides what to do based on whether its condition is True or False, and almost every flow control statement uses a condition.

8. Identify the three blocks in this code:

spam = 0
if spam == 10:
    print('eggs')    ----- (1)
    if spam > 5:
        print('bacon')  ---- (2)
    else:
        print('ham')  --- (3)
    print('spam')
print('spam')

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam = 1

def spam_equals():
    if spam == 1:
        print("hello")
    elif spam == 2:
        print("howdy")
    else:
        print('Greetings')

spam_equals()


10. What keys can you press if your program is stuck in an infinite loop?

control c

11. What is the difference between break and continue?

continue == skip
break == stop

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?


those are all equal, default values are _,1,1
start at 0 count up to 9 (for a total of 10) by 1

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

for i in range(1,11):
    print(i)
    

x=1
while x <11:
    print(x)
    x+=1

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?


dot notation

import spam

spam.bacon()

Extra credit: Look up the round() and abs() functions on the internet, and find out what they do. Experiment with them in the interactive shell.

round is the same as last section...

round() function - syntax - round(number, digits) rounds a float or int to x amount of decimal places (digits default is 0)

EXAMPLE - round(4) == 4 ..... round(4,4) == 4 ..... round(4.45678,2) == 4.46 more examples below


absolute value - abs() - syntax - abs(number)

EXAMPLE - abs(-7) == 7 ...  abs(7) == 7
