#NOTE... THIS DOESN'T ACTUALLY WORK CORRECTLY as is.  THe isWordGuessed function would need to stop using .pop to be fixed.  This is destructive even outside the function and causes the already guessed array to be lost.
# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed_len = len(lettersGuessed)

    testvar = lettersGuessed
    
    for iteration in range(0, guessed_len):
        if secretWord.find(testvar[-1]) != -1:
            secretWord = secretWord.replace(testvar[-1], "")
        testvar.pop(-1)

    if secretWord == "":
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word_len = len(secretWord)
    ans_string = ""
    #creates the emppty answer string with _'s
    for x in range(0, word_len):
        ans_string = ans_string + "_"

    ans_string = list(ans_string)

    secretWord = list(secretWord)

    guessed_len = len(lettersGuessed)
    
    for letter in lettersGuessed:
        for position in range (0, word_len):
            if secretWord[position] == letter:
                ans_string[position] = letter
        


    return ("".join(ans_string))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remaining_letters = "abcdefghijklmnopqrstuvwxyz"
     
    for letter in lettersGuessed:
        remaining_letters = remaining_letters.replace(letter, "")
        
    return (remaining_letters)    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    word_length = len(secretWord)
    lettersGuessed = []
    mistakesMade = 0
    
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(word_length) + " letters long."
    print "------------"

    while (mistakesMade < 8) and (isWordGuessed(secretWord, lettersGuessed) == False):

        availableLetters = getAvailableLetters(lettersGuessed)

        print "You have " + str(8 - mistakesMade) + " guesses left."
        print "Available letters: " + availableLetters
        guess = raw_input("Please guess a letter: ")
        guess = guess[0].lower()
        
        if availableLetters.find(guess) == -1:
            print "Oops! You've already guessed that letter:" + getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(guess)

            if secretWord.find(guess) != -1:
                print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
            else:
                print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
                mistakesMade = mistakesMade + 1
            
        print "------------"        

    if mistakesMade == 8:
        print "Sorry, you ran out of guesses. The word was " + secretWord

    elif isWordGuessed(secretWord, lettersGuessed) == True:
        print "Congratulations, you won!"

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

##
##x=0
##lets = []
##
##while x <5:
##    x=x+1
##    lets.append('a')
##
##print lets
