import random
import sys

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"
    
def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

while True:
    print("---ROCK-PAPER-SCISSORS---")
    rounds = int(input("Enter the number of rounds: "))
    player_score = 0
    computer_score = 0
    for i in range(rounds):
        print(f"\nRound {i+1} of {rounds}:")
        player = input("Enter your choice (rock/paper/scissors): ").lower()
        while player not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            player = input("Enter your choice (rock/paper/scissors): ").lower()
        computer = computer_choice()
        print(f"\nYour choice: {player}")
        print(f"Computer's choice: {computer}")
        result = get_winner(player, computer)
        print(result)
        if result == "You win!":
            player_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"Score - You: {player_score}, Computer: {computer_score}")
    print(f"\nFinal Score - You: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("You win the game! Congratulations!")
    elif player_score < computer_score:
        print("You lose the game! Better luck next time!")
    else:
        print("It's a tie game!")
    play_again = input("\nDo you want to Play again? (yes/no):" ).lower()
    while play_again not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again = input("Do you want to Play again? (yes/no):" ).lower()
    if play_again != 'yes':
        print("Exiting...Bye!!")
        sys.exit()