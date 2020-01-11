import random

# code for a magic 8 ball with ten fortunes


def shake_eight_ball(num):
    if num == 1:
        return "It is certian!"
    if num == 2:
        return "it is decidedly so"
    if num == 3:
        return "YES"
    if num == 4:
        return "Reply hazy ask agian later"
    if num == 5:
        return "try again"
    if num == 6:
        return "unclear ask a different way"
    if num == 7:
        return "my reply is NO"
    if num == 8:
        return "outlook not so good"
    if num == 9:
        return "very doubtful"
    if num == 10:
        return "not happening this month"


r = random.randint(1, 10)

fortune = shake_eight_ball(r)

print(fortune)
