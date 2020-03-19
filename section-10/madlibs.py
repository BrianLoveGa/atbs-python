import sys

# lets make a mad libs game


# welcome to the __(noun)__ news network's live coverage
# of the 20 _(number between 10 and 79)_  election.
# I am your host _(name)_ . The current top story is of course about
# _(politician name)_ and the running _(adverb)_ scandal.
# from when they were caught _(verb)_ with a chicken on
# the _(noun)_ farm. For more we go to _(adjective)_ _(noun)_
#  outside the courthouse


# A vacation is when you take a trip to some _(adjective)_ place
# with your _(adjective)_ family. Usually you go to some place
# that is near a/an _(noun)_ or up on a/an _(noun)_.
# A good vacation place is one where you can ride _(plural noun)_
# or play _(game)_ or go hunting for _(plural noun)_ . I like
# to spend my time _(ING verb)_ or _(ING verb)_.
# When parents go on a vacation, they spend their time eating
# three _(plural noun)_ a day, and fathers play golf, and mothers
# sit around _(ING verb)_. Last summer, my little brother
# fell in a/an _(noun)_ and got poison _(plant)_ all
# over his _(body part)_. My family is going to go to(the)
# _(place)_, and I will practice (ing verb)_. Parents
# need vacations more than kids because parents are always very
# _(adjective)_ and because they have to work _(number)_
# hours every day all year making enough _(plural noun)_ to pay
# for the vacation.


# Have you heard the new band _(ing verb)_ _(adjective)_ _(noun)_ ?
# They are the next big thing from _(place)_ . Their lead _(insturment)_
# player from sweden and their guitarist with the _(color)_ hair met in 
# high school . I won tickets listening to _(noun)_ _(adjective)_ radio
# do you want to come to the show with me? I'll buy us _(plural noun)_
# when we get there and we will stop for _(plural noun)_ beforehand.
# Come on you know it will be a/an _(ing verb)_ time!


# Oh boy! That new movie _(city)_ _(plural noun)_ coming out next month,
# you know about the _(plural noun)_ _(ing verb)_ all night long,
# it's going to be the _(adjective)_ movie to come out this year!
# I've heard it's already got _(name)_ award buzz. Well my friend
# has an awards cut since he's on the _(noun)_ _(adverb)_ commitee of 
# _(city)_ and he let me borrow it. I'm going to need you to go get us 
# some _(plural noun)_ and some frosty _(plural noun)_ for snacks.
# Here's _(number)_ _(animal)_ that oughta cover my share.


# One day, Gerald and Patti decided to go on a _(noun)_ .
# "Patti! We will need to gather many things!" Gerald said.
# They began to _(verb)_ . "Will we _(verb)_ ?" asked Patti.
# "Of course!" Gerald said. "So we will need to pack
#  _(noun)_ ." Patti _(verb)_ home to try to find 
# _(noun)_ to take with them. Gerald _(verb)_ in his closet
# to get a _(noun)_ in case it rained. "I think we might 
# need _(noun)_ so we don't get too hungry", Patti said
# when she returned. They made sure to pack _(noun)_ to
# munch on. "I really hope we get to _(verb)_ in the ocean
# when we get there!" Patti said. So Gerald and Patti 
# jumped in their _(noun)_ and left. "What should we do
# after this?" Gerald asked. "Maybe we can try to _(ing verb)_
# ," Patti said. Gerald replied, "I have always wanted 
# to _(verb)_ in a forest."



# let the games begin

