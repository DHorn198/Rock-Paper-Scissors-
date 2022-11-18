from random import randint

#This creates a list of playable options
h = ["Rock", "Paper", "Scissors"]

#This makes the computer randomly choose, it is 0,2 b/c number starts at 0, so Rock = 0, P = 1, etc
computer = h[randint(0,2)]

#once player plays a move, it changes to true
player = False

while player == False:
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose...", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose...", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
#Placed if the player wants to end the game, so stops the coding 
    elif player == "End" or "Stop":
        print("Great game!  Thanks for playing!!")      
        break
    else:
        print("That's not a valid play. Check your spelling!")
#Player set back to false causes the loop to continue, for endless game play!
    player = False
    computer = h[randint(0,2)]
