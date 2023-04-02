def main():
    # get input
    txt = input("Input: ").strip()
    # print the shortened text
    print(f"Output: {shorten(txt)}")


def shorten(word):
    # list vowels
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    # iterate word and remove vowels
    for i in word:
        if i in vowels:
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()
