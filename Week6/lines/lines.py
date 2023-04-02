import sys


def main():
    # check command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    line_count = 0

    # open the file
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                # skip comment lines
                if line.lstrip().startswith("#"):
                    continue

                # skip lines that are all whitespace
                if line.isspace():
                    continue

                # count lines not skipped
                line_count += 1

    except FileNotFoundError:
        sys.exit("File not found")

    print(line_count)


if __name__ == "__main__":
    main()
