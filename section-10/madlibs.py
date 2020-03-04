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


print("want to play mad libs?")
print("enter yes, or ok")
play = input(">>")
if play.lower() in ["yes", "sure", "ok"]:
    print("lets play")
    print("there ar only 2 libs so pick '1' or '2'")
    choice = input(">>")
    if choice in [1, "1", "one"]:
        print("enter your name")
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
    else:
        # adj1
        print("Great choice please enter an adjective ")
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
        print("again agin another ING verb please")
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
        print("enter one final ING verb")
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
else:
    print("good bye")
    sys.exit()
