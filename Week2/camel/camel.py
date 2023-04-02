def main():
    # get input
    camel = input("camelCase: ")
    # split string into list
    snake = list(camel)
    # iterate list
    for i in range(len(snake)):
        # when uppercase found
        if snake[i].isupper():
            # make it lowercase
            snake[i] = snake[i].lower()
            # insert "_" 
            snake.insert(i, "_")
    # iterate/print list on same line
    for j in snake:
        print(j, end="")
    # new line
    print()


main()