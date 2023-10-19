import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!", False
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return f"You win! {user_choice.capitalize()} beats {computer_choice}.", True
    else:
        return f"Computer wins! {computer_choice.capitalize()} beats {user_choice}.", True

# Function to update the score
def update_score(result, user_wins, computer_wins, draws):
    if result.startswith("You win"):
        user_wins += 1
    elif result.startswith("Computer wins"):
        computer_wins += 1
    else:
        draws += 1
    return user_wins, computer_wins, draws

# Function to play the game
def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0

    print("Welcome to Rock, Paper, Scissors Game!")

    while True:
        # User input
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        # Check for valid input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please choose from rock, paper, or scissors.")
            continue

        # Computer's choice
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        # Display the computer's choice
        print(f"Computer's choice: {computer_choice.capitalize()}")

        # Determine the winner
        result, continue_game = determine_winner(user_choice, computer_choice)

        # Update the score
        user_wins, computer_wins, draws = update_score(result, user_wins, computer_wins, draws)

        # Display the result and score
        print(result)
        print("User Wins:", user_wins)
        print("Computer Wins:", computer_wins)
        print("Draws:", draws)

        # Check if the game should continue
        play_again = input("Do you want to play another round? (yes/no or 'quit' to quit): ").lower()
        if play_again == "quit":
            break
        if play_again == "no":
            break
    # Display leaderboard at the end of the game
    print("\nGame Over! Leaderboard:")
    print("User Wins:", user_wins)
    print("Computer Wins:", computer_wins)
    print("Draws:", draws)

if __name__ == "__main__":
    play_game()

