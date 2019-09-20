def plusMinus(array):
    l = array
    c = 0
    positive = 0.0000
    negative = 0.0000
    neutro = 0.0000
    for c in range(0, len(l)):
       if (l[c] > 0):
           positive+=1
       if (l[c] == 0):
           neutro+=1
       if (l[c] < 0):
           negative+=1
    total = round(len(l), 4)
    result1 = positive/total
    result2 = negative/total
    result3 = neutro/total

    return round(result1, 4), round(result2, 4), round(result3, 4)


arr = [1, 1, 0, -1, -1, 3]

print(plusMinus(arr))
