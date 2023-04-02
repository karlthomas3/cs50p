def main():
    # get input from user
    exp = input("Expression: ")
    # split it up
    x, y, z = exp.split(" ")
    # convert x and z to floats
    x = float(x)
    z = float(z)
    
    match y:
        case "+":
            print(x+z)
        case "-":
            print(x-z)
        case "*":
            print(x*z)
        case "/":
            print(x/z)


main()