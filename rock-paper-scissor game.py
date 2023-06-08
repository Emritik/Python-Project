import random
choices = ['rock', 'scissor', 'paper']
player_score = 0
computer_score = 0
print("Players score: ", player_score)
print("Computers score: ", computer_score)
while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissor? :").lower()

    if player == computer:
        print("computer: ", computer)
        print("Player: ", player)
        print("Tie!!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("Player: ", player)
            print("You Lose!!")
            computer_score += 1
        if computer == "scissor":
            print("computer: ", computer)
            print("Player: ", player)
            print("You wins!!")
            player_score += 1

    elif player == "paper":
        if computer == "scissor":
            print("computer: ", computer)
            print("Player: ", player)
            print("You Lose!!")
            computer_score += 1
        if computer == "rock":
            print("computer: ", computer)
            print("Player: ", player)
            print("You wins!!")
            player_score += 1

    elif player == "scissor":
        if computer == "rock":
            print("computer: ", computer)
            print("Player: ", player)
            print("You Lose!!")
            computer_score += 1
        if computer == "paper":
            print("computer: ", computer)
            print("Player: ", player)
            print("You wins!!")
            player_score += 1

    play_again = input("Do you want play again:(Yes/No)?? ").lower()
    if play_again != "yes":
        break
print("Player total score: ", player_score)
print("Computer total score", computer_score)
if player_score < computer_score:
    print("You lose this rounds!!")
elif player_score > computer_score:
    print("You win this round congrats!!")
else:
    print("This round is complete on Tie!!")
print("Thanks for playing!!")