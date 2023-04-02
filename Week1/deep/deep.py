def main():
    # ask the question, correcting case and stripping whitespace
    answer = input("What's the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    # check the answer
    match answer:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


main()