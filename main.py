# Write a rock, paper, scissors game
# import random module
import random

OPTIONS = ["rock", "paper", "scissors", "lizard", "spock"]
WINNING_CASES = {
    "scissors": ["paper", "lizard"],
    "paper": ["rock", "spock"],
    "rock": ["lizard", "scissors"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}


def is_valid_choice(choice):
    return choice in OPTIONS


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    if computer_choice in WINNING_CASES[user_choice]:
        return "user"
    return "computer"


def play_round(user_choice):
    normalized_choice = user_choice.lower()
    if not is_valid_choice(normalized_choice):
        raise ValueError(f"Invalid choice: {user_choice}")

    computer_choice = random.choice(OPTIONS)
    return {
        "user_choice": normalized_choice,
        "computer_choice": computer_choice,
        "result": determine_winner(normalized_choice, computer_choice),
    }


# define a function that handle all the logic
def main():

    # get user input
    user_input = input("Enter rock, paper, scissors, lizard, or spock: ").lower()
    # check if the user input is valid
    if not is_valid_choice(user_input):
        print("Invalid input. Please try again.")
        return
    result = play_round(user_input)
    print(f"Computer chose: {result['computer_choice']}")

    if result["result"] == "tie":
        print("It's a tie!")
    elif result["result"] == "user":
        print("You win!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    main()