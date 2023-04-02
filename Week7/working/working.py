import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    # if time is correct format
    if times := re.search(
        r"^(\d?\d(?::\d\d)?\s(?:AM|PM))\sto\s(\d?\d(?::\d\d)?\s(?:AM|PM))$", s
    ):
        # return reformatted time
        return f"{am_pm(times.group(1))} to {am_pm(times.group(2))}"
    else:
        raise ValueError


def am_pm(hr, m="00"):
    # remove am/pm then split at ":" and convert times.
    # raise value error if anything goes wrong
    if " PM" in hr:
        hr = hr.replace(" PM", "")
        if ":" in hr:
            hr, m = hr.split(":")
        if int(hr) > 12 or int(m) > 59:
            raise ValueError
        if int(hr) < 12:
            hr = int(hr) + 12
        return f"{hr}:{m}"
    else:
        hr = hr.replace(" AM", "")
        if ":" in hr:
            hr, m = hr.split(":")
        if int(hr) > 12 or int(m) > 59:
            raise ValueError
        if int(hr) < 10:
            hr = f"0{hr}"
        if hr == "12":
            hr = "00"
        return f"{hr}:{m}"


if __name__ == "__main__":
    main()
