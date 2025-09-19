# Hangman Word Guessing Game (Python)

This is a simple **word guessing game** similar to hangman but without limit of guesses built with **Python**.  
It uses the **NLTK word corpus** to generate random words based on the chosen difficulty level.

---

## How It Works

### 1. Word Bank Selection
Depending on the difficulty you choose, the program filters the NLTK word list:

- **Easy** → words with 2–4 letters  
- **Medium** → words with 5–6 letters  
- **Hard** → words with 7+ letters

### 2. A Secret Word Is Chosen
From the filtered bank, the program randomly selects a secret word.  

### 3. Enter your guesses until you correctly identify some letter of the word.
- If the letter is in the secret word, it is revealed in the correct position(s).  
- If not, the blanks remain unchanged.  

### 4. Continue Guessing
Keep entering letters until you successfully reveal all letters in the word → You win! 


