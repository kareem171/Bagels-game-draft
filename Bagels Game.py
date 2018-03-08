#Bagels game
import random


Num_digits = 3
Max_Guess = 10

def getSecretNum():
    #Returns a string of random digits that is Num_Digits
    number = list(range(10))
    random.shuffle(numbers)
    secretNum = ""
    for i in range(Num_digits):
        secretNum += str(numbers[i])
        #secretNum = secretNum + str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    #Returns a string with the Boo, Blahhh, Ahhh clues to the user
    if guess==secretNum:
        return "You got it!"


    Clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum [i]:
             clues.append("Blahhh")
        elif guess[i] in secretNum:
             clues.append("Ahhh")
    if len(clues)==0:
         return "Boo"



    clues.sort()
    return''.join(clues)


def isOnlyDigits(num):
    #Returns True if num is a string of only digits. Otherwise, returns False
    if num=='':
        return False


    for i in num:
        if i not in "O 1 2 3 4 5 6 7 8 9".split():
            return False
        return True



print("I am thinking of a %s digit number. Try to guess what it is." % (Num_Digits))
print("The clues I give are...")
print("When I say:        That means:")
print("Boo                None of the digits are correct")
print("Blahhh             One digit is correct but in the wrong position")
print("Ahhh               One digit is correct and in the right position")

while True:
    secretNum= getSecretNum()
    print("I have thought up a number. You have %s guesses to get it." % (MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= Max_Guess:
        guess= ""
        while len(guess) != Num_Digits or not isOnlyDigits(guess):
          print("guess #%s:  " % (guessesTaken))
          guess = input()


        print(getClues(guess, secretNum))
        guessesTaken += 1
          
