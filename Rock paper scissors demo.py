#Rock Paper scissors in very few lines
import random
game = ""
while game == "":
    ops = ["rock", "paper", "scissors"]
    comp = ops[random.randint(0,2)]
    user = ops[int(input("Type 0 for rock, 1 for paper, and 2 for scissors: "))]
    if (user == ops[0] and comp == ops[2]) or (user == ops[1] and comp == ops[0]) or (user == ops[2] and comp == ops[1]):
        print("You win! Your choice of ---" + user.upper() + "--- beat the computer's choice of ---" + comp.upper() + "---")
    elif (user == ops[0] and comp == ops[1]) or (user == ops[1] and comp == ops[2]) or (user == ops[2] and comp == ops[0]):
        print("The computer has won, with the choice of ---" + comp.upper() + "--- against your choice of ---" + user.upper() + "---")
    else:
        print("It was a tie! Both you and the computer chose " + user.upper() + "!")
    game = input("Press enter to play again")
