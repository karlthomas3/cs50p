def main():
    # initialize price
    due = int(50)
    # if due
    while due > 0:
        print("Amount Due: ", due)
        due = due - insert()
    print("Change Due: ", due * -1)

    
def insert():
    while True:
        # request coin, ignoring incorrect input, and return the amount
        n = int(input("Insert Coin: "))
        if n == 5 or n == 10 or n == 25:
            return n
        else:
            return 0


main()