def probTest(limit):

    numRolls = 1


    chanceOfSeeingIt = (1.0/6.0)*((5.0/6.0)**(numRolls-1))



    while chanceOfSeeingIt > limit:
        numRolls = numRolls + 1
        chanceOfSeeingIt = (1.0/6.0)*((5.0/6.0)**(numRolls-1))
    return (numRolls)




print probTest(0.1)


def seeIt(tryNum):
    chanceOfSeeingIt = (1.0/6.0)*((5.0/6.0)**(tryNum-1))
    print chanceOfSeeingIt

#seeIt(1)
##    prob = (1.0/6.0)*(5.0/6.0)**(numRolls-1)
##
##    if limit > (1.0/6.0):
##        return 1
##
##    while prob > limit:
##        prob = (1.0/6.0)*(5.0/6.0)**(numRolls-1)
##        numRolls += 1
##        
##
##
##
##    return numRolls - 1
