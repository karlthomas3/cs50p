def main():
    # get input, lowercase, and strip whitespace
    fn = input("File name: ").lower().strip()

    # check for file extension
    if fn.endswith(".gif"):
        print("image/gif")
    elif fn.endswith(".jpg") | fn.endswith(".jpeg"):
        print("image/jpeg")
    elif fn.endswith(".png"):
        print("image/png")
    elif fn.endswith(".pdf"):
        print("application/pdf")
    elif fn.endswith(".txt"):
        print("text/plain")
    elif fn.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()