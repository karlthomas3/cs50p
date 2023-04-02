def main():
    # the menu
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
            
    # start at $0
    total = 0.00

    while True:
        # if the item's in the list, add it's price to the total
        try:
            item = input("Item: ").title()
            total = total + menu[item]
            print(f"Total: ${total:.2f}")
        except EOFError:
            print()
            return
        except KeyError:
            pass


main()