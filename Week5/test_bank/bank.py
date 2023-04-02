def main():
    # get input, strip whitespace from beginning, and correct case
    greeting = input("Greeting: ").lstrip()
    print(f"${value(greeting)}")


def value(greeting):
    # clean up greeting just in case
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
