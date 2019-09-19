import math

def diagonalDifference(arr):
    soma = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if(i == j):
               soma += arr[i][j]
    k = len(arr) - 1
    l = 0
    soma2 = 0
    while k >= 0 and l < len(arr):
        soma2 += arr[k][l]
            k-=1
            l+-1
        return abs(soma - soma2)



b = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
#There is a huge problem here
print(diagonalDifference(b))
#15
