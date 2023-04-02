import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # get matches for num strings
    if nums := re.search(r"^([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})$", ip):
        # convert them to ints and return true if <= 255
        if (
            int(nums.group(1)) <= 255
            and int(nums.group(2)) <= 255
            and int(nums.group(3)) <= 255
            and int(nums.group(4)) <= 255
        ):
            return True
    return False


...


if __name__ == "__main__":
    main()
