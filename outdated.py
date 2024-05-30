def main():

    while True:
        date =  input("Date: ")
        try:
           if convertdate(date):
               break
            
        except (ValueError, IndexError, ZeroDivisionError):
            print(end="")

def convertdate(usdate):
    if ('/' in usdate):
        yearstd = int(usdate.split("/")[2])
        monthstd = int(usdate.split("/")[0])
        if ((monthstd == 0) or (monthstd > 12)):
            return False
        daystd = int(usdate.split("/")[1])
        if ((daystd == 0) or (daystd > 31)):
            return False
        print(f"{yearstd}-{monthstd:02}-{daystd:02}")
        return True

    elif (',' in usdate):
        yearstd = int(usdate.split()[2])
        monthstd = monthstr2std(usdate.split()[0])
        if (not monthstd):
            return False
        daystd = int(usdate.replace(",","").split()[1])
        if ((daystd == 0) or (daystd > 31)):
            return False
        print(f"{yearstd}-{monthstd}-{daystd}")
        return True
    else:
        return False


def monthstr2std(monthstr):
    month = [
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
    monthstd=1
    for i in month:
        if (i == monthstr):
            return monthstd
        else:
            monthstd+=1
    return False


main()