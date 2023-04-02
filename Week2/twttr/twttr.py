def main():
    # list vowels
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # get input
    txt = input("Input: ")
    # iterat string and replace vowels with nothing
    for i in txt:
        if i in vowels:
            txt = txt.replace(i, "")

    # print new string
    print("Output: ", txt)


main()