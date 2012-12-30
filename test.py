
print len([1.8, 3.6, 6.0, 6.6, 8.8, 9.8, 9.8, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0])







##listOfWords = [0] * 300
##
##for pos in range (len(listOfWords)):
##    listOfWords[pos] = listOfWords[pos] + pos
##
##
##print listOfWords
##print len(listOfWords)
##
##
##
##
##
##














##class intSet(object):
##    """An intSet is a set of integers
##    The value is represented by a list of ints, self.vals.
##    Each int in the set occurs in self.vals exactly once."""
##
##    def __init__(self):
##        """Create an empty set of integers"""
##        self.vals = []
##
##    def insert(self, e):
##        """Assumes e is an integer and inserts e into self""" 
##        if not e in self.vals:
##            self.vals.append(e)
##
##    def member(self, e):
##        """Assumes e is an integer
##           Returns True if e is in self, and False otherwise"""
##        return e in self.vals
##
##    def remove(self, e):
##        """Assumes e is an integer and removes e from self
##           Raises ValueError if e is not in self"""
##        try:
##            self.vals.remove(e)
##        except:
##            raise ValueError(str(e) + ' not found')
##
##    def __str__(self):
##        """Returns a string representation of self"""
##        self.vals.sort()
##        return '{' + ','.join([str(e) for e in self.vals]) + '}'
##
##













##class Coordinate(object):
##    def __init__(self,x,y):
##        self.x = x
##        self.y = y
##
##    def getX(self):
##        # Getter method for a Coordinate object's x coordinate.
##        # Getter methods are better practice than just accessing an attribute directly
##        return self.x
##
##    def getY(self):
##        # Getter method for a Coordinate object's y coordinate
##        return self.y
##
##    def __str__(self):
##        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
##
##    def __eq__(self, other):
##        return (self.getX() == other.getX() and self.getY() == other.getY())
##    
##    def __repr__(self):
##        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'
##
##test = Coordinate(7,11)
##test2 = Coordinate(7,11)
##
##print (repr(test))

##def isPrime(n):
##    if type(n) != int:
##        raise TypeError()
##    if n < 0:
##        raise ValueError()
##    if n == 2:
##        return True
##    elif n < 2:
##        return False
##    for divisor in range(2, int(n**0.5+1)):
##        if n % divisor == 0: 
##            return False
##
##    return True
##print isPrime(7)
##




##def thisRaisesAZeroDivisionError():
##    x = 1/0
##
##def thisRaisesAValueError():
##    y = int('Five')
##
##def thisDoesNotRaiseAnyErrors():
##    z = 'just a string'
##
##def tryExercise():
##    print 'A',
##    try:
##        return
##        print 'B',
##    except ZeroDivisionError as e:
##        print 'C',
##    else:
##        print 'D',
##    finally:
##        print 'E',
##    print 'F'
##
##
##
##
##tryExercise()
##
##
##






