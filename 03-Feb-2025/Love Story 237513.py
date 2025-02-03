# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())
for _ in range(t):
    s = input()
    count = 0
    left, right = 0, 0
    res = "codeforces"
    for i in range(10):
        if s[left] != res[right]:
            count += 1
        left += 1
        right += 1
    print(count)