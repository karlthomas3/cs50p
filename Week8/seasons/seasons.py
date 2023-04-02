import datetime
import inflect
import re
import sys

p = inflect.engine()


def main():
    try:
        dob = dob_get(input("Date of birth: "))
        print(f"{time_diff(dob).capitalize()} minutes")
    except ValueError:
        sys.exit("Invalid date")


def dob_get(s):
    # get user to input DOB checking formatting and validity
    if dob := re.search(r"^(\d\d\d\d)-([\d]\d)-(\d\d)$", s):
        year, month, day = int(dob.group(1)), int(dob.group(2)), int(dob.group(3))
        dob = datetime.date(year, month, day)
        return dob
    else:
        raise ValueError


def time_diff(dob):
    # get difference between dob and current date
    # reduce it to minutes and return it in words
    today = datetime.date.today()
    diff = today - dob
    return p.number_to_words(int((diff.total_seconds() / 60)), andword="")


if __name__ == "__main__":
    main()
