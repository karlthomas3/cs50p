import random


def main():

    l = get_level()
    score = 0
    for i in range(10):
        score += problem(l)
    print("Score:", score)


def get_level():
    # make sure user inputs a level 1 2 or 3
    while True:
        l = input()
        if l == "1" or l == "2" or l == "3":
            return l


# generate 2 random numbers of the correct length
def generate_integer(l):
    while True:
        try:
            l = int(l)
            if l == 1 and int(l) < 4:
                return random.randint(0, 9)
            elif l == 2:
                return random.randint(10, 99)
            elif l == 3:
                return random.randint(100, 999)
            else:
                raise ValueError
        except ValueError:
            pass


def problem(l):
    x = generate_integer(l)
    y = generate_integer(l)
    tries = 3
    while tries > 0:
        try:
            guess = input(f"{x} + {y} = ")
            if guess.isnumeric() and int(guess) == x + y:
                return 1
            else:
                print("EEE")
                tries -= 1
        except ValueError:
            pass
    print(x + y)
    return 0


if __name__ == "__main__":
    main()
