
#This problem is so simples. Given a year I have to bring back with the century
#represented by this year
def centuryFromYear(year):
    n = (year % 100)
    o = int(year / 100)
    if n > 0:
        result = o + 1
    else:
        result = o

    return result

n = int(input("Enter with the number:"))
print(centuryFromYear(n))

