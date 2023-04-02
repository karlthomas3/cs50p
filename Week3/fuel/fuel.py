def main():
    # check user input
    z = check("Fraction: ")
    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else:
        print(round(z), "%", sep="")
        

def check(prompt):
    while True:
        try:
            # get input
            x, y = input(prompt).split("/")
            # convert to ints
            x = int(x)
            y = int(y)
            # make sure x < y, convert, and return
            if x <= y:
                return (x/y)*100
        except:
            pass


main()