#https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    G_col = len(G[1])
    G_row = len(G)
    P_col = len(P[1])
    P_row = len(P)
    print(P_row)
    for i in range(G_row - P_row + 1):
        for j in range(G_col - P_col + 1):
            if(G[i][j:j+P_col] == P[0]):
                print(G[i][j:j+P_col])
                print("hehe")
                print(G[i+1:i+P_row][j:j+P_col])
                print("hehe")
                print(P[1:][:])
                if(G[i+1: i+ P_row][j:j+P_col] == P[1:][:]):
                    return("YES")
                 
    return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()

