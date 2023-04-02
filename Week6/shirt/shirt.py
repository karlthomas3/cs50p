import os
import sys
from PIL import Image, ImageOps


def main():
    # confirm correct command line arguments using case insensitive extension checks
    if len(sys.argv) != 3:
        sys.exit("Usage: shirt.py IN-FILE OUT-FILE")

    # check infile format
    if (
        os.path.splitext(sys.argv[1])[1].lower() != ".jpg"
        and os.path.splitext(sys.argv[1])[1].lower() != ".jpeg"
        and os.path.splitext(sys.argv[1])[1].lower() != ".png"
    ):
        sys.exit("In-file must be JPEG or PNG")

    # check outfile format
    if (
        os.path.splitext(sys.argv[2])[1].lower() != ".jpg"
        and os.path.splitext(sys.argv[2])[1].lower() != ".jpeg"
        and os.path.splitext(sys.argv[2])[1].lower() != ".png"
    ):
        sys.exit("outfile must be JPEG or PNG")

    # check matching formats
    if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("In-file and out-file must be same formats")

    try:
        # open the before image and the shirt
        with Image.open(sys.argv[1], mode="r", formats=None) as in_file:
            with Image.open("shirt.png", mode="r", formats=None) as shirt:

                # resize image to fit shirt
                in_file = ImageOps.fit(in_file, shirt.size)

                # paste shirt over image
                in_file.paste(shirt, mask=shirt)

                # save new file
                in_file.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
