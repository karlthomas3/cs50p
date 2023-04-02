import random


def main():
    try:
        # prompt for number
        while True:
            level = input("Level: ")
            if level.isnumeric() and int(level) > 0:
                num = random.randint(1, int(level))
                break

        # prompt for guess
        guess = 0
        while guess != num:
            guess = input("Guess: ")
            if guess.isnumeric():
                guess = int(guess)
                if guess < num:
                    print("Too small!")
                elif guess > num:
                    print("Too large!")
        print("Just right!")
            
    except:
        print("wut")
        pass


if __name__ == "__main__":
    main()