print("want to play mad libs?")
print("enter yes, or ok")
play = input(">>")
if play.lower() in ["yes", "sure", "ok"]:
    # shoul add in a loop so can play all of them.
    print("lets play")
    print("there are currently 5 'mad libs style games' \n so pick '1' , '2' , '3' , '4' or '5'..." )
    choice = input(">>")
    if choice in [1, "1", "one"]:
        print("Choice one good call please - enter your name")
        name = input(">>")
        print("enter a noun")
        noun1 = input(">>")
        print("enter a number between 10 and 79")
        number = input(">>")
        print("enter a famous name")
        poliName = input(">>")
        print("enter an adverb")
        adverb = input(">>")
        print("enter an ing verb")
        verbING = input(">>")
        print("enter a noun")
        noun2 = input(">>")
        print("enter an adjective")
        adj = input(">>")
        print("and finally lastly enter a noun")
        noun3 = input(">>")
        print("thanks now here's the story")
        print(" ..... ")
        print("Welcome to the " + noun1 + " news network's live coverage")
        print("of the 20" + str(number) + " election.")
        print("I am your host " + name +
              ". The current top story is of course about")
        print(poliName + " and the running " + adverb + " scandal.")
        print("When they were caught " + verbING + " with a chicken!")
        print("On the now infamous " + noun2 + " farm.")
        print("For more we go to " + adj + " " +
              noun3 + " live outside the courthouse...")
    elif choice in[2,"2","two"]:
        # adj1
        print("Great choice #2 please enter an adjective ")
        adj1 = input(">>")
        # adj2
        print("please enter another adjective")
        adj2 = input(">>")
        # noun1
        print("excellent please enter a noun")
        noun1 = input(">>")
        # noun2
        print("please enter a second noun")
        noun2 = input(">>")
        # plural noun1
        print("please enter a pural noun")
        plNoun1 = input(">>")
        # game
        print("please enter a game")
        game = input(">>")
        # plural noun2
        print("awesome just a few more enter a plural noun")
        plNoun2 = input(">>")
        # ing verb1
        print("enter an ING verb please")
        ingVerb1 = input("")
        # ing verb2
        print("again again another ING verb please")
        ingVerb2 = input(">>")
        # plural noun3
        print("enter another plural noun ")
        plNoun3 = input(">>")
        # ing verb3
        print("enter an ING verb")
        ingVerb3 = input(">>")
        # noun3
        print("enter a noun")
        noun3 = input(">>")
        # plant
        print("enter an plant ")
        plant = input(">>")
        # body part
        print("enter a body part")
        body = input(">>")
        # place
        print("enter a place")
        place = input(">>")
        # ing verb4
        print("enter one more ING verb (last one I promise)")
        ingVerb4 = input(">>")
        # adj3
        print("enter an adjective")
        adj3 = input(">>")
        # number
        print("enter a number")
        numb = input(">>")
        # plural noun4
        print("lastly enter another plural noun")
        plNoun4 = input(">>")
        print("awesome here's the fun")
        print(" ........................")
        print(" ........................")
        print(" ........................")
        print("A vacation is when you take a trip to some " + adj1 + " place")
        print("with your " + adj2 + " family. Usually you go to some place ")
        print("that is near a/an " + noun1 + " or up on a/an " + noun2+". ")
        print("A good vacation place is one where you can ride " + plNoun1)
        print("or play " + game+" or go hunting for " + plNoun2 + ". I like ")
        print("to spend my time " + ingVerb1 + " or " + ingVerb2 + ". ")
        print("When parents go on a vacation, they spend their time eating")
        print("three "+plNoun3+" a day, and fathers play golf, and mothers ")
        print("sit around "+ingVerb3+ ". Last summer, my little brother ")
        print("fell in a/an "+ noun3+" and got poison "+ plant +" all ")
        print("over his "+ body +". My family is going to go to(the) ")
        print( place+", and I will practice " + ingVerb4 + ". Parents") 
        print("need vacations more than kids because parents are always very")
        print( adj3 +" and because they have to work " + str(numb) + " hours ")
        print("every day all year making enough "+ plNoun3 + " to pay ")
        print("for the vacation.")
    elif choice in [3,"3","three"]:
        print("You picked the third story, Awesome! Please enter an ing verb")
        verbing = input(">>")
        print("please enter an adjective")
        adj = input(">>")
        print("enter a noun")
        noun = input(">>")
        print("enter a city")
        place = input(">>")
        print("enter a musical insturment")
        inst = input(">>")
        print("enter a color")
        color = input(">>")
        print("enter a noun")
        nounA = input(">>")
        print("enter an adjective")
        adjA = input(">>")
        print("enter a plural noun")
        plural = input(">>")
        print("enter a plural noun")
        pluralA = input(">>")
        print("enter an ing verb")
        verbingA = input(">>")
        print("thanks .... here is what you made ...")
        print("Have you heard the new band " + verbing +" "+ adj +" "+ noun+"?")
        print("They are the next big thing from "+ place+". Their lead "+inst )
        print("player from Sweden and their guitarist with the "+color+" hair met in ")
        print("high school. I won tickets listening to " + nounA +" "+ adjA + " radio ")
        print("do you want to come to the show with me? I'll buy us " + plural )
        print("when we get there and we will stop for " + pluralA + " beforehand.")
        print("Come on you know it will be a/an " + verbingA + " time! ")
    elif choice in [4,"4","four"]:
        print("the 4rd 'mad lib style' game \n please enter a city")
        city = input(">>")
        print("enter a plural noun")
        plnoun = input(">>")
        print("enter a plural noun")
        plnoun2 = input(">>")
        print("enter an ing verb")
        ingverb = input(">>")
        print("enter an adjective")
        adj = input(">>")
        print("enter a name")
        name = input(">>")
        print("enter a noun")
        noun = input(">>")
        print("enter an adverb")
        adv = input(">>")
        print("enter a city")
        city2 = input(">>")
        print("enter a plural noun")
        plnoun3 = input(">>")
        print("enter a plural noun")
        plnoun4 = input(">>")
        print("enter a number")
        numb = input(">>")
        print("enter a plural animal")
        plal = input(">>")
        print("Excellent round 4 done ")
        print("Oh boy! That new movie " +city+" "+plnoun+" coming out next month,")
        print("you know about the " +plnoun2 +" "+ ingverb+ " all night long,")
        print("it's going to be the "+ adj +" movie to come out this year!")
        print("I've heard it's already got tons of " + name +" award buzz. Well my friend")
        print("has an 'awards cut' since he's on the "+ noun+ " "+ adv +" commitee of")
        print(city2 +" and he let me borrow it. I'm going to need you to go get us")
        print("some "+ plnoun3 +" and some frosty "+plnoun4+" for snacks.")
        print("Here's "+ str(numb) +" "+ plal +" that oughta cover my share.")
    else:
        print("Option five Gerald and Patti's story nice pick \n please enter a noun")
        noun1 = input(">>")
        print("please enter a verb")
        verb1 = input(">>")
        print("please enter a second verb")
        verb2 = input(">>")
        print("please enter a second noun")
        noun2 = input(">>")
        print("and enter another verb")
        verb3 = input(">>")
        print("now another noun")
        noun3 = input(">>")
        print("and back to another verb")
        verb4 = input(">>")
        print("enter another noun")
        noun4 = input(">>")
        print("please enter a noun again")
        noun5 = input(">>")
        print("and another noun here")
        noun6 = input(">>")
        print("one more verb again")
        verb5 = input(">>")
        print("another noun this time")
        noun7 = input(">>")
        print(" enter an ING verb please")
        ingVerb = input(">>")
        print(" and lastly one final verb")
        verb6 = input(">>")
        print("All done here's the funny bit")
        print("One day, Gerald and Patti decided to go on a " + noun1 +".")
        print("'Patti! We will need to gather many things!' Gerald said.")
        print("They began to "+ verb1 +". 'Will we "+ verb2 +"?' asked Patti.")
        print("'Of course!' Gerald said. 'So we will need to pack extra")
        print(noun2 +".' Patti "+ verb3 +" home to try to find ")
        print(noun3 +" to take with them. Gerald "+ verb4 +" in his closet")
        print("to get a " + noun4 + " in case it rained. 'I think we might") 
        print("need " + noun5 + " so we don't get too hungry', Patti said")
        print("when she returned. They made sure to pack " + noun6 + " to ")
        print("munch on. 'I really hope we get to " + verb5 + " in the ocean")
        print("when we get there!' Patti said. So Gerald and Patti") 
        print("jumped in their " + noun7 + " and left. 'What should we do")
        print("after this?' Gerald asked. 'Maybe we can try " +  ingVerb )
        print(",' Patti said. Gerald replied, 'I have always wanted ")
        print("to " + verb6 + " in a forest.'")

else:
    print("good bye")
    sys.exit()



# 5 decent ones, time to make a loop so can replay without exiting the game. 