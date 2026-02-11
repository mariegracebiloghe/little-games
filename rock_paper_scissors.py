"""
Rock Paper Scissors - Beginner-Friendly Python Project
This game lets a player play Rock, Paper, Scissors against the computer.
"""

# We import random so the computer can pick a random choice each round.
import random


# This list stores all valid choices that both player and computer can use.
VALID_CHOICES = ["rock", "paper", "scissors"]


# This function asks the player for a choice and validates the input.
def get_player_choice():
    # We keep asking until the player enters a valid option.
    while True:
        # input() reads text from the keyboard.
        player_input = input("Choose rock, paper, or scissors: ").strip().lower()

        # If the typed choice is valid, we return it to the game loop.
        if player_input in VALID_CHOICES:
            return player_input

        # If the choice is not valid, we print a helpful message and ask again.
        print("Invalid input. Please type: rock, paper, or scissors.")


# This function randomly selects one option for the computer.
def get_computer_choice():
    # random.choice picks one item from the VALID_CHOICES list.
    return random.choice(VALID_CHOICES)


# This function compares player and computer choices and returns the result message.
def decide_winner(player_choice, computer_choice):
    # If both choices are the same, the round is a tie.
    if player_choice == computer_choice:
        return "It's a tie!"

    # These are the winning situations for the player.
    player_wins = (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    )

    # If one of the winning situations is true, the player wins.
    if player_wins:
        return "You win!"

    # Otherwise, the computer wins.
    return "You lose!"


# This function asks if the player wants to play another round.
def ask_to_play_again():
    # We keep asking until the player gives a clear yes or no.
    while True:
        # Accept y/yes/n/no for beginner-friendly flexibility.
        answer = input("Play again? (y/n): ").strip().lower()

        # If the player says yes, return True.
        if answer in ["y", "yes"]:
            return True

        # If the player says no, return False.
        if answer in ["n", "no"]:
            return False

        # If answer is unclear, ask again.
        print("Please enter 'y' for yes or 'n' for no.")


# This is the main function that runs the full game.
def main():
    # Welcome message shown once at the start.
    print("Welcome to Rock, Paper, Scissors!")

    # This loop allows multiple rounds.
    while True:
        # Get the player's valid choice.
        player_choice = get_player_choice()

        # Get the computer's random choice.
        computer_choice = get_computer_choice()

        # Show both choices to the player.
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        # Decide and display the result.
        result = decide_winner(player_choice, computer_choice)
        print(result)

        # Ask if the player wants to continue.
        if not ask_to_play_again():
            # Exit message before breaking the loop.
            print("Thanks for playing. Goodbye!")
            break

        # Print a blank line to separate rounds.
        print()


# This checks if this file is being run directly.
# If yes, it starts the game by calling main().
if __name__ == "__main__":
    main()
