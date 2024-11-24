def isleap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        leap = True
    return leap

year = int(input())
print(isleap(year))