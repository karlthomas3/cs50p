# start with a main
def main():
    # get text
    text = input("Text: ")

    # convert text
    text = convert(text)
    print(text)


def convert(text):
    # replace smileys and frowns
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    # send it back
    return text


main()