import random 

def main():
    while True:
        try:
            userRange = int(input("Define limit:"))
        except ValueError:
            print("Please select a number")
        else:
            break
    
    tries = 0
    targetNumber = random.randint(0,userRange)

    while True:
        tries+=1
        try:
            userGuess = int(input("Guess:"))
        except ValueError:
            print("Please select a number")
        if userGuess > targetNumber:
            print("Too high")
        elif userGuess <  targetNumber:
            print("Too low")
        else:
            print("Exactly!")
            break
    print(f"Tries: {tries}")

if __name__ == "__main__":
    main()