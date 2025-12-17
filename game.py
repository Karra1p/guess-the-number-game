import random

def get_user_guess():
    """Get a valid integer guess from the user."""
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")

def play_game(lower=1, upper=100, max_attempts=7):
    """Play one round of the guess-the-number game."""
    secret = random.randint(lower, upper)
    attempts = 0
    print(f"\nI'm thinking of a number between {lower} and {upper}.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1

        if guess < secret:
            print("Too low! Try a higher number.")
        elif guess > secret:
            print("Too high! Try a lower number.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.\n")
            return

        print(f"Attempts left: {max_attempts - attempts}\n")

    print(f"Out of attempts! The number was {secret}.\n")

def main():
    print("=== Guess the Number ===")
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
