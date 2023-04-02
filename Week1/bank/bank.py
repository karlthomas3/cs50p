def main():
    # get input, strip whitespace from beginning, and correct case
    greeting = input("Greeting: ").lstrip().lower()
    # output amount
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()