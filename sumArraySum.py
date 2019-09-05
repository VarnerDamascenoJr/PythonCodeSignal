#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
#I will receive a array of number.
def simpleArraySum(ar):
#I'll put my array at one variable and initalize anothe with zero value
    l = ar
    a = 0
    #Now I will initialize my loop pushing each value of this array
    #inside my variable a. For end, I return a
    for num in range(len(l)):
        a +=l[num]
    return a    
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
