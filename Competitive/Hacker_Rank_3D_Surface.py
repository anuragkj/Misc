#https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A,H,W):
    zeroes = 0
    x_maxm = []
    for i in A:
        x_maxm.append(max(i))
        for j in i:
            if j == 0:
              zeroes+=1
    sum_1 = (H*W-zeroes)
    sum_2 = 0
    sum_3 = 0
    y_maxm = []
    x_gaps = []
    y_gaps = []
    for j in range(W):
        maxm = 0
        for i in range(H):
            if A[i][j]>maxm:
                maxm = A[i][j]
            # if (not(i==0 or j == 0 or i == H-1 or j == W-1)):
            #     if A[i][j]<A[i+1][j] and A[i][j]<A[i-1][j]
                    
        y_maxm.append(maxm)
    
    print(2*(sum_1 + sum(x_maxm) + sum(y_maxm)))
    return(1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A,H,W)

    fptr.write(str(result) + '\n')

    fptr.close()
