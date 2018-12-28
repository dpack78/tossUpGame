import random
import constants

def getRoll(diceCount):
    a_roll = []
    a_colorMap = [
        'g','g','g','y','y','r',
    ]
    for i in range(diceCount):
        a_roll.append(random.choice(a_colorMap))
    
    if(constants.DEBUG_ON):
        print('roll: ')
        print(a_roll)
    return a_roll

def rolePassed(a_role):
    hasARed = False
    for color in a_role:
        if(color == 'g'):
            return True
        if(color == 'r'):
            hasARed = True

    if(hasARed):
        return False
    
    return True

def rollScore(a_role):
    score = 0
    for color in a_role:
        if(color == 'g'):
            score += 1
    return score