def main():
    # start with list of months
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            # get input from user
            date = input("Date: ").strip()

            # format check
            if date[0].isalpha() and "/" in date:
                raise
            if date[0].isalpha() and not "," in date:
                raise

            # replace space and comma and "/" with "-"
            date = date.replace(" ", "-").replace(",", "").replace("/", "-")

            # split string at "-"
            month, day, year = date.split("-")
                
            # replace month with mm
            if month.capitalize() in months:
                month = months.index(month.capitalize()) + 1

            # convert to ints
            month = int(month)
            day = int(day)
        
            # check for number of days/months
            if day > 31 or month > 12 or len(year) != 4:
                raise
                
            # convert year to int
            year = int(year)

            print(f"{year}-{month:02d}-{day:02d}")
            return
            
        except:
            pass


main()