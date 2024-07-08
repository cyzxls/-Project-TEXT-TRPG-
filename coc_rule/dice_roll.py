import random
from dice_rule import diceGdBad


def Roll(skill,bonus):
    roll = random.randrange(1,101)
    pangung, plmapangung = diceGdBad(skill,roll+bonus)
    


