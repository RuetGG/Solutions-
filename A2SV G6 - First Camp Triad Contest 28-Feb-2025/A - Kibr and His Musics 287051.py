# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

n, m = map(int, input().split())
prod = []  

for i in range(n):
    name , time = map(int, input().split())
    prod.append(name * time)
    if len(prod) == n:
        curr_sum = 0
        prefix = [0] * n
        for i in range(n):
            curr_sum += prod[i]
            prefix[i] = curr_sum
        v = list(map(int, input().split()))
        i = 0
        j = 0
        while i < m:
            while i < m and prefix[j] >= v[i]:
                print(j + 1)
                i += 1
            j += 1