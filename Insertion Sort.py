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
    fin = arr[-1]

    for num in range(len(arr)-2, -1, -1): 
        if fin < arr[num]:
            arr[num + 1] = arr[num] 
            print(" ".join(map(str, arr)))
        else:
            arr[num + 1] = fin
            print(" ".join(map(str, arr)))
            break
    else:
        arr[0] = fin
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
