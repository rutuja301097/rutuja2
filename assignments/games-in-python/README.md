
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input to practice string manipulation, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Implement the Hangman Game

#### Description
Create a complete Hangman game where players guess letters to reveal a hidden word before running out of attempts. The game should randomly select words from a predefined list and handle user input interactively.

#### Requirements
Completed program should:

- Randomly select words from a predefined list (e.g., a list of 5-10 common words).
- Accept single-letter guesses from the user and update the display to show current progress in a format like `_ _ _` (revealing correct letters in their positions).
- Track and display the number of incorrect guesses remaining (e.g., start with 6 attempts).
- End the game when the word is fully guessed or when attempts are exhausted.
- Display appropriate win/lose messages at the end (e.g., "Congratulations! You guessed the word." or "Game over! The word was [word].").
- Handle invalid inputs gracefully (e.g., non-letter characters or repeated guesses).
- Example gameplay flow:
  ```
  Welcome to Hangman!
  Word: _ _ _ _ _
  Guess a letter: a
  Word: _ a _ _ _
  Incorrect guesses left: 5
  ...
  ```
