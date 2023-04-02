

def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    to = to.strip().title()
    first, last = to.split(" ")
    print("hello, ", first)


main()