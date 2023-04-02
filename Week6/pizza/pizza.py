import sys
import csv
from tabulate import tabulate


def main():
    # check command line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: pizza.py filename.csv")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    table = []

    # open with dictreader, read list into memory then print table with tabulate
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append(row)
        print(tabulate(table, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
