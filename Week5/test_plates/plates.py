def main():
    # get input
    plate = input("Plate: ")
    
    # check if plate valid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

        
def first_letters(t):
    # convert to list
    t = list(t)
    # iterate first two chars
    for i in range(2):
        if t[i].isalpha() == False:
            return False
    return True

    
def char_count(t):
    # return true if text within correct range
    if len(t) > 2 and len(t) < 7:
        return True
    return False

    
def no_mid_num(t):
    num = False
    # iterate text
    for i in t:
        # first num cant be 0
        if i == "0" and num == False:
            return False
        # flag when num found
        if i.isnumeric():
            num = True
        # if alpha found after num flagged, return false
        if i.isalpha() and num == True:
            return False
    return True


def is_valid(t):
    if char_count(t) and first_letters(t) and no_mid_num(t) and t.isalnum():
        return True
    return False


if __name__ == "__main__":
    main()