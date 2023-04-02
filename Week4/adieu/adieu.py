import inflect


def main():
    # set up inflect
    p = inflect.engine()

    # list for names
    list = []
    while True:
        # keep adding names to the list
        try:
            list.append(input())
        # control-d breaks out and prints the inflected list
        except EOFError:
            list = p.join(list)
            print("Adieu, adieu, to", list)
            return


if __name__ == "__main__":
    main()
