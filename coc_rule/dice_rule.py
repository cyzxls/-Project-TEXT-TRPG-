import random


def diceGdBad(skill, roll):
    pangung = False
    plmapangung = 1
    if roll == 1:
        pangung = True
        plmapangung = 4
    elif roll == 100 and skill >= 50:
        pangung = False
        plmapangung = -4
    elif roll >= 96 and skill < 50:
        pangung = False
        plmapangung = -4
    else:
        if roll <= skill:
            pangung = True
            if roll < skill // 5:
                plmapangung = 2   
            elif roll < skill // 2:
                plmapangung = 3
        elif roll > skill:
            plmapangung = -1
        
    return pangung, plmapangung