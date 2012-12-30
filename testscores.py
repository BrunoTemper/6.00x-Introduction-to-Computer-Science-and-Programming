import pylab
import random

def generateScores(numTrials):

    scores = []
    
    for testNum in range (numTrials):

#    grade = int(random.random() * 100)

        grade1 = random.randrange(50, 80)
        grade2 = random.randrange(60, 90)
        grade3 = random.randrange(55, 95)
        finalGrade = (.25 * grade1) + (.25 * grade2) + (.5 * grade3)

##        if finalGrade >= 70 and finalGrade <= 75:
##            count += 1.0
            
        scores.append(finalGrade) 

    return scores

    # Your code here
    pass

def plotQuizzes():


    pylab.hist(generateScores(10000), bins = 7)
 
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()


    
    # Your code here
    pass


plotQuizzes()
