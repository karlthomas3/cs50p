from pyfiglet import Figlet
import sys
import random


def main():
    # set up figlet
    figlet = Figlet()
    fonts = figlet.getFonts()
    # either 0 optional arguments
    if len(sys.argv) == 1:
        f = random.choice(fonts)
    # or 2
    elif (
        len(sys.argv) == 3
        and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
        and sys.argv[2] in fonts
    ):
        f = sys.argv[2]
    else:
        # incorrect usage gets an error message and exits program
        sys.exit("Invalid usage")

    # if we're still here, set the font
    figlet.setFont(font=f)
    # and convert whatever they input
    print(figlet.renderText(input("Input: ")))


if __name__ == "__main__":
    main()
