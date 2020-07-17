
def int2ordinal(i):
    if i < 20: #determining suffix for < 20
        if i == 1: 
            suffix = 'st'
        elif i == 2:
            suffix = 'nd'
        elif i == 3:
            suffix = 'rd'
        else:
            suffix = 'th'  
    else:   #determining suffix for > 20
        tens = str(i)
        tens = tens[-2]
        unit = str(i)
        unit = unit[-1]
        if tens == "1":
           suffix = "th"
        else:
            if unit == "1": 
                suffix = 'st'
            elif unit == "2":
                suffix = 'nd'
            elif unit == "3":
                suffix = 'rd'
            else:
                suffix = 'th'
    return str(i)+ suffix
def main():
    day = int(input("Enter a day between 1 and 31: "))
    month = int(input("Enter a month between 1 and 12: "))
    year = int(input("Enter a year between 1 and 2100: "))
    print("On the", int2ordinal(day), "day of the", int2ordinal(month), \
            "month of the", int2ordinal(year), "year, something amazing happened!")
main()






