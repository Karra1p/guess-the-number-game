# Guess the Number Game

A simple Python console game where players guess a randomly generated number with hints and attempt tracking.

## Description

This interactive console game challenges players to guess a secret number within a limited number of attempts. The game provides feedback after each guess ("too high" or "too low") to help players narrow down the correct answer.

## Features

- **Random Number Generation**: Uses Python's `random` module to generate unpredictable target numbers
- **Input Validation**: Handles invalid inputs gracefully with error messages
- **Configurable Parameters**: Easy to adjust number range (default: 1-100) and max attempts (default: 7)
- **Attempt Tracking**: Shows remaining attempts after each guess
- **Replay Option**: Allows players to start a new game without restarting the program
- **Clean Code Structure**: Functions are modular and well-documented with docstrings

## Tech Stack

- **Language**: Python 3.x
- **Libraries**: `random` (standard library)

## How to Run

### Prerequisites
- Python 3.x installed on your system

### Steps

1. Clone the repository:
```bash
git clone https://github.com/Karra1p/guess-the-number-game.git
cd guess-the-number-game
```

2. Run the game:
```bash
python game.py
```

3. Follow the prompts to play!

## How to Play

1. The game will tell you the range of numbers (1-100 by default)
2. You have 7 attempts to guess the correct number
3. After each guess, you'll receive a hint:
   - "Too low! Try a higher number."
   - "Too high! Try a lower number."
   - "🎉 Correct! You guessed it in X attempts."
4. If you run out of attempts, the game reveals the correct number
5. Choose to play again or exit

## Example Output

```
=== Guess the Number ===

I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it.

Enter your guess: 50
Too high! Try a lower number.
Attempts left: 6

Enter your guess: 25
Too low! Try a higher number.
Attempts left: 5

Enter your guess: 37
🎉 Correct! You guessed it in 3 attempts.

Play again? (y/n): n
Thanks for playing!
```

## Code Structure

- `get_user_guess()`: Validates and returns user input
- `play_game()`: Contains the main game logic
- `main()`: Handles the game loop and replay functionality

## Learning Outcomes

This project demonstrates:
- **Control Flow**: Using loops, conditionals, and functions
- **Error Handling**: Try-except blocks for input validation
- **User Interaction**: Reading console input and providing feedback
- **Code Organization**: Separating concerns with modular functions

## Future Enhancements

- Add difficulty levels (Easy, Medium, Hard)
- Track high scores and fastest wins
- Add a hint system (e.g., "You're getting warmer!")
- Implement a GUI version using Tkinter

## Author

**Karra1p**  
Data Analyst | Python Developer  
LinkedIn: [Your LinkedIn Profile]  
GitHub: [@Karra1p](https://github.com/Karra1p)

## License

This project is open source and available under the MIT License.
