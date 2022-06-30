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
    y_maxm = 0
    x_gaps = 0
    y_gaps = 0
    x_maxm = 0
    for j in range(W):
        maxm = 0
        gap_store = 0
        for i in range(H):
            if(A[i][j] == 0):
                zeroes+=1
            if A[i][j]>maxm:
                maxm = A[i][j]
            
            if(not(i==0) and A[i][j]<=A[i][j-1]):
                print(i,j)
                gap_store+=A[i][j-1]-A[i][j]
            else:
                gap_store+=A[i][j]-A[i][j-1]
                y_gaps+=gap_store
                gap_store = 0
        y_maxm+=maxm
                    
    for i in range(H):
        maxm = 0
        gap_store = 0
        for j in range(W):
            if A[i][j]>maxm:
                maxm = A[i][j]
            
            if(not(j==0) and A[i][j]<=A[i-1][j]):
                print(i,j)
                gap_store+=A[i-1][j]-A[i][j]
            else:
                gap_store+=A[i][j]-A[i-1][j]
                x_gaps+=gap_store
                gap_store = 0
        x_maxm+=maxm
        
    sum_1 = (H*W-zeroes)
    print(f"sum_1: {sum_1}, x_maxm: {x_maxm}, y_maxm: {y_maxm}, x_gaps: {x_gaps}, y_gaps : {y_gaps}")
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
