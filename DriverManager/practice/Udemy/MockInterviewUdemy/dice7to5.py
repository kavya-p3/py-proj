from random import randint

def dicevalue():
    return randint(1,7)

def implementdice5from7():
    roll =7
    while roll>5:
        roll = dicevalue()
        print('the retuened value is ',roll)
    print('the final value is ',roll)


implementdice5from7()