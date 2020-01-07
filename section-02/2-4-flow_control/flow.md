__A flow chart__

{start}
   |
   |
   |
   [is raining ?] -- yes --> [have umbrella ?] -- no --> [Wait awhile] <----------|
        |                           |                           |                 |
        |                           |                           |                 |
        No                        Yes                     [is raining ? ] -- yes --
        |                           |                           |
        |                           |                           NO
        |                           |                           |
     [Go outside then]  <------------   <------------------------
            |
            |
            |
            |
          {end}


Boolean = True or False in PY

comparison operators

******
Operator      ||  MEANING
******

+ ==         ||  Equal to   (no === here)
+ !=         ||  Not equal to
+ <          ||  Less than
+ >          ||  Greater than
+ <=         ||  Less than or equal to
+ >=         ||  Greater than or equal to

True expressions:

42 == 42
2 != 42
42 < 100
42 >= 42
42 == 42.0

Flase expressions:

42 == 'forty two'
42 == '42'
42 == 41
42 < 42
42 == 'hello'
42 != 42



Boolean operators

And , Or , Not

__Truth Table__

expression      ||    evaluates to...
******
True and True   ||    True
True and False  ||    False
False and True  ||    False
False and False ||    False

******

True or True   ||    True
True or False  ||    True
False or True  ||    True
False or False ||    False

******

not True       || False
not False      || True
