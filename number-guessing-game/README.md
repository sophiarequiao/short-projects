# Number Guessing Game

## Project Overview

The objective of this project is to build a simple number guessing game that challenges the user to identify a randomly selected number within a specified range. 

The game begins by allowing the user to define a range by entering a lower and an upper bound (for example, from A to B). Once the range is set, the system randomly selects an integer that falls within this user-defined interval. The user's task is to guess the chosen number using as few attempts as possible. 

The game provides feedback after each guess, helping the user refine their next guess based on whether their previous attempt was too high or too low.

---

## Example: Guessing in a Range from 1 to 100

Suppose the user defines the range from 1 to 100, and the system randomly selects `42` as the target number. The guessing process might look like this:

| Guess | User Input | Feedback    |
|-------|------------|------------|
| 1     | 50         | Too high   |
| 2     | 25         | Too low    |
| 3     | 37         | Too low    |
| 4     | 43         | Too high   |
| 5     | 40         | Too low    |
| 6     | 41         | Too low    |
| 7     | 42         | Correct!   |

**Total Guesses:** 7

---

## How to Play

1. Run the game script.  
2. Enter the lower and upper bounds for the number range.  
3. Enter your guesses until you correctly identify the number.  
4. Use the feedback ("Too high" or "Too low") to refine your next guess.  
