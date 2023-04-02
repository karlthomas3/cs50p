def main():
    # start with an empty dict
    list = {}

    while True:
        try:
            # get input from user
            item = input().upper()
            # add to count if in list
            if item in list:
                list[item] += 1
            # add to list if not
            else:
                list[item] = 1
        # control-d breaks loop
        except EOFError:
            # sort a list of the keys
            alist = sorted(list.keys())
            print()
            # print the count and the key
            for i in alist:
                print(list[i], i)
            return


main()