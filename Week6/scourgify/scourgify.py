import sys
import csv


def main():
    # check command line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: scourgify.py INFILE.csv OUTFILE.csv")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    before = []

    # read before file into memory
    try:
        with open(sys.argv[1]) as infile:
            next(infile)
            # remove quotes, commas, and newlines then split into 3 variables
            for line in infile:
                last, first, house = (
                    line.replace('"', "").replace(" ", "").replace("\n", "").split(",")
                )
                # and add them to the list as dicts
                before.append({"last": last, "first": first, "house": house})

        # open new csv, iterate before list and write dicts to new file
        with open(sys.argv[2], "w") as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in before:
                writer.writerow(i)

    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
