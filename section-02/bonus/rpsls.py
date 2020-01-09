import random
import sys


# lets zazz it up here and make a rock paper scissors 
#  with lizard & spock version
# https://en.wikipedia.org/wiki/Rock_paper_scissors#Additional_weapons

wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # The player input loop.
        print('Enter your move: (ro)ck (pa)per (sc)issors (li)zard (sp)ock or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            print('thanks for playing your final score was: ')
            print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
            sys.exit()  # Quit the program.
        if playerMove in['ro','pa','sc','li','sp'] :
            break  # Break out of the player input loop.
        print('Type one of ro, pa, sc, li, so, or q.')

    # Display what the player chose:
    if playerMove == 'ro':
        print('ROCK versus...')
    elif playerMove == 'pa':
        print('PAPER versus...')
    elif playerMove == 'sc':
        print('SCISSORS versus...')
    elif playerMove == 'li':
        print('LIZARD versus...')
    elif playerMove == 'sp':
        print('SPOCK versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 5)
    if randomNumber == 1:
        computerMove = 'ro'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'pa'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 'sc'
        print('SCISSORS')
    elif randomNumber == 4:
        computerMove = 'li'
        print('LIZARD')
    elif randomNumber == 5:
        computerMove = 'sp'
        print('SPOCK')


    # Display and record the win/loss/tie:
    # start with a tie
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1

    # ways you win
    # 2 ways to win with each option - 6 total outcomes

    elif playerMove == 'ro' and computerMove == 'sc':
        print('You win! rock crushes scissors')
        wins = wins + 1
    elif playerMove == 'ro' and computerMove == 'li':
        print('You win! rock smashes lizard')
        wins = wins + 1
    elif playerMove == 'pa' and computerMove == 'ro':
        print('You win! paper covers rock')
        wins = wins + 1
    elif playerMove == 'pa' and computerMove == 'sp':
        print('You win! paper disproves Spock')
        wins = wins + 1
    elif playerMove == 'sc' and computerMove == 'pa':
        print('You win! scissors cuts paper')
        wins = wins + 1
    elif playerMove == 'sc' and computerMove == 'li':
        print('You win! scissors decapitates lizard')
        wins = wins + 1
    elif playerMove == 'li' and computerMove == 'sp':
        print('You win! lizard poisions Spock')
        wins = wins + 1
    elif playerMove == 'li' and computerMove == 'pa':
        print('You win! lizard eats paper')
        wins = wins + 1
    elif playerMove == 'sp' and computerMove == 'sc':
        print('You win! Spock smashes scissors')
        wins = wins + 1
    elif playerMove == 'sp' and computerMove == 'ro':
        print('You win! Spock vaporizes rock')
        wins = wins + 1

    # now the 6 losing scenarios 2 for each

    elif playerMove == 'ro' and computerMove == 'pa':
        print('You lose! computer paper covered your rock')
        losses = losses + 1
    elif playerMove == 'ro' and computerMove == 'sp':
        print('You lose! computer Spock vaporized your rock')
        losses = losses + 1
    elif playerMove == 'pa' and computerMove == 'sc':
        print('You lose! computer scissors cut your paper')
        losses = losses + 1
    elif playerMove == 'pa' and computerMove == 'li':
        print('You lose! computer lizard ate your paper')
        losses = losses + 1
    elif playerMove == 'sc' and computerMove == 'ro':
        print('You lose! computer rock smashed your scissors')
        losses = losses + 1
    elif playerMove == 'sc' and computerMove == 'sp':
        print('You lose! computer Spock smashed your scissors')
        losses = losses + 1
    elif playerMove == 'li' and computerMove == 'ro':
        print('You lose! computer rock smashed your lizard')
        losses = losses + 1
    elif playerMove == 'li' and computerMove == 'sc':
        print('You lose! computer scissors decapitated your lizard')
        losses = losses + 1
    elif playerMove == 'sp' and computerMove == 'pa':
        print('You lose! computer paper disproved your Spock')
        losses = losses + 1
    elif playerMove == 'sp' and computerMove == 'li':
        print('You lose! computer lizard posioned your Spock')
        losses = losses + 1