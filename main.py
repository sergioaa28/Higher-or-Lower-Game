import os
import random
from art import logo, vs
from game_data import data

def clear_screen():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def play_game():
    """Runs the main game loop."""
    print(logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        # Make account B become the new account A
        account_a = account_b  

        # Pick a new account for B, making sure it's different from A
        account_b = random.choice(data)
        while account_b == account_a:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Clear the screen for better user experience
        clear_screen()
        print(logo)

        # Get follower count of each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if the user is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"✅ You're right! Current score: {score}")
        else:
            print(f"❌ Sorry, that's wrong. Final score: {score}.")
            game_should_continue = False

while True:
    play_game()
    again = input("Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! 👋")
        break
