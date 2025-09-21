import random
from nltk.corpus import words
import nltk

def main():
    bankOfWords = chooseLevel("Do you want to play with easy, medium or hard words? ")

    secret_word = random.choice(bankOfWords).lower()
    listOfLetterGuessed=["_" for i in secret_word]

    while True:
        userLetter = input("Guess: ").lower()
        if(userLetter.isalpha()):
            listOfLetterGuessed = verifyLetter(userLetter, secret_word, listOfLetterGuessed)
            for letter in listOfLetterGuessed:
                print(letter)
            if ''.join(listOfLetterGuessed) == secret_word:
                break
    print(f"\n Congratulation!!! You've discovered the word: {secret_word}")

def chooseLevel(prompt):
    nltk.download('words')
    word_list = words.words()
    while True: 
        level = input(prompt).lower()
        match level:
            case "easy":
                bankOfWords = [w.lower() for w in word_list if 2 <= len(w) <= 4]
                break
            case "medium":
                bankOfWords = [w.lower() for w in word_list if 4 < len(w) <= 6]
                break
            case "hard":
                bankOfWords = [w.lower() for w in word_list if len(w) > 6]
                break
            case _:
                pass
    return bankOfWords

def verifyLetter(letter, word, output):
    if letter in word:
        for i in range(len(word)):
            if word[i]==letter:
                output[i]=letter
    return output

if __name__=="__main__":
    main()