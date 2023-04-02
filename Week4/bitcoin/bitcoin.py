import requests
import sys
import json
import numpy


def main():
    # argument check
    try:
        if len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
        num = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument not a number")

    try:
        # query
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        #  isolate the price and remove the ","
        o = response.json()["bpi"]["USD"]["rate"].replace(",", "")
        # convert to float and multiply by argv[1]
        price = float(o) * num
        # print to 4 decimal places
        print(f"${price:,.4f}")

    except requests.RequestException:
        print("Request exception")


if __name__ == "__main__":
    main()