###dictTest = {}
###dictTest[['a','b']] = 'word'
##
###tupleTest = "rocks", 0, dictTest
##
###print dictTest
##
##
##def myLog(x, b):
##    '''
##    x: a positive integer
##    b: a positive integer; b >= 2
##
##    returns: log_b(x), or, the logarithm of x relative to a base b.
##    '''
##    # Your Code Here
##
##    if x == 0:
##        return 1
##    
##    power = 0
##    while b**power < x:
##        power += 1
##        if b**power == x or b**(power+1) > x:
##           return power
##
##
##print myLog(0,10)
##
###myLog(150,10)
###print myLog(1000,5)
##
####
####import math
####import random
####
#####print math.floor(math.log (15,3))
####
####
####for i in range (0,10):
####    b = random.randint(2,10)
####    x = random.randint(1, b**10)
####    print str(x) + ' , ' + str(b)
####    print str(myLog(x,b)) + ' , ' + str(math.log (x,b))
####
####
##
##
##def laceStrings(s1, s2):
##    """
##    s1 and s2 are strings.
##
##    Returns a new str with elements of s1 and s2 interlaced,
##    beginning with s1. If strings are not of same length, 
##    then the extra elements should appear at the end.
##    """
##    # Your Code Here
##
##    comboString = ''
##
##    s1Len = len(s1)
##    s2Len = len(s2)
##
##    if s1Len > s2Len:
##        longerLen = s1Len
##    else:
##        longerLen = s2Len
##
##
##    for x in range (0, longerLen):
##        if s1Len > x:
##            comboString += s1[x]
##        if s2Len > x:
##            comboString += s2[x]
##
##    return comboString
##
##
###print laceStrings('1234567', 'dogsaregreat')
##
##
##def laceStringsRecur(s1, s2):
##    """
##    s1 and s2 are strings.
##
##    Returns a new str with elements of s1 and s2 interlaced,
##    beginning with s1. If strings are not of same length, 
##    then the extra elements should appear at the end.
##    """
##    def helpLaceStrings(s1, s2, out):
##        if s1 == '':
##            return out + s2
##        if s2 == '':
##            return out + s1
##        else:
##            return helpLaceStrings(s1[1:len(s1)],s2[1:len(s2)], out + s1[0] + s2[0])
##    return helpLaceStrings(s1, s2, '')
##
##
##
###print laceStringsRecur('1234567', 'dogsaregreat')
##
##def McNuggets(n):
##    """
##    n is an int
##
##    Returns True if some integer combination of 6, 9 and 20 equals n
##    Otherwise returns False.
##    """
##    aMax = n/6 + 1
##    bMax = n/9 + 1
##    cMax = n/20 + 1
##    
##    for a in range (0, aMax):
##        if 6*a == n:
##            return True
##        for b in range (0, bMax):
##            if 6*a + 9*b == n:
##                return True
##            for c in range (0, cMax):
##                if 6*a + 9*b + 20*c == n:
##                    return True
##    return False
##
###print McNuggets(50)
##
##
##def fixedPoint(f, epsilon):
##    """
##    f: a function of one argument that returns a float
##    epsilon: a small float
##  
##    returns the best guess when that guess is less than epsilon 
##    away from f(guess) or after 100 trials, whichever comes first.
##    """
##    guess = 1.0
##    for i in range(100):
##        if abs(f(guess) - guess) < epsilon:
##            return guess
##        else:
##            guess = f(guess)
##    return guess
##
##
##def sqrt(a):
##    def tryit(x):
##        return 0.5 * (a/x + x)
##    return fixedPoint(tryit(a), 0.0001)
##
##
##
##
###print sqrt(25)
###print float(5)
##
#####print ['w','o','r','d'].sort()
#####a = ['w', 'o', 'r', 'd', 's']
#####a.sort()
#####print (a)
####
####
#####a = ['w', 'o', 'r', 'd', 's']
#####a.pop(-1)
#####a.pop(-1)
#####print (a)
####
####
#####print ("worded".replace("d", ""))
####
####
####
####def isWordGuessed(secretWord, lettersGuessed):
####    '''
####    secretWord: string, the word the user is guessing
####    lettersGuessed: list, what letters have been guessed so far
####    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
####      False otherwise
####    '''
####    guessed_len = len(lettersGuessed)
####    
####    for iteration in range(0, guessed_len):
####        if secretWord.find(lettersGuessed[-1]) != -1:
####            secretWord = secretWord.replace(lettersGuessed[-1], "")
####        lettersGuessed.pop(-1)
####
####    if secretWord == "":
####        return True
####    else:
####        return False
####
#####isWordGuessed("bird", ["d","i","b","s","s","s"] )
####
####
####def getGuessedWord(secretWord, lettersGuessed):
####    '''
####    secretWord: string, the word the user is guessing
####    lettersGuessed: list, what letters have been guessed so far
####    returns: string, comprised of letters and underscores that represents
####      what letters in secretWord have been guessed so far.
####    '''
####    # FILL IN YOUR CODE HERE...
####
####    word_len = len(secretWord)
####    ans_string = ""
####    #creates the emppty answer string with _'s
####    for x in range(0, word_len):
####        ans_string = ans_string + "_"
####
####    ans_string = list(ans_string)
####
####    secretWord = list(secretWord)
####
####    guessed_len = len(lettersGuessed)
####    
####    for letter in lettersGuessed:
####        for position in range (0, word_len):
####            if secretWord[position] == letter:
####                ans_string[position] = letter
####        
####
####
####    return ("".join(ans_string))
####
####
#####secretWord = 'apple' 
#####lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']    
#####print (getGuessedWord(secretWord, lettersGuessed))
####
####
####
####
####
####
####def getAvailableLetters(lettersGuessed):
####    '''
####    lettersGuessed: list, what letters have been guessed so far
####    returns: string, comprised of letters that represents what letters have not
####      yet been guessed.
####    '''
####    # FILL IN YOUR CODE HERE...
####
####    remaining_letters = "abcdefghijklmnopqrstuvwxyz"
####     
####    for letter in lettersGuessed:
####        remaining_letters = remaining_letters.replace(letter, "")
####        
####    return (remaining_letters)    
####
####
####
####def chooseWord(wordlist):
####    """
####    wordlist (list): list of words (strings)
####
####    Returns a word from wordlist at random
####    """
####    return random.choice(wordlist)
####
####
####
####
####
####
#####print (getAvailableLetters ([ 'k', 'p', 'r', 's', 'e', 'i',]))
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
######        letter_pos = secretWord.find(lettersGuessed[-1])
######        print (letter_pos)
######
######        while letter_pos != -1:
######            ans_string[letter_pos] = lettersGuessed[-1]
######            letter_pos = letter_pos + 1
######            secretWord[letter_pos:].find(lettersGuessed[-1])
######            print (letter_pos)
######            print (secretWord[letter_pos + 2:])
######        lettersGuessed.pop(-1)
####
####
#####length = 5
#####ans_string = ""
####
#####for x in range(0, length):
#####    ans_string = ans_string + "_"
#####print (ans_string.replace("_", "_ "))
####
#####string = list("rambots")
#####print (string[5])
####
#####string[5] = "r"
####
####
#####print ("".join(string))
####
#####print ("bannnnanssss"[10:].find("a"))class intSet(object):
##    """An intSet is a set of integers
##    The value is represented by a list of ints, self.vals.
##    Each int in the set occurs in self.vals exactly once."""
##
##    def __init__(self):
##        """Create an empty set of integers"""
##        self.vals = []
##
##    def insert(self, e):
##        """Assumes e is an integer and inserts e into self""" 
##        if not e in self.vals:
##            self.vals.append(e)
##
##    def member(self, e):
##        """Assumes e is an integer
##           Returns True if e is in self, and False otherwise"""
##        return e in self.vals
##
##    def remove(self, e):
##        """Assumes e is an integer and removes e from self
##           Raises ValueError if e is not in self"""
##        try:
##            self.vals.remove(e)
##        except:
##            raise ValueError(str(e) + ' not found')
##
##    def __str__(self):
##        """Returns a string representation of self"""
##        self.vals.sort()
##        return '{' + ','.join([str(e) for e in self.vals]) + '}'
######
