import random          # imports the library named random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    user = input("Choose your weapon: ")
    comp = random.choice(['rock','paper','scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

if user == 'rock':
    print('Ha! I really chose paper--I WIN!')

    print("Better luck next time...")
    #process
if user == "paper" and comp == "rock"
    print (f"user{user} win over computer{comp}")
if user == "paper" and comp == "paper"
    print ("Tie game")
if user == "paper" and comp == "scissors"
    print("comp wins")
if comp == "paper" and user == "scissor"
    print("user wins") 
if comp == "scisssors" and user == "scissors"
    print("tie game")
if comp == "rock" and user == "rock"
    print("tie game")
if
    #test functions
    rps()