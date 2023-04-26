#import the random module
from random import randint

#Create a function with the score parameter
def game(score):

    bot = randint(0,2)                              #The bot chooses a random number
    bot_pick = hand[bot]                            #The bot assigns that number to the index of the list and stores it in a variable
    
    user = str(input("\nWhat do you choose?\n")).lower()    #First user input. '.lower()' for lowercase
    score += 0                                      #Calling the parameter, but not changing the score
    
    if user == bot_pick:                            #Statements
        print(bot_pick,"\nIt's a draw.")
        print("\nWanna play another?")
        
        run = str(input("Y/n?")).lower()            #Asks to play again
        
        if run == 'y':
            print("\nLet's GO!")
            game(score)                             #Calls the function with the score remembered
        elif run == 'n':
            print("\nGoodbye!")                     #Exit game
        else:
            print("Please input Y or N!")
            return
        
        game(score)
    
    elif user != bot_pick:                          #if not draw
        print(bot_pick)
        
        if user == hand[0] and bot_pick == hand[1]:
            print("\nYou lost. Paper beats Rock.")
        elif user == hand[0] and bot_pick == hand[2]:
            score += 1
            print("\nYou won. Rock beats Scissors. Your score is :", score)
        elif user == hand[1] and bot_pick == hand[0]:
            score += 1
            print("\nYou won. Paper beats Rock. Your score is :", score)
        elif user == hand[1] and bot_pick == hand[2]:
            print("\nYou lost. Scissors beats Paper.")
        elif user == hand[2] and bot_pick == hand[0]:
            print("\nYou lost. Rock beats Scissors.")
        elif user == hand[2] and bot_pick == hand[1]:
            score += 1
            print("\nYou won. Scissors beats Paper. Your score is :", score)
        else:
            print("error")
        
        print("\nWanna play another?")
        
        run = str(input("Y/n?")).lower()
        
        if run == 'y':
            print("\nLet's GO!")
            game(score)
        elif run == 'n':
            print("\nGoodbye!")
        else:
            print("Please input Y or N!")
            return
    return

hand = ['rock', 'paper', 'scissors']                #Storing the options in a list

print("Hello Player!\nAre you ready to play Rock-Paper-Scissors?")

game(0)                                             #First call of the function
