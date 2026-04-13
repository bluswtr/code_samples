#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem

# iterative (only need the last 3 values)
def stepPerms(n):
    steps = {1:1,2:2,3:4}
    if n == 1:
        return steps[1]
    elif n == 2: 
        return steps[2]
    elif n == 3:
        return steps[3]
    for i in range(4,n+1):
        count = steps[1] + steps[2] + steps[3]
        steps[1] = steps[2]
        steps[2] = steps[3]
        steps[3] = count
    return steps[3]
'''
# dynamic programming method
def stepPerms(n):
    steps = {1:1,2:2,3:4}
    if n == 1:
        return steps[1]
    elif n == 2: 
        return steps[2]
    elif n == 3:
        return steps[3]
    for i in range(4,n+1):
        steps[i] = steps[i-3] + steps[i-2] + steps[i-1]
        # print(steps[i])
    return steps[n]

# recursive memoization

def stepPerms(n):
    memo = {1:1,2:2,3:4}
    return climb_stairsM(n, memo)

def climb_stairsM(n, memo):
    if n in memo:
        return memo[n]
    else:
        memo[n] = climb_stairsM(n-3, memo) + climb_stairsM(n-2, memo) + climb_stairsM(n-1, memo)
        return memo[n]
'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
