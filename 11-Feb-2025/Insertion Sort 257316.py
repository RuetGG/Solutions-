# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    target = arr[n - 1]
    j = n - 2
    for i in range(n - 2, -1, -1):  
        if target < arr[i]:
            arr[i + 1] = arr[i]
            j -= 1
            print(" ".join(map(str, arr)))
        else:
            arr[i + 1] = target
            print(" ".join(map(str, arr)))
            break  
    if j == -1:  
        arr[0] = target
        print(" ".join(map(str, arr)))  


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)