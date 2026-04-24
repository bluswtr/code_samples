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
#
# Intuition: the number of ways to climb n steps is the sum of the number of ways to climb n-1, n-2, and n-3 steps.
# Solution 1 is an iterative approach that only keeps track of the last 3 values.
# Solution 2 is a dynamic programming approach that stores all values up to n. 
# Solution 3 is a recursive approach with memoization to avoid redundant calculations.

# Solution 1 - iterative (only need the last 3 values)
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

# Solution 2 - dynamic programming method
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

# Solution 3 - recursive memoization
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
    ''' 

'''
4/22/2026
https://neetcode.io/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        s = (n+1) * [0]
        s[0] = 0
        s[1] = 1
        s[2] = 2

        for i in range(3,n+1):
            s[i] = s[i-1] + s[i-2]

        return s[n]
'''