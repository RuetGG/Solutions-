# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

from collections import Counter
t = int(input())
for i in range(t):
    a, b = list(map(str, input().split()))
    if a[-1] == b[-1] and len(a) != len(b):
        if a[-1] == "S" and len(a) > len(b):
            print("<")
        elif a[-1] == "S" and len(a) < len(b):
            print(">")
        elif a[-1] == "L" and len(a) > len(b):
            print(">")
        elif a[-1] == "L" and len(a) < len(b):
            print("<")
    else:
        if a[-1] == "L" and b[-1] != "L":
            print(">")
        elif b[-1] == "L" and a[-1] != "L":
            print("<")
        elif a[-1] == "S" and b[-1] != "S":
            print("<")
        elif b[-1] == "S" and a[-1] != "S":
            print(">")    

        else:
            print("=")