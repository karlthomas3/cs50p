def main():
    # get input from user
    time = input("Time: ").strip().lower()
    # convert time
    time = convert(time)

    # output meal if within mealtime
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    # check time format
    if time.endswith(" a.m."):
        # if its am just remove am from the string
        time = time.strip(" a.m.")
    # split the string
    x, y = time.split(":")
    if y.endswith(" a.m."):
        # if its am just remove am from the string
        y = y.strip(" a.m.")
    if y.endswith(" p.m."):
        # if its pm remove pm and add 12 to x
        y = y.strip(" p.m.")
        x = float(x) + 12
    # convert to floats
    x = float(x)
    y = float(y)
    # math out how many hours
    z = ((x*60)+y)/60
    return z


if __name__ == "__main__":
    main()