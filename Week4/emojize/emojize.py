# imports
import emoji


def main():
    txt = input("Input: ")
    txt = emoji.emojize(txt)
    print("Output:", txt)


if __name__ == "__main__":
    main()
