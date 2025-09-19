import random 

def main():
    while True:
        try:
            userRange = input("Define lower and upper limits (eg: A and B):").strip()
            userRange = userRange.split(" ")
            upperLimit = int(userRange[0])
            lowerLimit = int(userRange[2])
        except (ValueError, IndexError):
            pass
        else:
            break
    
    tries = 0
    targetNumber = random.randint(upperLimit,lowerLimit)

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