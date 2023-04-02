def main():
    while True:
        try:
            # get input
            fraction = input("Fraction: ")
            print(gauge(convert(fraction)))
            break
        except:
            pass


def convert(fraction):
    # get input
    x, y = fraction.split("/")
    # convert to ints
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    # make sure x < y, convert, and return
    if x <= y:
        return round((x / y) * 100)
    else:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
